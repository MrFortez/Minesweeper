import pygame
import globals
from tile import Tile
from pygame.sprite import Group
from constants import *


class MineTile(Tile):
    def __init__(self, pixelX, pixelY, spriteX, spriteY, cordsX, cordsY) -> None:
        super().__init__(pixelX, pixelY, spriteX, spriteY, cordsX, cordsY)

    def isMine(self):
        return True
    
    def reveal(self):
        self.surf = self.getSprite(globals.spriteSheet, 32, 32, 16, 16, (32, 32))