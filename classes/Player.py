import pygame as pg
from pygame.math import Vector2
from pygame.transform import rotozoom
from pygame.locals import *
from classes.Bullet import Bullet
from classes.LevelsGame import LG
from source import playersSection
from icecream import ic
PLAYERSSECTION = playersSection(LG.playersLevel)

class Player(pg.sprite.Sprite):
    def __init__(self, 
                 pos = None, 
                 group = None,
                 game = None):
        super().__init__(group)

        self.game = game
        self.group = group
        self.size = PLAYERSSECTION['size']
        self.speed = PLAYERSSECTION['speed']
        self.speedBullet = PLAYERSSECTION['speedBullet']
        self.killBulletDistance = PLAYERSSECTION['killBulletDistance']
        if PLAYERSSECTION['image']:
            self.image = pg.transform.scale(pg.image.load(PLAYERSSECTION['image']), self.size).convert_alpha()
        else:
            self.image = pg.Surface(self.size)
            self.image.fill(PLAYERSSECTION['color'])
        self.imageRot = self.image
        self.rect = self.imageRot.get_rect(center = pos)
        self.direction = Vector2()
        self.vector = Vector2(self.rect.center)
        self.angle = 0
        self.posWeapon = []
        for value in PLAYERSSECTION['weapons']:
            self.posWeapon.append([value[1][0], value[1][1]])
        self.moveLeft = True
        self.moveRight = True
        self.moveUp = True
        self.moveDown = True


    def rotateVector(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)


    @property
    def posWeaponRot(self):
        result = []
        for w in self.posWeapon:
            x, y = w
            newX, newY = self.rotateVector([x, y], self.angle / 57.5)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result


    def rotate(self, angle):
        self.angle += angle
        self.imageRot = rotozoom(self.image, -self.angle, 1)  #
        self.rect = self.imageRot.get_rect(center = self.rect.center)


    def move(self):
        keys = pg.key.get_pressed()
        if keys[K_a] and self.moveLeft:
            self.direction.x = -1
        if keys[K_d] and self.moveRight:
            self.direction.x = 1
        if keys[K_w] and self.moveUp:
            self.direction.y = -1
        if keys[K_s] and self.moveDown:
            self.direction.y = 1


    def checkPosition(self):
        # if self.rect.left <= (self.group.backgroundRect.left + self.game.win.screen.get_width() / 2):
        #     self.rect.left = self.group.backgroundRect.left + self.game.win.screen.get_width() / 2
        #     self.moveLeft = False
        # else:
        #     self.moveLeft = True

        # if self.rect.right >= (self.group.backgroundRect.right - self.game.win.screen.get_width() / 2):
        #     self.rect.right = self.group.backgroundRect.right - self.game.win.screen.get_width() / 2
        #     self.moveRight = False
        # else:
        #     self.moveRight = True

        # if self.rect.top <= self.group.backgroundRect.top + self.game.win.screen.get_height() / 2:
        #     self.rect.top = self.group.backgroundRect.top + self.game.win.screen.get_height() / 2
        #     self.moveUp = False
        # else:
        #     self.moveUp = True

        # if self.rect.bottom >= self.group.backgroundRect.bottom - self.game.win.screen.get_height() / 2:
        #     self.rect.bottom = self.group.backgroundRect.bottom - self.game.win.screen.get_height() / 2
        #     self.moveDown = False
        # else:
        #     self.moveDown = True

        if self.rect.left <= self.group.backgroundRect.left:
            self.rect.left = self.group.backgroundRect.left
            self.moveLeft = False
        else:
            self.moveLeft = True

        if self.rect.right >= self.group.backgroundRect.right:
            self.rect.right = self.group.backgroundRect.right
            self.moveRight = False
        else:
            self.moveRight = True

        if self.rect.top <= self.group.backgroundRect.top:
            self.rect.top = self.group.backgroundRect.top
            self.moveUp = False
        else:
            self.moveUp = True

        if self.rect.bottom >= self.group.backgroundRect.bottom:
            self.rect.bottom = self.group.backgroundRect.bottom
            self.moveDown = False
        else:
            self.moveDown = True


    def shots(self):
        for value in self.posWeaponRot:
            player_bullet = Bullet(
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
            self.game.playersBulletsGroup.add(player_bullet)
            self.game.sound.playerShots('sounds/player_shot.mp3')


    def update(self):
        self.move()
        self.checkPosition()
        self.rect.center += self.direction * self.speed * self.game.deltaTime
        # self.globalCenter += self.direction * self.speed * self.game.deltaTime
        for value in self.posWeaponRot:
            value[0] += self.direction.x * self.speed * self.game.deltaTime
            value[1] += self.direction.y * self.speed * self.game.deltaTime
        self.direction.x = 0
        self.direction.y = 0