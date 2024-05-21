import pygame as pg
from pygame.math import Vector2
from random import uniform, choice, randint
from icecream import ic
from classes.Bullet import Bullet
import math
from classes.LevelsGame import LG
from classes.SoundGame import soundGame
from pygame.transform import rotozoom
from source import enemiesSection
from source import explosionSection
ENEMIESSECTION = enemiesSection(LG.enemiesLevel)

class Enemy(pg.sprite.Sprite):
    def __init__(self, 
                 pos = None, 
                 group = None,
                 game = None):
        super().__init__(group)

        self.game = game
        self.group = group
        self.size = ENEMIESSECTION['size']
        self.speed = ENEMIESSECTION['speed']
        self.speedBullet = ENEMIESSECTION['speedBullet']
        self. killBulletDistance = ENEMIESSECTION['killBulletDistance']
        self.shotsDistance = ENEMIESSECTION['shotsDistance']
        self.shotsFrequency = ENEMIESSECTION['shotsFrequency']
        self.explosionSize = ENEMIESSECTION['explosionSize']
        self.explosionImage = ENEMIESSECTION['explosionImage']
        if ENEMIESSECTION['image']:
            self.image = pg.transform.scale(pg.image.load(ENEMIESSECTION['image']), self.size).convert_alpha()
        else:
            self.image = pg.Surface(self.size)
            self.image.fill(ENEMIESSECTION['color'])
        self.imageRot = self.image
        self.rect = self.imageRot.get_rect()
        self.rect.center = (uniform(pos[0] + 200, pos[2] - 200), uniform(pos[1] + 200, pos[3] - 200))
        self.direction = Vector2()
        self.vector = Vector2(self.rect.center)
        self.angle = 0
        self.posWeapon = []
        for value in ENEMIESSECTION['weapons']:
            self.posWeapon.append([value[1][0], value[1][1]])
        # delattr(self, 'source')
        self.moveFrameCount = 0
        self.moveFrameMax = 600
        self.moveFrameFlag = False
        self.enemy_bullet = None
        self.startExplosion = False
        self.touch = False
        self.explosionCount = 0
        self.explosionFrameRate = 80


    def explosion(self):
        self.startExplosion = True
        self.touch = True
        self.old_rect_center = self.rect.center
        self.imageRot = pg.transform.scale(pg.image.load(self.explosionImage), self.explosionSize).convert_alpha()
        self.rect = self.imageRot.get_rect()
        self.rect.center = self.old_rect_center


    def rotateVector(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)
    

    @property
    def posWeaponRot(self):
        result = []
        for w in self.posWeapon:
            x, y = w
            newX, newY = self.rotateVector([x, y], self.angle/57.5)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result


    def rotate(self):
        rotateX = self.game.player.rect.centerx - self.rect.centerx
        rotateY = self.game.player.rect.centery - self.rect.centery
        angleRot = - math.atan2(rotateY, rotateX) * 180 / math.pi
        self.angle = -angleRot
        self.imageRot = rotozoom(self.image, angleRot, 1)
        self.rect = self.imageRot.get_rect(center = self.rect.center)


    def move(self):
        if self.moveFrameFlag:
            self.moveFrameCount += 1
            if self.moveFrameCount == self.moveFrameMax:
                self.moveFrameFlag = False
                self.moveFrameCount = 0
        else:
            self.moveFrameFlag = True
            moveX = [0, 1, -1]
            moveY = [0, 1, -1]
            self.direction.x = choice(moveX)
            self.direction.y = choice(moveY)


    def checkPosition(self):
        if self.rect.left <= self.group.backgroundSurface.get_rect().left or self.rect.right >= self.group.backgroundSurface.get_rect().right:
            self.direction.x *= -1

        if self.rect.top <= self.group.backgroundSurface.get_rect().top or self.rect.bottom >= self.group.backgroundSurface.get_rect().bottom:
            self.direction.y *= -1


    def shots(self):
        if (pg.math.Vector2(self.rect.center).distance_to(self.game.player.rect.center)) <= self.shotsDistance and randint(1, self.shotsFrequency * 2) == self.shotsFrequency:
            for value in self.posWeaponRot:
                enemy_bullet = Bullet(
                                        pos = (value[0], value[1]),
                                        group = self.game.cameraGroup,
                                        game = self.game,
                                        size = (3, 15),
                                        color = 'red',
                                        speed = self.speedBullet,
                                        angle = self.angle,
                                        shooter = self,
                                        killBulletDistance = self.killBulletDistance
                                        )
                self.game.enemiesBulletsGroup.add(enemy_bullet)
                soundGame.enemyShots('sounds/enemy_shot.mp3')


    def update(self):
        self.checkPosition()
        self.rotate() if not self.startExplosion else None
        self.move()
        self.shots() if not self.startExplosion else None
        self.rect.center += self.direction * self.speed * self.game.deltaTime
        for value in self.posWeaponRot:
            value[0] += self.direction.x * self.speed * self.game.deltaTime
            value[1] += self.direction.y * self.speed * self.game.deltaTime
        if self.startExplosion:
            self.explosionCount += 1
            if self.explosionCount >= self.explosionFrameRate // 2:
                self.explosionImage = 'images/explosion/smoke.png'
                self.explosion()
        if self.explosionCount == self.explosionFrameRate:
            self.kill()
