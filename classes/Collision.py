import pygame as pg
from classes.LevelsGame import LG
from classes.SoundGame import soundGame

class Collision:
    def __init__(self, 
                 game = None):
        self.game = game

    def killObjects(self):
        collidedObjects = pg.sprite.groupcollide(self.game.enemiesSpritesGroup, self.game.playersBulletsGroup, False, True)
        if collidedObjects:
            soundGame.playExplosion('sounds/explosion.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    LG.score += 1 if not LG.bossFlag else 0
                    if LG.bossFlag:
                        LG.bossLife -= 1
                hits[0].explosion()
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesBulletsGroup, self.game.playersSpritesGroup, False, False)
        if collidedObjects:
            soundGame.playExplosionBullet('sounds/explosionBullet.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    LG.playerLife -= 1
                hits[0].explosion(size = (25, 25), image = 'images/explosion/bulletExplosion.png')
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesSpritesGroup, self.game.playersSpritesGroup, False, False)
        if collidedObjects:
            soundGame.playExplosion('sounds/explosion.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    LG.score += 1 if not LG.bossFlag else 0
                    LG.playerLife -= 1
                    if LG.bossFlag:
                        LG.bossLife -= 1
                hits[0].explosion()
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesBulletsGroup, self.game.playersBulletsGroup, False, True)
        if collidedObjects:
            soundGame.playExplosionBullet('sounds/explosionBullet.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                # if hits[0].touch == False:
                hits[0].explosion(size = (25, 25), image = 'images/explosion/bulletExplosion.png')
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()