from models.grid import Grid
from models.configurations import *


class Player:  # Player Class
    def __init__(self):
        self.score = 0
        self.turns = 1
        self.grid = Grid()
        self.firstBuilding = self.secondBuilding = None
        self.savedGame = False

    # Display first main menu upon launching python code
    def displayMainMenu(self):

        print("""
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game
3. Options

0. Exit
""")

    # Prompt player for input in first main menu
    def promptMainMenu(self):
        return input('Please enter an input: ')

    # Validate options made in main menu
    def validateMain(self, option):
        if option == '0':
            print('---- Game Ended ----')
            self.exitGame()
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("3"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

    def displayOptionMenu(self):
        option = None
        while option != "0":
            self.displayOptionMenuHelper()
            option = self.promptOptionMenu()
            self.validateOptionMenu(option)

            if option == "1":
                self.displayBuildingPoolOptionMenu()

    def displayOptionMenuHelper(self):
        print("""
SimpCity Game Options
---------------------
1. Choose Building Pool

0. Return to Main Menu
""")

    def promptOptionMenu(self):
        return input("Please enter an option: ")

    # Validate options made in main menu
    def validateOptionMenu(self, option):
        if option == '0':
            print('\n---- Back to Main Menu ----')
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("1"):
            print(f"You selected option {option}")
        else:
            print('Invalid option!')

    def displayBuildingPoolOptionMenu(self):
        option = None
        while option != "9" and option != "0":
            self.displayBuildingPoolOptionMenuHelper()
            self.displayCurrentBuildingPool()
            option = self.promptBuildingPoolOptionMenu()
            self.validateBuildingPoolOptionMenu(option)

    def displayBuildingPoolOptionMenuHelper(self):
        print("""
Choose Building Pool
--------------------
1. Beach
2. Factory
3. Highway
4. House
5. Shop
6. Monument
7. Park 

0. Return to Option Menu
""")

    def promptBuildingPoolOptionMenu(self):
        return input("Enter 5 building options with a comma separator (e.g. 1,2,4,6,7) or '0' to exit: ")

    # Validate options made in main menu
    def validateBuildingPoolOptionMenu(self, option):
        if option == '0':
            print('\n---- Back to Option Menu ----')
        elif self.isBuildingPoolOptionsValid(option):
            self.updateBuildingPoolFromOption(option)
            print("Sucessfully updated building pool!")
        else:
            print('Invalid option!')

    def isBuildingPoolOptionsValid(self, option):
        # (e.g. 1,2,4,6,7)

        if len(option) != 9:
            return False

        choices = option.split(',')

        return len(set(choices)) == 5 and all(ord("1") <= ord(x) <= ord("7") for x in choices)

    def updateBuildingPoolFromOption(self, option):
        self.grid.availableBuildings.updateBuildingPool(option)

    def displayCurrentBuildingPool(self):
        self.grid.availableBuildings.displayCurrentBuildingPool()

    def gameMenuContent(self, firstBuilding, secondBuilding):
        return (
            f"""
1. Build a {firstBuilding}
2. Build a {secondBuilding}
3. See current score

4. Save game
0. Exit to main menu""")

    def displayGameMenu(self, firstBuilding=None, secondBuilding=None):
        if firstBuilding is not None and secondBuilding is not None:
            self.firstBuilding, self.secondBuilding = firstBuilding, secondBuilding
        else:
            self.firstBuilding, self.secondBuilding = self.retrieveTwoRandomBuildings()

        print(self.gameMenuContent(self.firstBuilding, self.secondBuilding))

    def startNewGame(self):
        self.turns = 1
        self.savedGame = False
        self.grid.initializeGrid()
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
                self.promptEnterBuildingPosition(buildingValue)
            else:
                print(f"You selected option {option}")
        else:
            print("Invalid option!")

    def promptEnterBuildingPosition(self, building):
        positions = input("Build where? ")

        if self.grid.isPositionValid(positions):
            x, y = self.grid.retrieveParsedPosition(positions)
            if self.turns == 1 or (self.turns > 1 and self.grid.hasAdjacentBuildingsForPosition(x, y)):
                self.grid.updateGrid(x, y, building)
                self.grid.decreaseBuildingCount(building)
                self.turns += 1
                self.savedGame = False
            else:
                print("You must build next to an existing building.")

        else:
            print("Please enter a valid building position!")

    # Calculate total score for current game iteration
    def retrieveBuildingsScore(self):
        scores, scoresBreakdown = self.grid.retrieveBuildingsScore()

        for buildingName, scoreBreakdown in scoresBreakdown.items():
            totalBuildingScore = sum(scoreBreakdown)
            if len(scoreBreakdown) > 0:
                breakdown = " + ".join(map(str, scoreBreakdown))
            else:
                breakdown = totalBuildingScore
            print(f"{buildingName}: {breakdown} = {totalBuildingScore}")

        print("\nTotal Score: " + str(scores))

    # Prompt player to check if they saved their game beforehand
    def promptSaveGame(self):
        return input('\nGame has not been saved yet. Would you like to save your progress? [Y/N]: ').upper()

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
        print('\nGame has been saved successfully.\n\n---- Back to Game Menu----')

    # Access grid attribute to display grid
    def displayGrid(self):
        self.grid.displayGrid()

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

    def displayAvailableBuildings(self):
        self.grid.displayAvailableBuildings()

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        exit(0)
