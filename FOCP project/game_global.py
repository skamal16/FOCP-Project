import pygame, sys
pygame.init()

width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
FPS = 60
clock = pygame.time.Clock()
gravity = -2

GREY = (150, 150, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

comicsans_font = pygame.font.SysFont('comicsans',30)
menu_font = pygame.font.SysFont('blackadderitc', 100)
blackadderitc_font = pygame.font.SysFont('blackadderitc', 30)

MOVE_SPEED = 1
pygame.display.set_caption("I/O")

ENEMYSPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMYSPAWN, 400)

PARTICLESPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(PARTICLESPAWN, 500)

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)
