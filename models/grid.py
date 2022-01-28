from models.available_buildings import AvailableBuildings
from models.buildings import *
from models.enums import Buildings
from models.configurations import *
import os 


class Grid:  # Grid Class
    def __init__(self):
        self.rowCount = self.colCount = 4
        # First initialise the object in each position as None
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.factoryList = []
        self.availableBuildings = AvailableBuildings()

    def isPositionXValid(self, x):
        return len(x) == 1 and ord('A') <= ord(x.upper()) <= ord('A') + (self.colCount - 1)

    def isPositionYValid(self, y):
        return len(y) == 1 and y.isnumeric() and 1 <= int(y) <= self.rowCount

    def parseXPositionInput(self, x):
        return ord(x.upper()) - ord('A')

    def parseYPositionInput(self, y):
        return int(y) - 1

    def isPositionValid(self, userInput):
        if len(userInput) != 2:
            return False

        x, y = userInput

        return self.isPositionXValid(x) and self.isPositionYValid(y) \
            and self.grid[self.parseYPositionInput(y)][self.parseXPositionInput(x)] is None

    def retrieveParsedPosition(self, userInput):
        x, y = userInput

        return (self.parseYPositionInput(y), self.parseXPositionInput(x))

    def hasAdjacentBuildingsForPosition(self, x, y):
        adjacentPositions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for dx, dy in adjacentPositions:
            if 0 <= dx < self.rowCount and 0 <= dy < self.colCount and self.hasBuildingOnPosition(dx, dy):
                return True

        return False

    def hasBuildingOnPosition(self, x, y):
        return self.grid[x][y] is not None

    def updateGrid(self, x, y, buildingName):
        # convert the user input to 0-indexed for array processing
        self.grid[x][y] = self.createBuilding(buildingName, x, y)

    def updateGridSize(self, x, y):
        self.rowCount = int(x)
        self.colCount = int(y)
        self.initializeGrid()

    def createBuilding(self, buildingName, x, y):
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

            # raise exception if the building input cannot be found in the cases
            case _:
                raise Exception()

    def decreaseBuildingCount(self, buildingName):
        self.availableBuildings.decreaseAvailableBuilding(buildingName)

    def retrieveBuildingsScore(self):
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

            # mark the current position as visited
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
                # update the dp value as 1 if a park building is found
                if self.grid[x][y] is not None and self.grid[x][y].getName() == Buildings.PARK.value and not visited[x][y]:
                    parkSize = dfs(x, y)
                    score = scoresMap[parkSize]
                    scoreBreakdown.append(score)
                    result += score

        return (result, scoreBreakdown)

    def retrieveTwoRandomBuildings(self):
        return self.availableBuildings.retriveTwoRandomBuildings()

    # displays the grid and adapts to each building type
    def displayGrid(self):
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
                        # raise exception if the building input cannot be found in the cases
                        case _:
                            raise Exception()
                lowerGridline += "-----+"
            if self.rowCount <= 2:
                row += f"\t {self.availableBuildings.buildings[x * 2]}: {self.availableBuildings.availability[x * 2]}"
                lowerGridline += f"\t {self.availableBuildings.buildings[x * 2 + 1]}: {self.availableBuildings.availability[x * 2 + 1]}"
                if self.colCount == 6:
                    lastRemainingBuilding = f"\t\t\t\t\t {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}\n"
                else:
                    for y in range(self.colCount):
                        lastRemainingBuilding += "\t"
                    lastRemainingBuilding += f" {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}\n" 

                print(row)
                print(lowerGridline)
                if x == 1:
                    print(lastRemainingBuilding)
                
            else:
                row += f"\t {self.availableBuildings.buildings[x * 2]}: {self.availableBuildings.availability[x * 2]}" \
                    if x < 2 else ""
                row += f"\t {self.availableBuildings.buildings[4]}: {self.availableBuildings.availability[4]}" \
                    if x == 2 else ""
                lowerGridline += f"\t {self.availableBuildings.buildings[x * 2 + 1]}: {self.availableBuildings.availability[x * 2 + 1]}" \
                    if x < 2 else "\n" if x == self.rowCount - 1 else ""

                print(row)
                print(lowerGridline)

    # parses the grid as an array of string, allowing it to be written into txt file
    def parseGridAsString(self):
        returnStrArr = []
        for row in self.grid:
            rowStr = []
            for v in row:
                rowStr.append("None" if v is None else v.name)
            returnStrArr.append(",".join(rowStr))
        return returnStrArr

    # re-initializes grid to be empty
    def initializeGrid(self):
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.availableBuildings.availability = [8] * 5
        self.factoryList.clear()
        
    # checks if save game file exists
    def isSavedGameExist(self):
        return os.path.exists(savedGameFilename)

    # serialising from file to grid object
    def readGridFromFile(self):
        if not self.isSavedGameExist():
            return
        lines = self.readFiles()

        isFileValid, formattedGrid = self.isSavedGameFileValid(lines)
        if isFileValid:
            self.grid = formattedGrid
            print('Successfully loaded the game!')


    def isSavedGameFileValid(self, lines):
        if len(lines) != self.rowCount:
            return (False, None)

        validBuildings = set(['None', 'BCH', 'FAC', 'HSE', 'SHP', 'HWY', 'MON', 'PRK'])
        results = []

        len(lines[0])

        for line in lines:
            line = line.strip("\n").split(',')
            if len(line) != self.colCount:
                return (False, None)

            for building in line:
                if building not in validBuildings:
                    return (False, None)
            results.append(line)

        return (True, results)

    def readFiles(self):
        lines = None
        with open(savedGameFilename, "r+") as file:
            lines = file.readlines()

        return lines
