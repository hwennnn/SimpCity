import sys
from models.grid import Grid
from models.configurations import *


class Player:  # Player Class
    def __init__(self):
        self.score = 0
        self.turns = 1
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
            self.exitGame()
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("2"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

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
        if len(option) == 1 and ord("0") <= ord(option) <= ord("5"):
            print(f"You selected option {option}")
        else:
            print("Invalid option!")

    def promptSaveGame(self):
        return input('Are you sure to exit to main menu without saving game? [Y/N]: ').upper()

    def validateSaveGame(self, option):
        if option.upper() == "Y":
            print('Returning to main menu...')

        else:
            print("Select Option '5' in the game menu to save your game")

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
        exit(0)
