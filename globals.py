import pygame
import os

# Set up Sprite Groups
# players = pygame.sprite.Group()

# enemies = pygame.sprite.Group()

# playerProjectiles = pygame.sprite.Group()

# enemyProjectiles = pygame.sprite.Group()

# Set up the game clock
clock = pygame.time.Clock()
globalTime = pygame.time.get_ticks()

# Initialize sprite sheet
spriteSheet = None

# Editable Game Variables
boardSize = (19, 19)

# percentage of tiles that are mines.
mineDensity = .15

# keep this as a multiple of 16 for a normal gameplay experience
tileSize = 32