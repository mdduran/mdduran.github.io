import random, os.path

#import basic pygame modules
import renpygame as pygame
from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit, "Sorry, extended image module required"


def os_path_join(a, b):
    return a + "/" + b

#game variables
TILESIZE       = 16    #width and height of each tile.
WIDTH          = 800
HEIGHT         = 600
WORLDWIDTH     = 48
WORLDHEIGHT    = 36
WORLD          = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],         #world represents the tiles in the game. 0 is an empty tile, 1 is a tile you can walk on, and 2 is the tile with the hat. Player always starts in bottom-left corner.
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],         #NOTE: when accessing one of these numbers, the format is [Y, X]
                  [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                  [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                  [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                  [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                  [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],         #world represents the tiles in the game. 0 is an empty tile, 1 is a tile you can walk on, and 2 is the tile with the hat. Player always starts in bottom-left corner.
                  [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],         #NOTE: when accessing one of these numbers, the format is [Y, X]
                  [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                  [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],         #world represents the tiles in the game. 0 is an empty tile, 1 is a tile you can walk on, and 2 is the tile with the hat. Player always starts in bottom-left corner.
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],         #NOTE: when accessing one of these numbers, the format is [Y, X]
                  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                  [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
                  [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                  [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],         #world represents the tiles in the game. 0 is an empty tile, 1 is a tile you can walk on, and 2 is the tile with the hat. Player always starts in bottom-left corner.
                  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],         #NOTE: when accessing one of these numbers, the format is [Y, X]
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]]

HATLOC         = [WORLDWIDTH - 1, WORLDHEIGHT - 1]
SCREENRECT     = Rect(0, 0, 800, 600)


def load_image(file):
    "loads an image, prepares it for play"
    file = os_path_join('maze_data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os_path_join('maze_data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print 'Warning, unable to load,', file
    return dummysound()



def isPosValid(x, y):
    if x < 0 or x >= WORLDWIDTH or y < 0 or y >= WORLDHEIGHT:
        return False
    elif WORLD[y][x] == 0:      #Yes, x,y is normaly correct, but for this, you have to put y,x
        return False
    
    return True
    
def getInputDirectionX():
    keystate = pygame.key.get_pressed()
    
    direction = 0
    if keystate[K_RIGHT] > 0:
        direction = 1
    elif keystate[K_LEFT] > 0:
        direction = -1
    elif keystate[K_UP] > 0:
        direction = 0
    elif keystate[K_DOWN] > 0:
        direction = 0
        
    return direction
        
def getInputDirectionY():
    keystate = pygame.key.get_pressed()
    
    direction = 0
    if keystate[K_RIGHT] > 0:
        direction = 0
    elif keystate[K_LEFT] > 0:
        direction = 0
    elif keystate[K_UP] > 0:
        direction = -1
    elif keystate[K_DOWN] > 0:
        direction = 1
        
    return direction
# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Player(pygame.sprite.Sprite):
    pos = [0,WORLDHEIGHT - 1]
    images = []
    delay = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        pos = [0,WORLDHEIGHT - 1]
        self.rect = self.image.get_rect().move(self.pos[0] * TILESIZE + 10, (self.pos[1] * TILESIZE) + 10)
        
    def update(self):
        if self.delay < 8:
            self.delay = self.delay + 1

    def move(self, x, y):
        if self.delay < 8 or (x==0 and y==0):
            return
        
        if isPosValid(self.pos[0] + x, self.pos[1] + y):
            self.pos = [self.pos[0] + x, self.pos[1] + y]
            self.delay = 0
        else:
            return
            
        if x < 0:
            self.image = self.images[0]
        elif x > 0:
            self.image = self.images[1]
        elif y < 0:
            self.image = self.images[2]
        elif y > 0:
            self.image = self.images[3]
        
        self.rect.move_ip(x*TILESIZE,y*TILESIZE)
    

class Timer(pygame.sprite.Sprite):
    #timeleft = 1200

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font("DejaVuSans.ttf", 20)

        self.font.set_italic(1)
        self.color = (255, 255, 255)
        self.update()
        self.rect = self.image.get_rect().move(40, HEIGHT - 32)
        
    def update(self):
        #self.timeleft = self.timeleft - 5
        msg = "Time Left: %d" % timeleft
        self.image = self.font.render(msg, 0, self.color)
        #Test for score

            
class Tile(pygame.sprite.Sprite):
    pos = [0,0]
    images = []
    
    def __init__(self, position):
        self.pos = position
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        north = isPosValid(self.pos[0],self.pos[1]-1)
        south = isPosValid(self.pos[0],self.pos[1]+1)
        east = isPosValid(self.pos[0]+1,self.pos[1])
        west = isPosValid(self.pos[0]-1,self.pos[1])
        
        if isPosValid(self.pos[0],self.pos[1]):
            if north and south and east and west:
                self.image = self.images[14]
            elif north and south and west:
                self.image = self.images[10]
            elif south and east and west:
                self.image = self.images[11]
            elif north and east and west:
                self.image = self.images[12]
            elif north and south and east:
                self.image = self.images[13]
            elif south and east:
                self.image = self.images[6]
            elif north and east:
                self.image = self.images[7]
            elif south and west:
                self.image = self.images[8]
            elif north and west:
                self.image = self.images[9]
            elif east and west:
                self.image = self.images[0]
            elif north and south:
                self.image = self.images[1]
            elif east:
                self.image = self.images[2]
            elif north:
                self.image = self.images[3]
            elif south:
                self.image = self.images[4]
            elif west:
                self.image = self.images[5]
            else:
                self.image = self.images[15]
        else:
            self.image = self.images[15]
            
        self.rect = self.image.get_rect().move(self.pos[0] * TILESIZE + 10, (self.pos[1] * TILESIZE) + 10)
        
class Hat(pygame.sprite.Sprite):
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect().move(HATLOC[0] * TILESIZE + 10, (HATLOC[1] * TILESIZE) + 10)

        
def main(winstyle = 0):
    # Initialize pygame
    pygame.init()

    if pygame.mixer and not pygame.mixer.get_init():
        print 'Warning, no sound'
        pygame.mixer = None

    # Set the display mode
    if store._preferences.fullscreen:
        winstyle = FULLSCREEN
    else:
        winstyle = 0

    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    
    horizontal = load_image('horizontal.png')   #0
    vertical = load_image('vertical.png')       #1
    
    ende = load_image('ende.png')               #2
    endn = load_image('endn.png')               #3
    ends = load_image('ends.png')               #4
    endw = load_image('endw.png')               #5
    
    bendes = load_image('bendes.png')           #6
    bendne = load_image('bendne.png')           #7
    bendsw = load_image('bendsw.png')           #8
    bendwn = load_image('bendwn.png')           #9
    
    threewaye = load_image('threewaye.png')     #10
    threewayn = load_image('threewayn.png')     #11
    threeways = load_image('threeways.png')     #12
    threewayw = load_image('threewayw.png')     #13
    
    fourway = load_image('fourway.png')         #14
    
    empty = load_image('empty.png')             #15
    
    
    left = load_image('playerleft.gif')
    up = load_image('playerup.gif')
    down = load_image('playerdown.gif')
    Player.images = [left, pygame.transform.flip(left, 1, 0), up, down]
    Tile.images = [horizontal, vertical, ende, endn, ends, endw, bendes, bendne, bendsw, bendwn, threewaye, threewayn, threeways, threewayw, fourway, empty]
    Hat.images = [load_image('hat.gif')]
    #decorate the game window
    #icon = pygame.transform.scale(Alien.images[0], (32, 32))
    #pygame.display.set_icon(icon)
    #pygame.display.set_caption('MAZE')
    pygame.mouse.set_visible(1)

    #create the background, tile the bgd image
    bgdtile = load_image('empty.png')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    #myfont = pygame.font.SysFont("monospace", 15)
    #label = myfont.render("Time left: 80", 1, (255,255,0))
    #screen.blit(label, (100, 100))
    pygame.display.flip()

    #load the sound effects
    #boom_sound = load_sound('boom.wav')
    #shoot_sound = load_sound('car_door.wav')
    #if pygame.mixer:
    #    music = os_path_join('data', 'house_lo.wav')
    #    pygame.mixer.music.load(music)
    #    pygame.mixer.music.play(-1)

    # Initialize Game Groups
    tiles = pygame.sprite.Group()
    all = pygame.sprite.OrderedUpdates()

    #assign default groups to each sprite class
    Timer.containers = all
    Player.containers = all
    Hat.containers = all
    Tile.containers = all

    #Create Some Starting Values
    #global# score
    clock = pygame.time.Clock()
    
    global timeleft
    
    timeleft = 120

    #initialize our starting sprites
    #Tile() #note, this 'lives' because it goes into a sprite group
    
    #add tiles to world
    for x in range(0, WORLDWIDTH):
        for y in range(0, WORLDHEIGHT):
            Tile([x,y])
            
    Hat()
    player = Player()
    #timer = Timer()

    if pygame.font:
        all.add(Timer())

    while timeleft > 0:
        milliseconds = clock.tick(40)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
        timeleft = timeleft - seconds
        
        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return -1
                
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        #handle player input
        player.move(getInputDirectionX(), getInputDirectionY())
        
        if player.pos == HATLOC:
            return 1

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)

    return 0
