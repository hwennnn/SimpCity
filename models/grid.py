from models.available_buildings import AvailableBuildings
from models.buildings import Beach, Factory, House, Highway, Shop
from models.enums import Buildings
import os
from models.configurations import *


class Grid:  # Grid Class
    def __init__(self):
        self.rowCount = self.colCount = 4
        # First initialise the object in each position as None
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]
        self.availableBuildings = AvailableBuildings()

    def isPositionXValid(self, x):
        return ord('A') <= ord(x.upper()) <= ord('D')

    def isPositionYValid(self, y):
        return y.isnumeric() and 1 <= int(y) <= self.rowCount

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
            if 0 <= dx < 3 and 0 <= dy < 3 and self.hasBuildingOnPosition(dx, dy):
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
                return Factory(buildingName, x, y)

            case Buildings.HOUSE.value:
                return House(buildingName, x, y)

            case Buildings.SHOP.value:
                return Shop(buildingName, x, y)

            case Buildings.HIGHWAY.value:
                return Highway(buildingName, x, y)

            # raise exception if the building input cannot be found in the cases
            case _:
                raise Exception()

    def decreaseBuildingCount(self, buildingName):
        self.availableBuildings.decreaseAvailableBuilding(buildingName)

    def retrieveBuildingsScore(self):
        pass

    def retrieveTwoRandomBuildings(self):
        return self.availableBuildings.retriveTwoRandomBuildings()

    def displayAvailableBuildings(self):
        self.availableBuildings.displayAvailableBuilding()

    # displays the grid and adapts to each building type
    def displayGrid(self):
        print("""
    A     B     C     D
 +-----+-----+-----+-----+ """)
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

                        # raise exception if the building input cannot be found in the cases
                        case _:
                            raise Exception()
            print(
                """{0}
 +-----+-----+-----+-----+ """.format(rowline))

    # parses the grid as an array of string, allowing it to be written into txt file
    def parseGridAsString(self):
        returnStrArr = []
        for row in self.grid:
            rowStr = []
            for v in row:
                rowStr.append("None" if v is None else v.name)
            returnStrArr.append(",".join(rowStr))
        return returnStrArr

    def isSavedGameExist(self):
        pass

    # serialising from file to grid object
    def readGridFromFile(self):
        pass

    def isSavedGameFileValid(self, lines):
        pass

    def readFiles(self):
        pass
