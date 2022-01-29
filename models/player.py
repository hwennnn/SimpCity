"""
This module deals with all player related functions.
"""
__docformat__ = "google"

from xmlrpc.client import boolean
from models.enums import Buildings
from models.grid import Grid
from models.configurations import *


class Player:
    turns: int
    """The turn number of the player"""
    grid: Grid
    """The Grid object related to the player"""
    firstBuilding: Buildings
    """The enum object for representing the first shuffled building value"""
    secondBuilding: Buildings
    """The enum object for representing the second shuffled building value"""
    savedGame: bool
    """The boolean condition for checking if the player saved their game"""

    def __init__(self):
        """
        Initialise the player object with default values for turns, grid, firstBuilding, secondBuilding and savedGame object.
        """
        self.turns = 1
        self.grid = Grid()
        self.firstBuilding = self.secondBuilding = None
        self.savedGame = False

    # Display first main menu upon launching python code
    def displayMainMenu(self):
        """
        This method will display the main menu options for the player to
        interact with the main menu.

        """
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
        """
        Returns:
            str: The main menu option input by the player

        """
        return input('Please enter an input: ')

    # Validate options made in main menu
    def validateMain(self, option):
        """
        Args:
            option (str): The main menu option input by the player

        This method will display valid strings based on the user's main menu input.

        """
        if option == '0':
            print('---- Game Ended ----')
            self.exitGame()
        # Check for validity of option
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("4"):
            print(f"You selected option {option}")
        else:
            print(f'{option} is an invalid option!')

    def displayOptionMenu(self):
        """
        This method facilitates the process of the player's actions when they enter the Game Options Menu.

        """
        option = None
        while option != "0":
            # Always displays option menu if player does not exit by entering "0"
            self.displayOptionMenuHelper()
            option = self.promptOptionMenu()  
            self.validateOptionMenu(option)

            if option == "1":
                # Enter Change Building Pool Menu
                self.displayBuildingPoolOptionMenu()

            elif option == "2":
                self.displayGridSizeMenu()

    # String display for game options menu
    def displayOptionMenuHelper(self):
        """
        This method will display the game options menu for the player to interact with the game option menu.

        """
        optionMenuContent = [
            "\nSimpCity Game Options",
            "---------------------",
            "1. Choose Building Pool",
            "2. Adjust Grid Size\n",
            "0. Return to Main Menu"
        ]

        print("\n".join(optionMenuContent))

    def promptOptionMenu(self):
        """
        Returns:
            str: The game option menu choice input by the player

        This method will return the player's menu choice input as a string object.

        """
        return input("Please enter an option: ")

    # Validate options made in main menu
    def validateOptionMenu(self, option):
        """
        Args:
            option (str): The game menu option input by the player

        This method will display valid strings based on the user's option menu input.

        """
        if option == '0':
            print('\n---- Back to Main Menu ----')
        # Check for validity of option
        elif len(option) == 1 and ord("1") <= ord(option) <= ord("2"):
            print(f"You selected option {option}")
        else:
            print(f'{option} is an invalid option!')

    # Function that facilitates the process of changing the game building pool
    def displayBuildingPoolOptionMenu(self):
        """
        This method facilitates the process of the player's actions when they enter the Building Pool Options Menu.

        """
        option = None
        while option != "9" and option != "0":
            # Always display building pool change menu if player does not exit by entering "0"
            self.displayBuildingPoolOptionMenuHelper()
            self.displayCurrentBuildingPool()
            option = self.promptBuildingPoolOptionMenu()
            self.validateBuildingPoolOptionMenu(option)

    # String display for building pool change menu
    def displayBuildingPoolOptionMenuHelper(self):
        """
        This method will display the building pool options for the player to
        interact with the change building pool menu.

        """
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
        """
        Returns:
            str: The building pool choice input by the player

        This method will return the player's building pool choices input as a string object.

        """
        return input("\nEnter 5 building options with a comma separator (e.g. 1,2,4,6,7) or '0' to exit: ")

    # Validate options made in building pool menu
    def validateBuildingPoolOptionMenu(self, option):
        """
        Args:
            option (str): The building pool choice input by the player

        The method will display valid strings based on the user's building pool menu input.
        If the player enters a valid building pool option, the method will update the current building pool
        based on the user's input.

        """
        if option == '0':
            print('\n---- Back to Option Menu ----')
        elif self.isBuildingPoolOptionsValid(option):
            self.updateBuildingPoolFromOption(option)
            print("Sucessfully updated building pool!")
        else:
            print(f'Invalid option! {option} is not a valid building pool!')

    # Check validity of building pool options by player in building pool change menu
    def isBuildingPoolOptionsValid(self, option):
        """
        Args:
            option (str): The building pool choice input by the player. \n
            Example -> 1,2,3,5,7

        Returns:
            bool: The result whether the building pool is valid.

        This method will return whether the userInput is a valid building pool selection for gameplay
        by checking whether the input lengths are of the correct size and the options are within the number of building types available.

        """
        if len(option) != 9:
            return False

        choices = option.split(',')

        # Check Condition for valid input choices
        return len(set(choices)) == 5 and all(ord("1") <= ord(x) <= ord("7") for x in choices)

    # Calls grid's availableBuildings function for updating current building pool to selected options
    def updateBuildingPoolFromOption(self, option):
        """
        Args:
            option (str): The building pool choice input by the player. \n
            Example -> 1,2,3,5,7

        This method will call the function in the available buildings object that changes the
        current building pool for the current player.

        """
        self.grid.availableBuildings.updateBuildingPool(option)

    # Calls grid's availableBuildings function for displaying current building pool for active player
    def displayCurrentBuildingPool(self):
        """
        Args:
            option (str): The building pool choice input by the player. \n
            Example -> 1,2,3,5,7

        This method will call the function in the available buildings object that changes the
        current building pool for the current player.

        """
        self.grid.availableBuildings.displayCurrentBuildingPool()
    
    # Function that facilitates the process of changing the game grid size
    def displayGridSizeMenu(self):
        gridSize = None
        while gridSize != "0":
            self.displayGrid()
            gridSize = self.promptGridSize()
            self.validateGridSize(gridSize)

    def promptGridSize(self):
        """
        Returns:
            str: The grid size menu input by the player

        This method will return the player's grid size menu input as a string object.

        """
        return input("\nEnter a valid Grid Size (x,y) between 1-6 with a comma separator (e.g. 3,4) or '0' to exit: ")

    # Validate options made in grid size adjustment menu
    def validateGridSize(self, option):
        """
        Args:
            option (str): The grid size menu input by the player.

        The method will display valid strings based on the user's grid size menu input.
        If the player enters a valid grid size, the method will update the current grid size
        based on the user's input.

        """
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
        """
        Args:
            gridSize (str): The grid size menu input by the player. \n
            Example -> 2,2

        Returns:
            bool: The result whether the grid size is valid.

        This method will return whether the userInput is a valid grid size for gameplay
        by checking whether the input lengths are of the correct size and the options are within the eligible row and column sizes.

        """
        if len(gridSize) != 3:
            return False

        size = gridSize.split(',')

        # Check condition for valid grid size choice
        return size[0].isnumeric() and size[1].isnumeric() and 1 < int(size[0]) <= 6 and 1 < int(size[1]) <= 6

    # Splits grid size input into values to be passed into updateGridSize function in grid object
    def updateGridSize(self, gridSize):
        """
        Args:
            gridSize (str): The grid size menu input by the player. \n
            Example -> 2,2

        This method will call the function in the grid object that changes the grid size to the grid input from the player

        """
        size = gridSize.split(',')
        self.grid.updateGridSize(size[0], size[1])

    def retrieveGameMenuContent(self, firstBuilding, secondBuilding):
        """
        Args:
            firstBuilding (Buildings): The first building obtained from the retrieve random buildings method. \n
            secondBuilding (Buildings): The second building obtained from the retrieve random buildings method. \n
            Example -> HSE or MON or HWY

        Returns:
            str: The game menu content in a new line to avoid cluttering of game information

        This method will return the game menu options as a string for displaying in the displayGameMenu() method

        """
        gameMenuContent = [
            f"1. Build a {firstBuilding}",
            f"2. Build a {secondBuilding}",
            "3. See current score\n",
            "4. Save game",
            "0. Exit to main menu"
        ]

        return ("\n".join(gameMenuContent))

    def displayGameMenu(self, firstBuilding=None, secondBuilding=None):
        """
        Args:
            firstBuilding (Buildings): The first building attribute to be set as a random building. \n
            secondBuilding (Buildings): The second building attribute to be set as a random building. \n
            Example -> HSE or MON or HWY

        This method displays the In-Game menu for the player during the game session.

        """
        if firstBuilding is not None and secondBuilding is not None:
            self.firstBuilding, self.secondBuilding = firstBuilding, secondBuilding
        else:
            self.firstBuilding, self.secondBuilding = self.retrieveTwoRandomBuildings()

        print(self.retrieveGameMenuContent(
            self.firstBuilding, self.secondBuilding))

    def startNewGame(self):
        """
        This method resets the player's attributes when they start a new game in the main menu

        """
        self.turns = 1
        self.savedGame = False
        self.initializeGrid()
        print('\n---- Entering Game Menu ----')

    # Prompt player for input in InGame main menu
    def promptGameMenu(self):
        """
        Returns:
            str: The game menu option input by the player

        This method will return the player's game menu option input as a string object.

        """
        return input('Please enter an input: ')

    # Validate options made in game menu
    def validateGame(self, option):
        """
        Args:
            option (str): The game menu option input by the player.

        The method will display valid strings based on the user's game option menu input.
        If the player chooses to place either the first or second building, they will be prompted with a building position input.

        """
        if len(option) == 1 and ord("0") <= ord(option) <= ord("4"):
            if ord("1") <= ord(option) <= ord("2"):
                buildingValue = self.firstBuilding if \
                    ord(option) == ord("1") else self.secondBuilding
                positions = self.promptEnterBuildingPosition(buildingValue)
                self.validatePlaceBuildingOnPosition(buildingValue, positions)
            else:
                print(f"You selected option {option}\n")
        else:
            print(f"{option} is an invalid option!")

    def promptEnterBuildingPosition(self, building):
        """
        Args:
            building (Buildings): The building object the player chooses to place.

        The method will prompt the user for a valid position and update the grid
        with the player's building of choice on the position input if the position input is valid.

        """
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
        """
        This method displays the score accumulation for the current state of the grid object.
        It calls the method for displaying the score breakdown while retrieving the total score and printing it.

        """
        print()

        scores = self.retrieveBuildingsScore()

        print("\nTotal Score: " + str(scores))

    # Calculate total score for current game iteration
    def retrieveBuildingsScore(self, printBreakdown=True):
        """
        Args:
            printBreakdown (bool): The Boolean value for determining if the score breakdown should be displayed.

        Returns:
            int: The total score of the current grid object

        This method will retrieve the total score and score breakdown from the grid method retrieveBuildingsScore().
        The method will print each line of the score breakdown and return the total score.

        """
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
        """
        Returns:
            str: The input that determines if the player has saved their game or not

        This method will prompt the user for whether they have saved their game yet and return the input as a string

        """
        return input('Game has not been saved yet. Would you like to save your progress? [Y/N]: ').upper()

    # Validate options for prompting save game.
    def validateSaveGame(self, option):
        """
        Args:
            option (str): The [Y/N] option input by the player.

        This method will display valid strings based on the user's saved game menu input.
        The method is called when the player chooses to exit the game without saving the game.

        """
        if option.upper() == "Y":
            print('\nGame has been saved successfully.\n\n---- Back to Main Menu ---')

        elif option.upper() == "N":
            print("\n---- Back to Main Menu ----")

        else:
            print("Invalid Option. Returning to Game Menu...")

    # Validation message for successfully saving game in the game menu
    def savedGameSuccessful(self):
        """
        This method displays a saved game successfully message if the player chooses the Save Game option in the game menu.

        """
        print('\nGame has been saved successfully.\n\n---- Back to Game Menu----')

    # Access grid attribute to display grid
    def displayGrid(self, isFinal=False):
        """
        Args:
            isFinal (bool): The boolean to check if it is the Final Turn for the active player.

        This method will call the Grid function for displaying the grid object.
        If it is the final turn for the player, the additioanl tag "Final layout of SimpCity:" will be added with the grid display

        """
        if isFinal:
            print("\nFinal layout of Simp City:")

        self.grid.displayGrid()

    #Re-initialize the grid
    def initializeGrid(self):
        self.grid.initializeGrid()

    def loadGame(self):
        """
        This method will call the Grid function for loading a grid object from a text file.

        """
        self.grid.readGridFromFile()

    # writing row,col of grid , saved building pool and grid state to file
    def saveGame(self):
        """
        This method will call the Grid function for parsing the grid as a string and writing it into a text file.
        The method will set the player attribute savedGame to True for validation In-Game.

        """
        with open(savedGameFilename, 'w+') as f:
            f.write("(" + str(self.grid.rowCount) + "," + str(self.grid.colCount) + ")"+ "\n")
            f.write("#" + self.grid.availableBuildings.exportBuildings() + "\n")
            gridValue = self.grid.parseGridAsString()
            for row in gridValue:
                f.writelines(row + "\n")
        self.savedGame = True

    def retrieveTwoRandomBuildings(self):
        """
        Returns:
            firstBuilding (Buildings): The first building attribute to be set as a random building. \n
            secondBuilding (Buildings): The second building attribute to be set as a random building. \n
            Example -> HSE or MON or HWY

        This method will call the Grid object function for retrieving two random building values from the current buildings pool
        and returning it as 2 separate variables.
        """
        return self.grid.retrieveTwoRandomBuildings()

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        exit(0)
