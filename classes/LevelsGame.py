from pygame.math import lerp
from source import *


class LevelsGame:
    def __init__(self):
        self.score = 0
        self.oldScore = 0

        self.playersLevel = 1
        self.playerLife = 5

        self.globalLevel = 1
        self.currentLevel = 1
        self.finalLevel = 5

        self.enemiesLevel = 1
        self.attackLevel = 1
        self.enemiesAmountMin = 10
        self.enemies = round(lerp(self.enemiesAmountMin, 20, self.attackLevel / self.finalLevel))
        self.bossLevel = 1
        self.bossLife = 10
        self.bossAmount = 1
        self.bossTime = 5
        self.bossFlag = False
        
        self.galaxySector = 1

    def countingData(self):

        if self.score - self.oldScore == self.enemies:
            if not self.bossFlag:
                self.enemies = round(lerp(self.enemies, 20, self.attackLevel / self.finalLevel))
                self.currentLevel += 1
                self.playerLife += 1
                self.galaxySector += 1
            self.oldScore = self.score
        
        # if self.currentLevel % self.bossScreen +1 == 0:
        #     self.bossLevel += 1
            
        if self.currentLevel % 6 == 0:
            self.bossFlag = True
            self.globalLevel += 1
            self.currentLevel += 1

        # if len(self.PLAYERS) > self.playersLevel and not self.bossFlag:
        #     self.playersLevel = self.globalLevelGame

        # if len(self.ENEMIES) > self.enemiesLevel and not self.bossFlag:
        #     self.enemiesLevel = self.globalLevelGame

    
    def resetData(self):
        self.score = 0
        self.oldScore = 0

        self.playersLevel = 1
        self.playerLife = 5

        self.globalLevel = 1
        self.currentLevel = 1
        self.finalLevel = 5

        self.enemiesLevel = 1
        self.enemiesAmountMin = 10
        self.attackLevel = 1
        self.enemies = round(lerp(self.enemiesAmountMin, 20, self.attackLevel / self.finalLevel))
        self.bossLevel = 1
        self.bossLife = 10
        self.bossAmount = 1
        # self.bossTime = 5
        self.bossFlag = False
        
        self.galaxySector = 1


LG = LevelsGame()