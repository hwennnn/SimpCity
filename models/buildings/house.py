from models.buildings.building import Building
from models.enums import Buildings


class House(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        result = 0
        rowCount, colCount = len(grid), len(grid[0])

        # Prepare a list for storing adjacent coordinates and adjacent buildings
        adjacentPositions = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
        adjacentBuildings = []

        for dx, dy in adjacentPositions:
            if 0 <= dx < rowCount and 0 <= dy < colCount and grid[dx][dy] is not None:
                adjacentBuildings.append(grid[dx][dy])

        #Create a matches case for looping through all adjacent buildings
        for building in adjacentBuildings:

            match building.getName():
                #Case of Factory only adds 1 point and breaks the loop
                case Buildings.FACTORY.value:
                    result = 1
                    return result
                case Buildings.HOUSE.value:
                    result += 1
                case Buildings.SHOP.value:
                    result += 1
                case Buildings.BEACH.value:
                    result += 2

        return result
