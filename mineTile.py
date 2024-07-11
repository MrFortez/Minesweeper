import pygame
from tile import Tile
from pygame.sprite import Group
from constants import *

class MineTile(Tile):
    def __init__(self, cordsX, cordsY, spriteX, spriteY) -> None:
        super().__init__(cordsX, cordsY, spriteX, spriteY)

    def isMine(self):
        return True