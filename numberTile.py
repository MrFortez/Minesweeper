import pygame
import globals
from tile import Tile
from pygame.sprite import Group
from constants import *

class NumberTile(Tile):
    def __init__(self, pixelX, pixelY, spriteX, spriteY, cordsX, cordsY, number = 0) -> None:
        super().__init__(pixelX, pixelY, spriteX, spriteY, cordsX, cordsY)
        self.number = number

    # a check used to determine if the given tile is a mine
    def isMine(self):
        return False
    
    # adds the given value to the number
    def addNumber(self, val):
        self.number += val

    def getNumber(self):
        return self.number
    
    def reveal(self):
        self.isRevealed = True

        if (self.number >=1 and self.number <= 4):
            self.surf = self.getSprite(globals.spriteSheet, (self.number - 1) * 16, 0, 16, 16, (32, 32))

        elif (self.number >=5 and self.number <= 8):
            self.surf = self.getSprite(globals.spriteSheet, (self.number - 5) * 16, 16, 16, 16, (32, 32))

        else:
            self.surf = self.getSprite(globals.spriteSheet, 0, 32, 16, 16, (32, 32))
            