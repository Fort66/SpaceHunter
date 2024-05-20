import pygame as pg


class ScreenGame:
    def __init__(self, 
                 size = (800, 600),
                 icon = None
                 ):
        self.size = size
        self.screen = pg.display.set_mode(size, pg.RESIZABLE, 32)
        self.icon = pg.display.set_icon(pg.image.load(icon))
        self.caption = pg.display.set_caption('Космический патруль')
        self.rect = self.screen.get_rect()


    

        