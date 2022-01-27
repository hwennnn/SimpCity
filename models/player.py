from models.grid import Grid
from models.configurations import *


class Player:  # Player Class
    def __init__(self):
        self.turns = 1
        self.grid = Grid()
        self.firstBuilding = self.secondBuilding = None
        self.savedGame = False

    # Display first main menu upon launching python code
    def displayMainMenu(self):
        mainMenuContent = [
            "\nWelcome, mayor of Simp City!",
            "----------------------------",
            "1. Start new game",
            "2. Load saved game",
            "3. Show high scores",
            "4. Options\n",
            "0. Exit"
        ]

        print("\n".join(mainMenuContent))

    # Prompt player for input in first main menu
    def promptMainMenu(self):
        return input('Please enter an input: ')

    # Validate options made in main menu
    def validateMain(self, option):
        if option == '0':
            print('---- Game Ended ----')
            self.exitGame()
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("4"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

    # Function that facilitates the process of entering the game options menu
    def displayOptionMenu(self):    
        option = None
        while option != "0":
            self.displayOptionMenuHelper()
            option = self.promptOptionMenu()  
            self.validateOptionMenu(option)

            if option == "1":
                self.displayBuildingPoolOptionMenu()

            elif option == "2":
                self.displayGridSizeMenu()

    # String display for game options menu
    def displayOptionMenuHelper(self):
        optionMenuContent = [
            "\nSimpCity Game Options",
            "---------------------",
            "1. Choose Building Pool",
            "2. Adjust Grid Size\n",
            "0. Return to Main Menu"
        ]

        print("\n".join(optionMenuContent))

    def promptOptionMenu(self):
        return input("Please enter an option: ")

    # Validate options made in game options menu
    def validateOptionMenu(self, option):   
        if option == '0':
            print('\n---- Back to Main Menu ----')
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("2"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

    # Function that facilitates the process of changing the game building pool
    def displayBuildingPoolOptionMenu(self):
        option = None
        while option != "0":
            self.displayBuildingPoolOptionMenuHelper()
            self.displayCurrentBuildingPool()
            option = self.promptBuildingPoolOptionMenu()
            self.validateBuildingPoolOptionMenu(option)

    # String display for building pool change menu
    def displayBuildingPoolOptionMenuHelper(self):
        buildingPoolOptionMenuContent = [
            "\nChoose Building Pool",
            "--------------------",
            "1. Beach",
            "2. Factory",
            "3. Highway",
            "4. House",
            "5. Shop",
            "6. Monument",
            "7. Park\n",
            "0. Return to Option Menu"
        ]

        print("\n".join(buildingPoolOptionMenuContent))

    def promptBuildingPoolOptionMenu(self):
        return input("\nEnter 5 building options with a comma separator (e.g. 1,2,4,6,7) or '0' to exit: ")

    # Validate options made in building pool menu
    def validateBuildingPoolOptionMenu(self, option):
        if option == '0':
            print('\n---- Back to Option Menu ----')
        elif self.isBuildingPoolOptionsValid(option):
            self.updateBuildingPoolFromOption(option)
            print("Sucessfully updated building pool!")
        else:
            print(f'Invalid option! {option} is not a valid building pool!')

    # Check validity of building pool options by player in building pool change menu
    def isBuildingPoolOptionsValid(self, option):
        # (e.g. 1,2,4,6,7)

        if len(option) != 9:
            return False

        choices = option.split(',')

        # Check Condition for valid input choices
        return len(set(choices)) == 5 and all(ord("1") <= ord(x) <= ord("7") for x in choices)

    # Calls grid's availableBuildings function for updating current building pool to selected options
    def updateBuildingPoolFromOption(self, option):
        self.grid.availableBuildings.updateBuildingPool(option)

    # Calls grid's availableBuildings function for displaying current building pool for active player
    def displayCurrentBuildingPool(self):
        self.grid.availableBuildings.displayCurrentBuildingPool()
    
    # Function that facilitates the process of changing the game grid size
    def displayGridSizeMenu(self):
        gridSize = None
        while gridSize != "0":
            self.displayGrid()
            gridSize = self.promptGridSize()
            self.validateGridSize(gridSize)

    def promptGridSize(self):
        return input("\nEnter a valid Grid Size (x,y) between 1-6 with a comma separator (e.g. 3,4) or '0' to exit: ")

    # Validate options made in grid size adjustment menu
    def validateGridSize(self, option):
        if option == '0':
            print('\n---- Back to Option Menu ----')
        elif self.isGridSizeValid(option):
            self.updateGridSize(option)
            gridSize = option.split(',')
            print(
                f"Sucessfully updated grid size to [{gridSize[0]} x {gridSize[1]}]!")
        else:
            print(f'Invalid Grid Size! {option} is not a valid grid size!')

    # Check validity of grid size input by player in grid size adjustment menu 
    def isGridSizeValid(self, gridSize):
        # (e.g. 4,4  6,6  3,3)

        if len(gridSize) != 3:
            return False

        size = gridSize.split(',')

        # Check condition for valid grid size choice
        return size[0].isnumeric() and size[1].isnumeric() and 1 < int(size[0]) <= 6 and 1 < int(size[1]) <= 6

    # Splits grid size input into values to be passed into updateGridSize function in grid object
    def updateGridSize(self, gridSize):
        size = gridSize.split(',')
        self.grid.updateGridSize(size[0], size[1])

    def retrieveGameMenuContent(self, firstBuilding, secondBuilding):
        gameMenuContent = [
            f"1. Build a {firstBuilding}",
            f"2. Build a {secondBuilding}",
            "3. See current score\n",
            "4. Save game",
            "0. Exit to main menu"
        ]

        return ("\n".join(gameMenuContent))

    def displayGameMenu(self, firstBuilding=None, secondBuilding=None):
        if firstBuilding is not None and secondBuilding is not None:
            self.firstBuilding, self.secondBuilding = firstBuilding, secondBuilding
        else:
            self.firstBuilding, self.secondBuilding = self.retrieveTwoRandomBuildings()

        print(self.retrieveGameMenuContent(
            self.firstBuilding, self.secondBuilding))

    def startNewGame(self):
        self.turns = 1
        self.savedGame = False
        self.initializeGrid()
        print('\n---- Entering Game Menu ----')

    # Prompt player for input in InGame main menu
    def promptGameMenu(self):
        return input('Please enter an input: ')

    # Validate options made in game menu
    def validateGame(self, option):
        if len(option) == 1 and ord("0") <= ord(option) <= ord("4"):
            if ord("1") <= ord(option) <= ord("2"):
                buildingValue = self.firstBuilding if \
                    ord(option) == ord("1") else self.secondBuilding
                positions = self.promptEnterBuildingPosition(buildingValue)
                self.validatePlaceBuildingOnPosition(buildingValue, positions)
            else:
                print(f"You selected option {option}\n")
        else:
            print("Invalid option!")

    def promptEnterBuildingPosition(self, building):
        return input(f"\nWhere would you like to place {building} at? ")

    def validatePlaceBuildingOnPosition(self, building, positions):
        if self.grid.isPositionValid(positions):
            x, y = self.grid.retrieveParsedPosition(positions)
            if self.turns == 1 or (self.turns > 1 and self.grid.hasAdjacentBuildingsForPosition(x, y)):
                print(f"Placing {building} at {positions}...")
                self.grid.updateGrid(x, y, building)
                self.grid.decreaseBuildingCount(building)
                self.turns += 1
                self.savedGame = False
                print(f"{building} has been successfully placed at {positions}.")
            else:
                print(f"Placing {building} at {positions} was unsuccessful.")
                print(f"{positions} is an invalid position! You must build next to an existing building.")

        else:
            print(f"{positions} is an invalid position! Please enter a valid building position!")

    def displayBuildingsScore(self):
        print()

        scores = self.retrieveBuildingsScore()

        print("\nTotal Score: " + str(scores))

    # Calculate total score for current game iteration
    def retrieveBuildingsScore(self, printBreakdown=True):
        scores, scoresBreakdown = self.grid.retrieveBuildingsScore()

        for buildingName, scoreBreakdown in scoresBreakdown.items():
            totalBuildingScore = sum(scoreBreakdown)
            if len(scoreBreakdown) > 0:
                breakdown = " + ".join(map(str, scoreBreakdown))
            else:
                breakdown = totalBuildingScore

            if printBreakdown:
                print(f"{buildingName}: {breakdown} = {totalBuildingScore}")

        return scores

    # Prompt player to check if they saved their game beforehand
    def promptSaveGame(self):
        return input('Game has not been saved yet. Would you like to save your progress? [Y/N]: ').upper()

    # Validate options for prompting save game.
    def validateSaveGame(self, option):
        if option.upper() == "Y":
            print('\nGame has been saved successfully.\n\n---- Back to Main Menu ---')

        elif option.upper() == "N":
            print("\n---- Back to Main Menu ----")

        else:
            print("Invalid Option. Returning to Game Menu...")

    # Validation message for successfully saving game in the game menu
    def savedGameSuccessful(self):
        print('Game has been saved successfully.\n\n---- Back to Game Menu----')

    # Access grid attribute to display grid
    def displayGrid(self, isFinal=False):
        if isFinal:
            print("\nFinal layout of Simp City:")

        self.grid.displayGrid()

    #Re-initialize the grid
    def initializeGrid(self):
        self.grid.initializeGrid()

    # Access grid attribute to
    def loadGame(self):
        self.grid.readGridFromFile()

    def saveGame(self):
        with open(savedGameFilename, 'w+') as f:
            gridValue = self.grid.parseGridAsString()
            for row in gridValue:
                f.writelines(row + "\n")
        self.savedGame = True

    def retrieveTwoRandomBuildings(self):
        return self.grid.retrieveTwoRandomBuildings()

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        exit(0)
