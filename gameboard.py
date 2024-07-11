import pygame
import constants
import globals
from tile import Tile
from mineTile import MineTile
from numberTile import NumberTile
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
                self.tileArray[i].append(NumberTile(i * 32, j * 32, 16, 32));

    # This only occurs after the player clicks their first tile, randomly placing mines throughout the board.
    def initiateGame(self):
        numOfTiles = globals.boardSize[0] * globals.boardSize[1]
        numOfMines = (int)(numOfTiles * globals.mineDensity)

        # Place each mine in a random spot
        for i in range(0, numOfMines):
            targetRow = randint(0, globals.boardSize[0] - 1)         
            targetColumn = randint(0, globals.boardSize[1] - 1) 

            # If a tile is already a mine, reroll the target to ensure that a mine is place in a new spot.
            # Additionally, if the tile is the one that was clicked first, it cant be a mine
            while (self.getTileArray()[targetRow][targetColumn].isMine() or self.getTileArray()[targetRow][targetColumn].hasBeenRevealed()):
                targetRow = randint(0, globals.boardSize[0] - 1)         
                targetColumn = randint(0, globals.boardSize[1] - 1)   

            # Place the mine
            self.getTileArray()[targetRow][targetColumn] = MineTile(targetRow * 32, targetColumn * 32, 32, 32)

            # Increment the value of number tiles surrounding the chosen mine.
            for row in range(targetRow - 1, targetRow + 2):
                for column in range(targetColumn - 1, targetColumn + 2):
                    print(row)
                    print(column)
                    # if the chosen tile is out of bounds, dont do anything to it
                    if (row < 0 or row > globals.boardSize[0] - 1 or column < 0 or column > globals.boardSize[1] - 1):
                        pass
                    
                    # if the chosen tile is itself a mine, dont do anything to it
                    elif (self.getTileArray()[row][column].isMine()):
                        pass

                    # Increment the number of the tile
                    else:
                        self.getTileArray()[row][column].addNumber(1)






