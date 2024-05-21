import pygame as pg
from classes.ScreenGame import win
from icecream import ic

class InfoScreen:
    def __init__(self, 
                 group = None,
                 game = None):
        
        self.game = game
        self.group = group
        self.infoSize = (win.screen.get_width() - (win.screen.get_width() / 1.5), 50)
        self.font = pg.font.SysFont('arial', 16)


    def setInfoGame(self,
                    score = 0, 
                    playerLife = 0, 
                    globalLevel = 0,
                    currentLevel = 0,
                    bossLife = 0, 
                    boss = False):

        if boss:
            self.infoTextString1 = (f'Уничтожено: {str(score)}  Жизнь: {str(playerLife)}.  Галактика: {str(globalLevel)}  Сектор: {str(currentLevel)} БОСС: жизнь {str(bossLife)}')
            self.infoTextString2 = (f'Пауза: F2  Новая игра: F5  Правила: F1   FPS: {str(round(self.game.clock.get_fps(), 2))}')
        else:
            self.infoTextString1 = (f'Уничтожено: {str(score)}  Жизнь: {str(playerLife)}.  Галактика: {str(globalLevel)}  Сектор: {str(currentLevel)}')
            self.infoTextString2 = (f'Пауза: F2  Новая игра: F5  Правила: F1   FPS: {str(round(self.game.clock.get_fps(), 2))}')

    
    def update(self):
        win.screen.blit(self.font.render(self.infoTextString1, True, 'SlateGrey'), (0, win.screen.get_height() - self.infoSize[1]))

        win.screen.blit(self.font.render(self.infoTextString2, True, 'SlateGrey'), (0, win.screen.get_height() - self.infoSize[1] / 2))

        


