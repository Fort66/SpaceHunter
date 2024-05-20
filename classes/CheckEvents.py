import pygame as pg
from pygame.locals import *
from pygame.math import Vector2
import sys




class CheckEvents:
     def __init__(self, game = None):
         self.game = game
         self.angle = 0
         

     def checkEvents(self):
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.game.player.shots()
            
            if event.type == MOUSEWHEEL:
                if event.y == 1:
                    self.angle = -10
                    self.game.player.rotate(self.angle)

                if event.y == -1:
                    self.angle = 10
                    self.game.player.rotate(self.angle)

