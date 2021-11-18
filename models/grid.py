from models.enums import Buildings

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
        pass