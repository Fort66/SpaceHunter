import pygame as pg
from pygame.locals import *

pg.mixer.pre_init(44100, -16, 2, 2048)
import sys
from icecream import ic

from classes.ScreenGame import win
from classes.CameraGroup import CameraGroup
from classes.Player import Player
from classes.Enemy import Enemy
from classes.LevelsGame import LG
from classes.CheckEvents import CheckEvents
from classes.Collision import Collision
from classes.MiniMap import MiniMap
from classes.InfoScreen import InfoScreen
from source import screenGameSection


class Game:
    def __init__(self):
        pg.init()

        self.source = screenGameSection()
        # self.win = ScreenGame(size = self.source['size'],
        #                       icon = self.source['icon'],)
        self.clock = pg.time.Clock()
        self.deltaTime = 1
        self.FPS = 100
        # self.LG = LevelsGame()
        self.spritesGroups()
        self.setup()
        self.checkEvents = CheckEvents(game = self)
        self.collision = Collision(game = self)
        self.miniMap = MiniMap(game = self, 
                               group = self.cameraGroup)
        self.infoScreen = InfoScreen(game = self, 
                                     group = self.cameraGroup)
        delattr(self, 'source')
        pg.mouse.set_visible(False)
        pg.mouse.set_pos(win.screen.get_width() / 2, win.screen.get_height() / 2)
        # pg.event.set_grab(True)
        
    
    def spritesGroups(self):
        self.cameraGroup = CameraGroup(self)   
        self.enemiesSpritesGroup = pg.sprite.Group()
        self.playersSpritesGroup = pg.sprite.Group()
        self.enemiesBulletsGroup = pg.sprite.Group()
        self.playersBulletsGroup = pg.sprite.Group()


    def clearGroup(self):
        # self.cameraGroup.empty()
        self.enemiesSpritesGroup.empty()
        self.playersSpritesGroup.empty()
        self.enemiesBulletsGroup.empty()
        self.playersBulletsGroup.empty()


    def setup(self):
        self.player = Player(pos = win.rect.center,
                             group = self.cameraGroup,
                             game = self)
        self.playersSpritesGroup.add(self.player)

        for _ in range(LG.enemies if not LG.bossFlag else 1):
            self.enemy = Enemy(pos = self.cameraGroup.backgroundSurface.get_rect(),
                               group = self.cameraGroup,
                               game = self)
            self.enemiesSpritesGroup.add(self.enemy)


    def run(self):
        while True:
            self.deltaTime = self.clock.tick(self.FPS)

            self.checkEvents.checkEvents()
            self.collision.killObjects()

            if len(self.enemiesSpritesGroup) == 0:
                # self.clearGroup()
                # self.LG.nextLevel()
                self.player.kill()
                self.playersSpritesGroup.empty()
                self.enemiesSpritesGroup.empty()
                LG.countingData()
                self.cameraGroup.setBackground()
                self.setup()


            self.infoScreen.setInfoGame(score = LG.score,
                                        playerLife = LG.playerLife,
                                        globalLevel = LG.globalLevel,
                                        currentLevel = LG.currentLevel,
                                        bossLife = LG.bossLife,
                                        boss = False)

            win.screen.fill('black')
            self.cameraGroup.update()
            self.cameraGroup.customDraw(self.player)
            self.miniMap.update()
            self.infoScreen.update()

            
            
                
            # wep = self.enemy.posWeaponRot
            # for w in wep:
            #     x = w[0] - 2.5
            #     y = w[1] - 2.5
            #     pg.draw.rect(self.win.screen, ('red'), (x, y, 5, 5))


            self.clock.tick()

            pg.display.update()







