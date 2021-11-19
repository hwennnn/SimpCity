from models.enums import Buildings
from models.buildings.beach import Beach

class Grid:  # Grid Class
    def __init__(self):
        self.rowCount = self.colCount = 4
        # First initialise the object in each position as None
        self.grid = [[None] * self.colCount for _ in range(self.rowCount)]

    def isPositionXValid(self, x):
        pass

    def isPositionYValid(self, y):
        pass

    def parseXPositionInput(self, x):
        pass

    def parseYPositionInput(self, y):
        pass

    def isPositionValid(self, userInput):
        pass

    def updateGrid(self, x, y, buildingName):
        pass

    def createBuilding(self, buildingName, x, y):
        pass

    def retrieveBuildingsScore(self):
        pass

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
"""        {0}
         +-----+-----+-----+-----+ """.format(rowline))