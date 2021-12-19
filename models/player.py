import sys
from models.grid import Grid
from models.configurations import *


class Player:  # Player Class
    def __init__(self):
        self.score = 0
        self.turns = 1
        self.grid = Grid()

    #Display first main menu upon launching python code
    def displayMainMenu(self):

        print("""
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game

0. Exit
""")

    #Prompt player for input in first main menu
    def promptMainMenu(self):   
        return input('Please enter an input: ')

    #Validate options made in main menu
    def validateMain(self, option):    
        if option == '0':
            print('---- Game Ended----')
            self.exitGame()
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("2"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

    def gameMenuContent(self, firstBuilding, secondBuilding):
        return (
            f"""
1. Build a {firstBuilding}
2. Build a {secondBuilding}
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu""")

    def displayGameMenu(self, firstBuilding=None, secondBuilding=None):
        if firstBuilding is None and secondBuilding is None:
            firstBuilding, secondBuilding = self.retrieveTwoRandomBuildings()
        print(self.gameMenuContent(firstBuilding, secondBuilding))

    def startNewGame(self):
        self.turns = 1

    #Prompt player for input in InGame main menu
    def promptGameMenu(self):   
        return input('Please enter an input: ')

    #Validate options made in game menu
    def validateGame(self, option):   
        if len(option) == 1 and ord("0") <= ord(option) <= ord("5"):
            print(f"You selected option {option}")
        else:
            print("Invalid option!")

    #Prompt player to check if they saved their game beforehand
    def promptSaveGame(self):     
        return input('Are you sure to exit to main menu without saving game? [Y/N]: ').upper()

    #Validate options for prompting save game.
    def validateSaveGame(self, option):    
        if option.upper() == "Y":
            print('Returning to main menu...')

        elif option.upper() == "N":
            print("Select Option '5' in the game menu to save your game")

        else:
            print("Invalid Option. Returning to Game Menu...")

    #Access grid attribute to display grid
    def displayGrid(self):       
        self.grid.displayGrid()

    #Access grid attribute to
    def loadGame(self):           
        self.grid.readGridFromFile()

    def saveGame(self):     
        with open(savedGameFilename, 'w+') as f:
            gridValue = self.grid.parseGridAsString()
            for row in gridValue:
                f.writelines(row + "\n")

    def retrieveTwoRandomBuildings(self):
        return self.grid.retrieveTwoRandomBuildings()

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        exit(0)
