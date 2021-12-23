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
            and self.grid[self.parseXPositionInput(x)][self.parseYPositionInput(y)] is None

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
        pass

    def createBuilding(self, buildingName, x, y):
        pass

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
                        case "beach":
                            rowline += Buildings.BEACH.value + " | "
                        case "factory":
                            rowline += Buildings.FACTORY.value + " | "
                        case "highway":
                            rowline += Buildings.HIGHWAY.value + " | "
                        case "house":
                            rowline += Buildings.HOUSE.value + " | "
                        case "shop":
                            rowline += Buildings.SHOP.value + " | "
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
