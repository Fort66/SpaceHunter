import pygame as pg


class Radar:
    def __init__(self, screen, x, y, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pg.draw.line(self.screen, self.color, (self.x, self.y), (self.x + self.radius, self.y), 1)