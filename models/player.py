from models.grid import Grid
from process import run
from models.configurations import *


class Player:  # Player Class
    def __init__(self):
        self.score = 0
        self.turns = 0
        self.grid = Grid()

    def displayMainMenu(self):

        print("""
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game

0. Exit
""")

    def promptMainMenu(self):
        return input('Please enter an input: ')

    def validateMain(self, option):
        if option == '0':
            print('---- Game Ended----')
        else:
            print(f"You selected option {option}")

    def displayGameMenu(self):
        print(
"""
1.
2.
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu""")

    def startNewGame(self):
        self.turns = 1

    def promptGameMenu(self):
        return input('Please enter an input: ')

    def validateGame(self, option):
        if option == '0':
            print('Returning to main menu...')

        else:
            print(f"You selected option {option}")

    def displayGrid(self):
        self.grid.displayGrid()

    def loadGame(self):
        self.grid.readGridFromFile()

    def saveGame(self):
        with open(savedGameFilename, 'w+') as f:
            gridValue = self.grid.parseGridAsString()
            for row in gridValue:
                f.writelines(row + "\n")

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        pass
