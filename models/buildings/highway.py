from models.buildings.building import Building
from models.enums import Buildings


class Highway(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        result = 1
        rowCount, colCount = len(grid), len(grid[0])

        # Prepare a list of row coordinates for horizontal positions of highway location
        rowLeftPositions = [(self.x, self.y - 1), (self.x, self.y - 2), (self.x, self.y - 3)]
        rowRightPositions = [(self.x, self.y + 1), (self.x, self.y + 2), (self.x, self.y + 3)]
        rowBuildingLeft = []
        rowBuildingRight = []

        # Add buildings from grid into left and right list
        for dx, dy in rowLeftPositions:
            if 0 <= dx < rowCount and 0 <= dy < colCount:
                rowBuildingLeft.append(grid[dx][dy].getName() if grid[dx][dy] is not None else "None")

        for dx, dy in rowRightPositions:
            if 0 <= dx < rowCount and 0 <= dy < colCount:
                rowBuildingRight.append(grid[dx][dy].getName() if grid[dx][dy] is not None else "None")

        # Check if target Highway building is connected to other Highway buildings from left and right
        # if subsequent building is not a highway, it means there is no more connection, therefore loop will break
        if len(rowBuildingLeft) != 0:
            for buildingName in rowBuildingLeft:
                if buildingName == Buildings.HIGHWAY.value:
                    result += 1
                else:
                    break
                    
        if len(rowBuildingRight) != 0:
            for buildingName in rowBuildingRight:
                if buildingName == Buildings.HIGHWAY.value:
                    result += 1
                else:
                    break
        
        return result
