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
    
    # Reveals all adjacent non-mine tiles (only used for if this tile was revealed and is a blank tile)
    def expand(self, tile):
        for row in range(tile.cordsX - 1, tile.cordsX + 2):
            for column in range(tile.cordsY - 1, tile.cordsY + 2):

                # Account for the underflow of putting a negative number as the index of an array.
                # This was causing the expansion to reveal tiles on the opposite side of the board.
                if (row >= 0 and column >= 0):

                    # This try/except statement protects from trying to check a tile outside the bounds of the game.
                    try:
                        # Only attempt to reveal a tile if it is both not a mine and hasnt been revealed yet.
                        if (not self.getTileArray()[row][column].isMine() and not self.getTileArray()[row][column].hasBeenRevealed()):
                            self.getTileArray()[row][column].reveal()

                            # If a tile revealed through this method is itself a blank tile, repeat the process again with that tile
                            if (self.getTileArray()[row][column].getNumber() == 0):
                                self.expand(self.getTileArray()[row][column])
                    except:
                        pass

    # Reveals every tile
    def revealAll(self):
        for row in self.tileArray:
            for tile in row:
                tile.reveal()

    # This generates the board of tiles
    def initializeBoard(self):
        for i in range(0, globals.boardSize[0]):

            # This creates a new row for tiles.
            self.tileArray.append([])
            for j in range(0, globals.boardSize[1]):

                # This places a new tile onto the board, defaulting to the unlicked state.
                self.tileArray[i].append(NumberTile(i * 32, j * 32, 16, 32, i, j));

    # This only occurs after the player clicks their first tile, randomly placing mines throughout the board.
    def initiateGame(self):
        numOfTiles = globals.boardSize[0] * globals.boardSize[1]
        numOfMines = (int)(numOfTiles * globals.mineDensity)

        # Place each mine in a random spot
        for i in range(0, numOfMines):
            validLocation = False

            # If a tile is already a mine, reroll the target to ensure that a mine is place in a new spot.
            # Additionally, if the tile is the one that was clicked first, or is one of the tiles surrounding it, it cant be a mine
            while(not validLocation):
                targetRow = randint(0, globals.boardSize[0] - 1)         
                targetColumn = randint(0, globals.boardSize[1] - 1) 
                validLocation = True
                if (self.getTileArray()[targetRow][targetColumn].isMine()):
                    validLocation = False

                else:
                    for row in range(targetRow - 1, targetRow + 2):
                        for column in range(targetColumn - 1, targetColumn + 2):
                            try:
                                validLocation = not self.getTileArray()[row][column].hasBeenRevealed()
                            except:
                                pass
                            if (not validLocation):
                                break
                            
                        if (not validLocation):
                            break

            # Place the mine
            self.getTileArray()[targetRow][targetColumn] = MineTile(targetRow * 32, targetColumn * 32, 16, 32, targetRow, targetColumn)

            # Increment the value of number tiles surrounding the chosen mine.
            for row in range(targetRow - 1, targetRow + 2):
                for column in range(targetColumn - 1, targetColumn + 2):
                    # if the chosen tile is out of bounds, dont do anything to it
                    if (row < 0 or row > globals.boardSize[0] - 1 or column < 0 or column > globals.boardSize[1] - 1):
                        pass
                    
                    # if the chosen tile is itself a mine, dont do anything to it
                    elif (self.getTileArray()[row][column].isMine()):
                        pass

                    # Increment the number of the tile
                    else:
                        self.getTileArray()[row][column].addNumber(1)






