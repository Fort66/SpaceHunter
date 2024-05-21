def playersSection(level = 1):
    PLAYERS = {
                1:
                {'image': 'images/player/player.png',
                'weapons': [['gun0', (-30, 0)]],
                'size': (60, 47),
                'color': (255, 255, 255, 0),
                'speed': .4,
                'speedBullet': -.7,
                'bulletImage': 'images/bullet/bullet.png',
                'killBulletDistance': 1000,
                'rotateSpeed': 10,
                'explosion': 'images/explosion/explosion1.png',
                'explosionSound': 'sounds/explosion.mp3',
                'shohtsSound': 'sounds/playerShoot.mp3'},
                2:
                {'image': 'images/player/player1.png',
                    'weapons': [['gun0', (-30, 0)],
                                ['gun1', (0, -18)],
                                ['gun2', (0, 18)]],
                'size': (60, 36),
                'color': (255, 255, 255, 0),
                'speed': .5,
                'speedBullet': -.7,
                'bulletImage': 'images/bullet/bullet.png',
                'killBulletDistance': 1000,
                'rotateSpeed': 10,
                'explosion': 'images/explosion/explosion1.png',
                'explosionSound': 'sounds/explosion.mp3',
                'shootsSound': 'sounds/playerShoot.mp3'},
                }
    return PLAYERS[level]
                        

# enemies section
def enemiesSection(level = 1):
    ENEMIES = {
                1:
                {'image': 'images/enemies/enemy.png',
                'weapons': [['gun0', (18, 0)]],
                'size': (36, 35),
                'color': (139, 0, 0, 0),
                'speed': .2,
                'speedBullet': .4,
                'bulletImage': 'images/bullet/bullet.png',
                'killBulletDistance': 700,
                'explosionImage': 'images/explosion/explosion.png',
                'explosionSize': (100, 100),
                'explosionSound': 'sounds/explosion.mp3',
                'shohtsSound': 'sounds/enemyShoot.mp3',
                'shotsDistance': 500,
                'shotsFrequency': 50},
               2:
                {'image': 'images/enemies/enemy1.png',
                'weapons': [['gun1', (30, 15)],
                            ['gun2', (23, 10)],
                            ['gun3', (23, 20)]],
                'size': (30, 30),
                'color': (139, 0, 0, 0),
                'speed': .2,
                'speedBullet': .4,
                'bulletImage': 'images/bullet/bullet.png',
                'killBulletDistance': 700,
                'explosionImage': 'images/explosion/explosion.png',
                'explosionSize': (100, 100),
                'explosionSound': 'sounds/explosion.mp3',
                'shootsSound': 'sounds/enemyShoot.mp3',
                'shotsDistance': 500,
                'shotsFrequency': 50},
                }
    return ENEMIES[level]



# # boss section
def bossSection(level = 1):
    BOSS = {
            1:
            {'image': 'images/enemies/boss1.png',
            'weapons': [['gun1', (27, 66)],
                        ['gun2', (25, 63)],
                        ['gun3', (29, 63)],
                        ['gun4', (23, 22)],
                        ['gun5', (31, 22)],
                        ['gun6', (18, 25)],
                        ['gun7', (36, 25)],
                        ['gun8', (5, 32)],
                        ['gun8', (50, 32)]],

            'size': (55, 75),
            'speed': .5,
            'speedBullet': .8,
            'bulletImage': 'images/bullet/bullet.png',
            'explosion': 'images/explosionexplosion.png',
            'explosionSound': 'sounds/explosion.mp3',
            'shohtsSound': 'sounds/enemyShoot.mp3'},
                # 2:
                # {'image': 'images/boss2.png',
                # 'weapons': [['gun1', (15, 30)],
                #             ['gun2', (10, 23)],
                #             ['gun3', (20, 23)]],
                # 'size': (30, 30),
                # 'speed': .08,
                # 'speedBullet': .4,
                # 'explosion': 'images/explosion1.png',
                # 'shootsSound': 'sounds/enemyShoot.mp3'},
            }
    return BOSS[level]


# def bulletSection(level = 1):
#     BULLET = {
#               1:
#                 {'killBulletDistance': 2000,},
#               2:
#                 {'killBulletDistance': 2000,},
#              }
#     return BULLET[level]


def backgroundSection(level = 1):
    GALAXYSECTOR = {
                    1: 'images/back/back1.jpg',
                    2: 'images/back/back2.jpg',
                    3: 'images/back/back3.jpg',
                    4: 'images/back/back4.jpg',
                    5: 'images/back/back5.jpg',
                    6: 'images/back/back6.jpg',
                    7: 'images/back/back7.jpg',
                    8: 'images/back/back8.jpg',
                    9: 'images/back/back9.jpg',
                    10: 'images/back/back10.jpg',
                    11: 'images/back/back11.jpg',
                    12: 'images/back/back12.jpg',
                    13: 'images/back/back13.jpg',
                    14: 'images/back/back14.jpg',
                    15: 'images/back/back15.jpg',
                    16: 'images/back/back16.jpg',
                    17: 'images/back/back17.jpg',
                    18: 'images/back/back18.jpg',
                    19: 'images/back/back19.jpg',
                    20: 'images/back/back20.jpg',
                    21: 'images/back/back21.jpg',
                    22: 'images/back/back22.jpg',
                    }
    return GALAXYSECTOR[level]
# self.backgrounds =  {1: 'images/background.png'}


def explosionSection():
    EXPLOSION = {
                 'ships': 'images/explosion/explosion.png',
                 'bullets': 'images/explosion/bulletExplosion.png',
                }




# text section
def textSection(types = 'pauseScreen'):
    TEXT = {
            'pauseScreen':
                        {'textHeading': 'Пауза',
                        'textBody': 'Нажмите F2 для возобновления игры',
                        'colorTransparent': (0, 0, 255, 50),
                        'file': None,
                        'position': 'center'},
            'rulesScreen': 
                        {'textHeading': 'Правила игры',
                        'textBody': 'Нажмите F1 для возобновления игры',
                        'colorTransparent': (0, 0, 255, 50),
                        'file': 'rules_game.txt',
                        'position': 'top'},
            'newGameScreen': 
                        {'textHeading': 'Новая игра',
                        'textBody': 'Нажмите F5 для начала игры',
                        'colorTransparent': (0, 0, 255, 50),
                        'file': None,
                        'position': 'center'},
            # 'nextLevelScreen': 
            #             {'textHeading': f'Сет {str(game.GLG.currentLevel)}',
            #             'textBody': f'Задача - уничтожить {str(game.enemies)} вражеских кораблей',
            #             'colorTransparent': (0, 0, 255, 0),
            #             'file': None,
            #             'position': 'center'},
            }
    return TEXT[types]


def screenSection():
    pass



def screenGameSection():
    SCREENGAME = {'size': (1024, 768),
                  'fullscreen': False,
                  'icon': 'images/enemies/boss2.png',
                  'caption': 'Космический патруль',
                  }
    return SCREENGAME



