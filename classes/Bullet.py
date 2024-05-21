import pygame as pg
from pygame.math import Vector2
from pygame.transform import rotozoom
from classes.SoundGame import soundGame
from icecream import ic

class Bullet(pg.sprite.Sprite):
    def __init__(self, 
                pos = (0, 0), 
                group = None,
                game = None,
                size = (2, 2),
                color = 'white',
                speed = 0,
                angle = 0,
                shooter = None,
                killBulletDistance = None,
                image  = None):
        super().__init__(group)

        self.game = game
        self.group = group
        self.angle = angle
        self.size = size
        self.color = color
        self.speed = speed
        self.shooter = shooter
        self.killBulletDistance = killBulletDistance
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), self.size)
        self.imageRot = self.image
        self.imageRot = rotozoom(self.imageRot, -self.angle - 90, 1)
        self.rect = self.imageRot.get_rect(center = pos)
        self.oldShootCoordinate = Vector2(self.shooter.rect.center)
        self.vector = Vector2(self.rect.center)
        # self.direction = Vector2()
        self.offset = Vector2().rotate(self.angle)
        self.pos = Vector2(pos) + self.offset
        self.velocity = Vector2(1, 0).rotate(self.angle)
        self.startExplosion = False
        self.touch = False
        self.explosionCount = 0
        self.explosionFrameRate = 10


    def explosion(self, size = (20, 20), image = ''):
        self.startExplosion = True
        self.touch = True
        self.size = size
        self.old_rect_center = self.rect.center
        self.imageRot= pg.transform.scale(pg.image.load(image), self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.old_rect_center


    def move(self):
        self.pos += self.velocity * self.speed * self.game.deltaTime
        self.rect.center = self.pos


    def checkPosition(self):
        if pg.math.Vector2(self.rect.center).distance_to(self.oldShootCoordinate) >= self.killBulletDistance:
            soundGame.playExplosionBullet('sounds/explosionBullet.mp3')
            self.startExplosion = True
            self.explosion(size = (25, 25), image = 'images/explosion/bulletExplosion.png')
            if self.explosionCount == self.explosionFrameRate:
                self.kill()


    def update(self):
        self.checkPosition()
        self.move()
        if self.startExplosion:
            self.explosionCount += 1
        if self.explosionCount == self.explosionFrameRate:
            self.kill()

    
