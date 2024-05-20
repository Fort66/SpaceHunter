import pygame as pg

class Collision:
    def __init__(self, 
                 game = None):
        self.game = game

    def killObjects(self):
        collidedObjects = pg.sprite.groupcollide(self.game.enemiesSpritesGroup, self.game.playersBulletsGroup, False, True)
        if collidedObjects:
            self.game.sound.play_explosion('sounds/explosion.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    self.game.LG.score += 1 if not self.game.LG.bossFlag else 0
                    if self.game.LG.bossFlag:
                        self.game.LG.bossLife -= 1
                hits[0].explosion()
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesBulletsGroup, self.game.playersSpritesGroup, False, False)
        if collidedObjects:
            self.game.sound.playExplosionBullet('sounds/explosionBullet.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    self.game.LG.playerLife -= 1
                hits[0].explosion(size = (25, 25), image = 'images/bullet_explosion1.png')
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesSpritesGroup, self.game.playersSpritesGroup, False, False)
        if collidedObjects:
            self.game.sound.play_explosion('sounds/explosion.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                if hits[0].touch == False:
                    self.game.LG.score += 1 if not self.game.LG.bossFlag else 0
                    self.game.LG.playerLife -= 1
                    if self.game.LG.bossFlag:
                        self.game.LG.bossLife -= 1
                hits[0].explosion()
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()


        collidedObjects = pg.sprite.groupcollide(self.game.enemiesBulletsGroup, self.game.playersBulletsGroup, False, True)
        if collidedObjects:
            self.game.sound.playExplosionBullet('sounds/explosionBullet.mp3')
            hits = list(collidedObjects)
            if hits[0].startExplosion == False:
                # if hits[0].touch == False:
                hits[0].explosion(size = (25, 25), image = 'images/bullet_explosion1.png')
            if hits[0].explosionCount == hits[0].explosionFrameRate:
                hits[0].kill()