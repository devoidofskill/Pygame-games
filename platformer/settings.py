#Game Options

#Sizing / Speed
WIDTH = 480
HEIGHT = 600
FPS = 60
TITLE = "Jumpy boi"
FONT_NAME = 'arial'

#Player Properties
PLAYER_ACCELERATION = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = .8

#Game Properties
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
MOB_LAYER = 2
BOOST_POWER = 100
POW_SPAWN_PCT = 7


#Platform List
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 60),
                 (WIDTH / 2 - 50, HEIGHT * 4/5, 100, 20), (WIDTH/2, HEIGHT/1.55, WIDTH/8, HEIGHT/32),
                 (125, HEIGHT - 350, 100, 20),
                 (175, 100, 50, 20)]
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225,225,0)
