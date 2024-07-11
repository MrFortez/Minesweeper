import pygame
from constants import *
import globals
import os
import gameboard

# pygame mixer init
pygame.mixer.init()

# pygame init
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load sprite sheet
globals.spriteSheet = pygame.image.load(os.path.join("art", "minesweeper.png")).convert_alpha()

# Function to extract a sprite
def get_sprite(sheet, x, y, width, height, scale:tuple=None):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))\
    
    # Scale the sprite if a scale is provided
    if scale:
        sprite = pygame.transform.scale(sprite, scale)
    
    return sprite


# Initialize the game board
board = gameboard.Gameboard()
board.initializeBoard()
board.initiateGame()

# Run until the user asks to quit
RUNNING = True
while RUNNING:

    # Update Global Timer
    globals.globalTime = pygame.time.get_ticks()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos() # Get click position
        for row in board.getTileArray():
            for tile in row:
                if tile.rect.collidepoint(x, y): # Check if click is within rectangle
                    tile.whenClicked()
                    break

    for row in board.getTileArray():
        for tile in row:
            screen.blit(tile.surf, tile.rect)

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    globals.clock.tick(120)
    