import pygame as pg
from classes.Game import Game
import sys

if __name__ == "__main__":
    game = Game()
    game.run()

    # try:
    #     game.run()
    # finally:
    #     pg.quit()
    #     sys.exit()