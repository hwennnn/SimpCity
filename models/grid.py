"""
This module deals with all grid related functions.
"""
__docformat__ = "google"

from models.available_buildings import AvailableBuildings
from models.buildings import *
from models.enums import Buildings
from models.configurations import *
import os 


class Grid:
    rowCount: int
    """The row count of the grid"""
    colCount: int
    """The column count of the grid"""
    grid: list[list[str]]
    """The 2D array (row * grid) represents the grid. Initially each position in the grid is initialised as None"""
    factoryList: list[Factory]
    """The array keeps track of placed Factory building in the grid"""
    availableBuildings: AvailableBuildings
    """The available buildings object associated with the grid"""

    def __init__(self):
        """
        Initialise the grid object with default values for rowCount, columnCount, grid, factoryList and availableBuildings object.
        """
        self.rowCount = self.colCount = 4
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.factoryList = []
        self.availableBuildings = AvailableBuildings()

    def isPositionXValid(self, x):
        """
        Args:
            x (str): The building position on x-axis of the grid entered by the user.

        The method will validate whether the input is valid as the length is 1 and its within the boundary.

        """
        return len(x) == 1 and ord('A') <= ord(x.upper()) <= ord('A') + (self.colCount - 1)

    def isPositionYValid(self, y):
        """
        Args:
            y (str): The building position on y-axis of the grid entered by the user.

        The method will validate whether the input is valid as the length is 1 and its within the boundary.

        """
        return len(y) == 1 and y.isnumeric() and 1 <= int(y) <= self.rowCount

    def parseXPositionInput(self, x):
        """
        Args:
            x (str): The building position on x-axis of the grid entered by the user.

        Returns:
            int: The 0-indexed position integer represents the position on x-axis in the grid.

        The method will return the 0-indexed x position integer.

        """
        return ord(x.upper()) - ord('A')

    def parseYPositionInput(self, y):
        """
        Args:
            y (str): The building position on y-axis of the grid entered by the user.

        Returns:
            int: The 0-indexed position integer represents the position on y-axis in the grid.

        The method will return the 0-indexed y position integer.

        """
        return int(y) - 1

    def isPositionValid(self, userInput):
        """
        Args:
            userInput (str): The building position on the grid entered by the user. \n
            Example -> a1

        Returns:
            bool: The result whether the position is valid.

        The method will return whether the userInput is valid to be placed on the grid
        by checking whether the x and y axis are within boundary and that particular position is not occupied yet.

        """

        if len(userInput) != 2:
            return False

        x, y = userInput

        return self.isPositionXValid(x) and self.isPositionYValid(y) \
            and self.grid[self.parseYPositionInput(y)][self.parseXPositionInput(x)] is None

    def retrieveParsedPosition(self, userInput):
        """
        Args:
            userInput (str): The building position on the grid entered by the user. \n
            Example -> a1

        Returns:
            tuple(int): Return a tuple of integer values.

        The method will return the parsed positions from raw user inputs.
        For example, "a1" will become (0, 0).

        """
        x, y = userInput

        return (self.parseYPositionInput(y), self.parseXPositionInput(x))

    def hasAdjacentBuildingsForPosition(self, x, y):
        """
        Args:
            x (int): The building position on x-axis of the grid
            y (int): The building position on y-axis of the grid

        Returns:
            bool: The result whether the position has adjacent buildings.

        The method will return whether there is any adjacent buildings on its left, right, upper and down position.

        """

        adjacentPositions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for dx, dy in adjacentPositions:
            if 0 <= dx < self.rowCount and 0 <= dy < self.colCount and self.hasBuildingOnPosition(dx, dy):
                return True

        return False

    def hasBuildingOnPosition(self, x, y):
        """
        Args:
            x (int): The building position on x-axis of the grid
            y (int): The building position on y-axis of the grid

        Returns:
            bool: The result whether the position has any building

        The method will return whether there is any building on the position.

        """
        return self.grid[x][y] is not None

    def updateGrid(self, x, y, buildingName):
        """
        Args:
            x (int): The building position on x-axis of the grid
            y (int): The building position on y-axis of the grid
            buildingName (str): The name of the building going to be placed on the given position

        The method will place the building object associated with the buildingName in the given position.

        """

        # convert the user input to 0-indexed for array processing
        self.grid[x][y] = self.createBuilding(buildingName, x, y)

    def updateGridSize(self, x, y):
        """
        Args:
            x (int): The building position on x-axis of the grid entered by the user
            y (int): The building position on y-axis of the grid entered by the user

        The method will update rowCount and colCount accordingly based on the given user options.
        It will also call another method re-initialise the grid.

        """

        self.rowCount = int(x)
        self.colCount = int(y)
        self.initializeGrid()

    def createBuilding(self, buildingName, x, y):
        """
        Args:
            buildingName (str): The name of the building going to be placed on the given position
            x (int): The building position on x-axis of the grid
            y (int): The building position on y-axis of the grid

        Returns:
            Object: The created building object

        The method will return the created building object associated with the buildingName.

        """

        match buildingName:
            case Buildings.BEACH.value:
                return Beach(buildingName, x, y)

            case Buildings.FACTORY.value:
                factoryObject = Factory(buildingName, x, y)
                self.factoryList.append(factoryObject)
                return factoryObject

            case Buildings.HOUSE.value:
                return House(buildingName, x, y)

            case Buildings.SHOP.value:
                return Shop(buildingName, x, y)

            case Buildings.HIGHWAY.value:
                return Highway(buildingName, x, y)

            case Buildings.MONUMENT.value:
                return Monument(buildingName, x, y)

            case Buildings.PARK.value:
                return Park(buildingName, x, y)

    def decreaseBuildingCount(self, buildingName):
        """
        Args:
            buildingName (str): The name of the building

        The method will call the AvailableBuildings object method to decrease the available building count.

        """
        self.availableBuildings.decreaseAvailableBuilding(buildingName)

    def retrieveBuildingsScore(self):
        """
        Returns:
            tuple(int, map[int]): (The total buildings score of the player, The score breakdown for each type of building)

        The method will return the calculated total buildings score of the player in each position of the grid. \n
        There are two exceptions during the loop calculation, which are Factory and Park buildings, because they would only be calculated once at the start of the algorithm. \n

        """

        scoresBreakdown = {}

        for buildingName in self.availableBuildings.buildings:
            scoresBreakdown[buildingName] = []

        scores = 0
        # Declare exceptions for Park and Factory calculation
        exceptionList = [Buildings.PARK.value, Buildings.FACTORY.value]

        # calculate Factory Building Score
        if Buildings.FACTORY.value in self.availableBuildings.buildings:
            factoryScore, factoryScoreBreakdown = self.calculateFactoryBuildingsScore()
            scoresBreakdown[Buildings.FACTORY.value] = factoryScoreBreakdown
            scores += factoryScore

        # calculate Park Building Score
        if Buildings.PARK.value in self.availableBuildings.buildings:
            parkScore, parkScoreBreakdown = self.calculateParkBuildingsScore()
            scoresBreakdown[Buildings.PARK.value] = parkScoreBreakdown
            scores += parkScore

        for x in range(self.rowCount):
            for y in range(self.colCount):
                if self.grid[x][y] is not None and self.grid[x][y].getName() not in exceptionList:
                    buildingScore = self.grid[x][y].retrieveBuildingScore(
                        self.grid)
                    scoresBreakdown[self.grid[x]
                                    [y].getName()].append(buildingScore)
                    scores += buildingScore

        return (scores, scoresBreakdown)

    def calculateFactoryBuildingsScore(self):
        """
        Returns:
            tuple(int, map[int]): (The total Factory buildings score of the player, The score breakdown for the Factory Building)

        The method will return the calculated total Factory buildings score of the player in each position of the grid. \n

        A Factory (FAC) scores 1 point per factory (FAC) in the city, up to a maximum of 4
        points for the first 4 factories; all subsequent factories only score 1 point each. \n
        For example,
        - If there are 3 factories in the city, each factory will score 3 points, for a total
        of 3+3+3 = 9 points. \n
        - If there are 5 factories in the city, the first 4 factories will score 4 points each
        while the 5 th factory will score 1 point, for a total of 4+4+4+4+1 = 17 points.

        """

        scoreBreakdown = []
        result = 0

        # Determine length of facotryList for scoring
        factoryScore = len(self.factoryList) if len(
            self.factoryList) < 5 else 1

        # Loop through grid object and determine scoring
        for x in range(self.rowCount):
            for y in range(self.colCount):
                # Check building type
                if self.grid[x][y] is not None and self.grid[x][y].getName() == Buildings.FACTORY.value:

                    # Declare separate calculations for factoryList < 5 and factoryList >= 5
                    if len(self.factoryList) < 5:
                        scoreBreakdown.append(factoryScore)
                        result += factoryScore

                    if len(self.factoryList) >= 5:
                        score = (factoryScore * 4) if self.factoryList.index(
                            self.grid[x][y]) < 4 else factoryScore
                        scoreBreakdown.append(score)
                        result += score

        return (result, scoreBreakdown)

    def calculateParkBuildingsScore(self):
        """
        Returns:
            tuple(int, map[int]): (The total Park buildings score of the player, The score breakdown for the Park Building)

        The method will return the calculated total Park buildings score of the player in each position of the grid. \n

        A Park is a new type of building depending on how many
        parks are connected to each other (both horizontally and vertically). The
        score for a Park is given by the following table: \n

        scoresMap = {1: 1, 2: 3, 3: 8, 4: 16, 5: 22, 6: 23, 7: 24, 8: 25} \n
        Note that the score given above is for the entire Park, not for each Park
        building, so a 4-square Park scores 16 in total, not 16 per building.
        """

        scoreBreakdown = []
        result = 0

        # first init a 2D array to keep track of the visited buildings on (x, y) position
        visited = [[False] * self.colCount for _ in range(self.rowCount)]
        scoresMap = {1: 1, 2: 3, 3: 8, 4: 16, 5: 22, 6: 23, 7: 24, 8: 25}

        # A depth-first-search helper function to help explore its neighbours which are the Park buildings
        def dfs(x, y):
            # Return 0 as the current position has already been visited
            if visited[x][y]:
                return 0

            # mark the current position as visited so it will ensure each position wil only be visited once
            visited[x][y] = True
            # initialise the park building count as 1
            count = 1

            # explore 4 directions from the current position and conduct a depth-first-search from that position
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < self.rowCount and 0 <= dy < self.colCount and self.grid[dx][dy] is not None and self.grid[dx][dy].getName() == Buildings.PARK.value:
                    count += dfs(dx, dy)

            return count

        # search through all Park buildings and conduct a depth-first-search to retrieve the Park Building Size
        for x in range(self.rowCount):
            for y in range(self.colCount):
                if self.grid[x][y] is not None and self.grid[x][y].getName() == Buildings.PARK.value and not visited[x][y]:
                    parkSize = dfs(x, y)
                    score = scoresMap[parkSize]
                    scoreBreakdown.append(score)
                    result += score

        return (result, scoreBreakdown)

    def retrieveTwoRandomBuildings(self):
        """
        Returns:
            list[str]: The first two element of the shuffled buildings

        This method will return the first two element of the shuffled buildings.
        Logically the length of the shuffled buildings should be always greater than two.

        """

        return self.availableBuildings.retriveTwoRandomBuildings()

    def displayGrid(self):
        """
        This method will display the grid and adapts to each building type.

        The method will loop through each grid cell and retrieve the object stored within it.
        If there is a building in the cell and it matches a building name, the building name will be added to the row.
        If there is no building in the cell, an empty cell will be displayed
        Depending on the grid size, the Remaining Buildings Tab on the Right will be displayed accordingly
        E.g.:If grid size only has a row count of 2, the last Remaining Building Line will be printed as a separate
             line on its own. Otherwise, it will be concatenated beside the next row line.
        Displaying the Remaining Buildings Tab stops when row count has reached more than 2
        """

        columnIndication = "\n   "
        upperGridline = " +"

        for y in range(self.colCount):
            columnIndication += "  "+chr(65 + y)+"   "
            upperGridline += "-----+"

        columnIndication += "\t Remaining Buildings\n"
        upperGridline += "\t -------------------"
        print(columnIndication, upperGridline)

        for x in range(self.rowCount):
            lastRemainingBuilding = ""
            row = str(x + 1) + " |"
            lowerGridline = "  +"
            for building in self.grid[x]:
                if building is None:
                    row += "     |"
                else:
                    match building.getName():
                        case Buildings.BEACH.value:
                            row += " " + Buildings.BEACH.value + " |"
                        case Buildings.FACTORY.value:
                            row += " " + Buildings.FACTORY.value + " |"
                        case Buildings.HIGHWAY.value:
                            row += " " + Buildings.HIGHWAY.value + " |"
                        case Buildings.HOUSE.value:
                            row += " " + Buildings.HOUSE.value + " |"
                        case Buildings.SHOP.value:
                            row += " " + Buildings.SHOP.value + " |"
                        case Buildings.MONUMENT.value:
                            row += " " + Buildings.MONUMENT.value + " |"
                        case Buildings.PARK.value:
                            row += " " + Buildings.PARK.value + " |"

                lowerGridline += "-----+"

            # Checking Grid Size for displaying Remaining Buildings Tab
            if self.rowCount <= 2:
                # Add Remaining Buildings from Building Pool Availability to the Right Side of the grid row and grid line
                row += f"\t {self.availableBuildings.buildings[x * 2]}: {self.availableBuildings.availability[x * 2]}"
                lowerGridline += f"\t {self.availableBuildings.buildings[x * 2 + 1]}: {self.availableBuildings.availability[x * 2 + 1]}"

                # Fixed remaining building display for last building type
                if self.colCount == 6:
                    lastRemainingBuilding = f"\t\t\t\t\t {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}\n"

                # Adds a \t based on how wide grid is to allow for proper string display.
                else:
                    for y in range(self.colCount):
                        lastRemainingBuilding += "\t"
                    lastRemainingBuilding += f" {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}\n"

                print(row)
                print(lowerGridline)

                if x == 1:
                    print(lastRemainingBuilding)

            else:
                # If Grid Row Count > 2, all Remaining Buildings Strings can be added to the end of the Grid Rows and Grid Lines
                row += f"\t {self.availableBuildings.buildings[x * 2]}: {self.availableBuildings.availability[x * 2]}" \
                    if x < 2 else ""
                # Adds last Remaining Building line.
                row += f"\t {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}" \
                    if x == 2 else ""
                lowerGridline += f"\t {self.availableBuildings.buildings[x * 2 + 1]}: {self.availableBuildings.availability[x * 2 + 1]}" \
                    if x < 2 else "\n" if x == self.rowCount - 1 else ""

                print(row)
                print(lowerGridline)

    def parseGridAsString(self):
        """
        Returns:
            list[str]: The list of parsed string.

        This method will parse the grid as an array of string, allowing it to be written into txt file
        """

        returnStrArr = []
        for row in self.grid:
            rowStr = []
            for v in row:
                rowStr.append("None" if v is None else v.name)
            returnStrArr.append(",".join(rowStr))
        return returnStrArr

    def initializeGrid(self):
        """
        This method will reset the grid, the available building count and the factory list.
        """

        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.availableBuildings.availability = [8] * 5
        self.factoryList.clear()

    # checks if save game file exists
    def isSavedGameExist(self):
        """
        This method will check if there is a saved game file in the current directory.
        """

        return os.path.exists(savedGameFilename)

    def formatGrid(self, gridstr):
        """
        Parameters:
            list[str] : The grid as a string read in from a file.

        Returns:
            list[list[building obj]]: The grid as a list of list of building objects.

        This method will format the grid string into a grid object. 
        It takes in the building names as strings and parse it as an object.
        """ 

        grid = []
        for row in range(len(gridstr)):
            rowArr = gridstr[row]
            for i in range(len(rowArr)):
                if rowArr[i] == "None":
                    rowArr[i] = None
                else:
                    rowArr[i] = self.createBuilding(rowArr[i], row, i)
            grid.append(rowArr)
        return grid

    # serialising from file to grid object
    def readGridFromFile(self):
        """
        Returns:
            isSavedFilevalid (Bool): True if the file is valid, False otherwise.
            player turns (int): The number of turns the player has played otherwise it will be none if the file is invalid.
            

        This method will read the saved game file and set the grid , row and col, building pool after checking the validity of the saved game file.
        """

        if not self.isSavedGameExist():
            return (False, None) 

        lines = self.readFiles()

        isFileValid, results = self.isSavedGameFileValid(lines)        
        if isFileValid:
            self.rowCount = results["row"]
            self.colCount = results["col"]
            self.availableBuildings.updateBuildingPool(results["buildings"])
            formattedGrid = self.formatGrid(results["grid"])
            self.grid = formattedGrid
            # update buildings if grid contains buildings
            if len(results["buildingList"]) > 0:
                self.availableBuildings.updateAvailableBuildings(results["buildingList"])
            print('Successfully loaded the game!')
            return (True, results["turns"])
        else: 
            print('Saved game file not found')
            return (False, None)

    def isSavedGameFileValid(self, lines):
        """
        Parameters:
            list[str] : The lines of the saved game file. 

        Returns:
            isSavedFilevalid (Bool): True if the file is valid, False otherwise.
            results (dict): A dictionary to store the needed information extracted from the saved game file

        This method will check each line of file, and extract the needed information to be stored in the results dictionary.
        It will check if the file is valid , check if the turns are within the range of the game, check if the len of buildings is 5 and check if the grid is valid.

        """

        results = {} # set dict to store results

        # check if saved game file has (row,col), building pool, turns and grid 
        if len(lines) < 4:
            return (False, None)
        
        turns = int(lines.pop(0).lstrip("*").rstrip("\n"))
        if turns > 18:
            return (False, None)

        results["turns"] = int(turns)

        row,col = map(int,lines.pop(0).lstrip("(").rstrip(")\n").split(","))
        if row < 1 and col < 1: 
            return (False, None)

        results["row"] = row
        results["col"] = col
        
        # load buildings into builings
        buildings = lines.pop(0).lstrip("#").rstrip("\n")
        if len(buildings.split(",")) != 5:
            return (False, None)

        results["buildings"] = buildings

        if len(lines) != row:
            return (False, None)
        
        validBuildings = set(['None', 'BCH', 'FAC', 'HSE', 'SHP', 'HWY', 'MON', 'PRK'])
        gridStr = []
        buildingList = []
        
        for line in lines:
            line = line.strip("\n").split(',')
            if len(line) != col:
                return (False, None)

            for building in line:
                if building not in validBuildings:
                    # raise Exception("Invalid building found in saved game file")
                    return (False, None)
                if building != "None": 
                    buildingList.append(building)
            gridStr.append(line)
        
        results["grid"] = gridStr
        results["buildingList"] = buildingList

        return (True, results)

    def readFiles(self):
        """
         Returns:
            isSavedFilevalid (Bool): True if the file is valid, False otherwise.
            results (dict): A dictionary to store the needed information extracted from the saved game file

        This method will check each line of file, and extract the needed information to be stored in the results dictionary.
        It will check if the file is valid , check if the turns are within the range of the game, check if the len of buildings is 5 and check if the grid is valid.

        """
        
        lines = None
        with open(savedGameFilename, "r+") as file:
            lines = file.readlines()

        return lines
