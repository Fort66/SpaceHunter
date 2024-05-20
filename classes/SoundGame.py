import pygame as pg

class SoundGame:
    def __init__(self):
        self.background = None

    def play_backgroound(self, background = None):
        if background:
            self.background = pg.mixer.music.load(background)
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(-1)

    def playerShots(self, sound = None):
        if sound:
            channel0 = pg.mixer.Channel(0)
            channel0.set_volume(0.2)
            self.player_shot_sound = pg.mixer.Sound(sound)
            channel0.play(self.player_shot_sound)


    def enemyShots(self, sound = None):
        if sound:
            channel1 = pg.mixer.Channel(1)
            channel1.set_volume(0.05)
            self.enemy_shot_sound = pg.mixer.Sound(sound)
            channel1.play(self.enemy_shot_sound)

    def play_explosion(self, sound = None):
        if sound:
            channel2 = pg.mixer.Channel(2)
            channel2.set_volume(0.25)
            self.explosion_sound = pg.mixer.Sound(sound)
            channel2.play(self.explosion_sound)
    
    def playExplosionBullet(self, sound = None):
        if sound:
            channel3 = pg.mixer.Channel(3)
            channel3.set_volume(0.03)
            self.explosion_sound = pg.mixer.Sound(sound)
            channel3.play(self.explosion_sound)
