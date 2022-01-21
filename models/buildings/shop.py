from models.buildings.building import Building
from models.enums import Buildings


class Shop(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        result = 1
        rowCount, colCount = len(grid), len(grid[0])

        # Prepare a list for storing adjacent coordinates and adjacent buildings
        adjacentPositions = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
        adjacentBuildingsValue = []

        # Save string value for respective buildings
        for dx, dy in adjacentPositions:
            if 0 <= dx < rowCount and 0 <= dy < colCount and grid[dx][dy] is not None and grid[dx][dy].getName() != Buildings.SHOP.value:
                adjacentBuildingsValue.append(grid[dx][dy].getName())
        
        # Count unqiue values in list using set() function
        adjacentBuildingsSet = set(adjacentBuildingsValue)
        result += len(adjacentBuildingsSet)
        
        return result