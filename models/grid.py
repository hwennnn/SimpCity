import collections
from models.available_buildings import AvailableBuildings
from models.buildings import *
from models.enums import Buildings
from models.configurations import *
from collections import deque


class Grid:  # Grid Class
    def __init__(self):
        self.rowCount = self.colCount = 4
        # First initialise the object in each position as None
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.factoryList = []
        self.availableBuildings = AvailableBuildings()

    def isPositionXValid(self, x):
        return len(x) == 1 and ord('A') <= ord(x.upper()) <= ord('D')

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
            if 0 <= dx < 4 and 0 <= dy < 4 and self.hasBuildingOnPosition(dx, dy):
                return True

        return False

    def hasBuildingOnPosition(self, x, y):
        return self.grid[x][y] is not None

    def updateGrid(self, x, y, buildingName):
        # convert the user input to 0-indexed for array processing
        self.grid[x][y] = self.createBuilding(buildingName, x, y)

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
        scores = 0
        # Declare exceptions for Park and Factory calculation
        exceptionList = [Buildings.PARK.value, Buildings.FACTORY.value]
        scores += self.calculateFactoryBuildingsScore()
        scores += self.calculateParkBuildingsScore()

        for x in range(self.rowCount):
            for y in range(self.colCount):
                if self.grid[x][y] is not None and self.grid[x][y].getName() not in exceptionList:
                    scores += self.grid[x][y].retrieveBuildingScore(self.grid)

        return scores

    def calculateFactoryBuildingsScore(self):
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
                        result += factoryScore

                    if len(self.factoryList) >= 5:
                        result += (factoryScore * 4) if self.factoryList.index(
                            self.grid[x][y]) < 4 else factoryScore

        return result

    def calculateParkBuildingsScore(self):
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
                    result += scoresMap[parkSize]

        return result

    def retrieveTwoRandomBuildings(self):
        return self.availableBuildings.retriveTwoRandomBuildings()

    def displayAvailableBuildings(self):
        self.availableBuildings.displayAvailableBuilding()

    # displays the grid and adapts to each building type
    # will be reformatted in later sprint for adaptability to grid size
    def displayGrid(self):
        print("\n    A     B     C     D\t\t Remaining Buildings Left\n +-----+-----+-----+-----+\t ------------------------")
        for i in range(self.rowCount):
            rowline = "{0}| ".format(i + 1)
            for build in self.grid[i]:
                if build is None:
                    rowline += "    | "
                else:
                    match build.getName():
                        case Buildings.BEACH.value:
                            rowline += Buildings.BEACH.value + " | "
                        case Buildings.FACTORY.value:
                            rowline += Buildings.FACTORY.value + " | "
                        case Buildings.HIGHWAY.value:
                            rowline += Buildings.HIGHWAY.value + " | "
                        case Buildings.HOUSE.value:
                            rowline += Buildings.HOUSE.value + " | "
                        case Buildings.SHOP.value:
                            rowline += Buildings.SHOP.value + " | "
                        case Buildings.MONUMENT.value:
                            rowline += Buildings.MONUMENT.value + " | "
                        case Buildings.PARK.value:
                            rowline += Buildings.PARK.value + " | "
                        # raise exception if the building input cannot be found in the cases
                        case _:
                            raise Exception()
            print("{0}\t {1}: {2}\n +-----+-----+-----+-----+".format(rowline,
                                                                      self.availableBuildings.buildings[i],
                                                                      self.availableBuildings.availability[i]))
        print("\t\t\t\t {0}: {1}".format(
            self.availableBuildings.buildings[4], self.availableBuildings.availability[4]))

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

    def isSavedGameExist(self):
        pass

    # serialising from file to grid object
    def readGridFromFile(self):
        pass

    def isSavedGameFileValid(self, lines):
        pass

    def readFiles(self):
        pass
