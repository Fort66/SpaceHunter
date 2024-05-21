import pygame as pg
from source import screenGameSection
SCREENGAMESECTION = screenGameSection()

class ScreenGame:
    def __init__(self, 
                 size = SCREENGAMESECTION['size'],
                 icon = SCREENGAMESECTION['icon'],
                 caption = SCREENGAMESECTION['caption'],
                 ):
        if SCREENGAMESECTION['fullscreen']:
            self.screen = pg.display.set_mode(size, pg.FULLSCREEN)
        else:
            self.screen = pg.display.set_mode(size, pg.RESIZABLE, 32)
        self.icon = pg.display.set_icon(pg.image.load(icon))
        self.caption = pg.display.set_caption(SCREENGAMESECTION['caption'])
        self.rect = self.screen.get_rect()

win = ScreenGame()
    

        