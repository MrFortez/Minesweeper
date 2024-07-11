import pygame
from pygame.sprite import Group
from constants import *
from abc import ABC, abstractmethod

import globals

# The base class for all sprites in the game.
class Tile(pygame.sprite.Sprite):

    def __init__(self, cordsX, cordsY, spriteX, spriteY) -> None:
        pygame.sprite.Sprite.__init__(self)

        # this will create a surface object with a tile from the tile spritesheet
        self.surf = self.getSprite(globals.spriteSheet, spriteX, spriteY, 16, 16, (32, 32))

        # used for managing the position of the tile onscreen
        self.rect = self.surf.get_rect()
        self.rect.x = cordsX
        self.rect.y = cordsY

        self.isRevealed = False



    # Function to extract a sprite
    def getSprite(self, sheet, x, y, width, height, scale:tuple=None):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        
        # Scale the sprite if a scale is provided
        if scale:
            sprite = pygame.transform.scale(sprite, scale)
        
        return sprite

    # Set the Tile's position on the board
    def setPosition(self, pos):
        if (not (pos[0] < 0 or pos[0] + self.size[0] > WIDTH)):
            self.rect.x = pos[0]
        if (not (pos[1] < 0 or pos[1] + self.size[1] > HEIGHT)):
            self.rect.y = pos[1]   

    # This method is run when the tile is clicked
    def reveal(self):
        self.isRevealed = True
        self.surf = self.getSprite(globals.spriteSheet, 0, 32, 16, 16, (32, 32))

    def hasBeenRevealed(self):
        return self.isRevealed

    def isMine(self):
        return False