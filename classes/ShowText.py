import pygame as pg

class ShowText:
    def __init__(self, 
                 game = None, 
                 source = None, 
                 typeScreen = None):
        
        self.game = game
        self.source = source
        self.typeScreen = typeScreen
        self.screen = self.game.screen
        self.width = self.game.screen.get_width()
        self.height = self.game.screen.get_height()
        self.heading = pg.font.SysFont('arial', 38)
        self.text = pg.font.SysFont('arial', 24)
        self.textFiles = pg.font.SysFont('arial', 18)
        self.headingColor = 'yellow'
        self.textColor = 'white'
        self.textFilesColor = 'white'

    def textObjects(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()
    
    def changeSource(self, source, typeScreen):
        self.source = source
        self.typeScreen = typeScreen
        self.showText()

    def showText(self):

        self.textHeading = self.source.TEXT[self.typeScreen]['textHeading']
        self.textBody = self.source.TEXT[self.typeScreen]['textBody']
        self.textFile = self.source.TEXT[self.typeScreen]['file']
        self.colorTranapsrent = self.source.TEXT[self.typeScreen]['colorTransparent']
        self.position = self.source.TEXT[self.typeScreen]['position']

        headingSurf, headingRect = self.textObjects(self.textHeading, self.heading, self.headingColor)

        if self.position == 'top':
            headingRect.center = ((self.width / 2), (50))
        
        elif self.position == 'center':
            headingRect.center = ((self.width / 2), (self.height / 2))
        self.screen.blit(headingSurf, headingRect)

        if self.textBody:
            basicSurf, basicRect = self.textObjects(
                self.textBody, self.text, self.textColor)
            
            if self.position == 'top':
                basicRect.center = ((self.width / 2), (100))
            
            elif self.position == 'center':
                basicRect.center = ((self.width / 2), (self.height / 2) + 100)

            self.screen.blit(basicSurf, basicRect)
    
        if self.textFile:
            with open(self.source.TEXT[self.typeScreen]['file'], 'r', encoding = 'utf-8') as file:
                rules_list = []
                for line in file:
                    rules_list.append(line[:-1])
            y_pos = 0
            for lines in rules_list:
                linesSurf, linesRect = self.textObjects(
                    lines, self.textFiles, self.textFilesColor)
                linesRect.x = 20
                linesRect.y = 150 + y_pos
                self.screen.blit(linesSurf, linesRect)
                y_pos += 30

        self.topWindow(self.colorTranapsrent)

    def topWindow(self, colorTransparant):
        topScreen = pg.Surface((self.width(), self.height()), pg.SRCALPHA)
        topScreen.fill(colorTransparant)
        self.screen.blit(topScreen, (0, 0))
        pg.display.update()