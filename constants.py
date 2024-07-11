# import libraries that you will need
import pygame
from random import randint, choice

# constants for screen size
WIDTH = 1024
HEIGHT = 768

# constants for colors
RED = [0xe3, 0x1b, 0x23]
BLUE = [0x00,0x2F,0x8B]
GREY = [0xA2, 0xAA, 0xAD]
WHITE = [0xFF, 0xFF, 0xFF]
BLACK = [0x00, 0x00, 0x00]
GREEN = (0, 255, 0)

COLORS = [BLUE, RED, GREY, WHITE, BLACK, GREEN]

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)
