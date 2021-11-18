import os

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

    # parses the grid as an array of string, allowing it to be written into txt file
    def parseGridAsString(self):
        returnStrArr = []
        for row in self.grid:
            rowStr = []
            for v in row: 
                rowStr.append("None" if v is None else v)
            returnStrArr.append(",".join(rowStr))
        return returnStrArr


    # serialising from file to grid object
    def readGridFromFile(self, savedFile):
        if os.path.exists(savedFile):
            with open(savedFile, "r+") as file: 
                lines = file.readlines()
                for line in lines: 
                    line.split(",").strip("\n") #striping from reading file
                print(lines)




