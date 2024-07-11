import pygame
import constants
import globals
from tile import Tile
from mineTile import MineTile
# from numberTile import NumberTile
from random import randint, choice, shuffle


class Gameboard():
    def __init__(self):
        self.tileArray = []

    def getTileArray(self):
        return self.tileArray
    
    # This generates the board of tiles
    def initializeBoard(self):
        for i in range(0, globals.boardSize[0]):

            # This creates a new row for tiles.
            self.tileArray.append([])
            for j in range(0, globals.boardSize[1]):

                # This places a new tile onto the board, defaulting to the unlicked state.
                self.tileArray[i].append(Tile(i * 32, j * 32, 16, 32));

    # This only occurs after the player clicks their first tile, randomly placing mines throughout the board.
    def initiateGame(self):
        numOfTiles = globals.boardSize[0] * globals.boardSize[1]
        numOfMines = (int)(numOfTiles * globals.mineDensity)

        for i in range(0, numOfMines):
            targetRow = randint(0, globals.boardSize[0] - 1)         
            targetColumn = randint(0, globals.boardSize[1] - 1) 

            while (self.getTileArray()[targetRow][targetColumn].isMine()):
                targetRow = randint(0, globals.boardSize[0] - 1)         
                targetColumn = randint(0, globals.boardSize[1] - 1)   
                   
            self.getTileArray()[targetRow][targetColumn] = MineTile(targetRow * 32, targetColumn * 32, 32, 32)



