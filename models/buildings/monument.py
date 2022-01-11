from models.buildings.building import Building
from models.enums import Buildings


class Monument(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        cornerCount = 0
        rowCount, colCount = len(grid), len(grid[0])

        corners = set([(0, 0), (0, colCount - 1),
                      (rowCount - 1, 0), (rowCount - 1, colCount - 1)])

        for x, y in corners:
            if grid[x][y] is not None and grid[x][y].getName() == Buildings.MONUMENT.value:
                cornerCount += 1

        if cornerCount >= 3:
            return 4
        else:
            if (self.x, self.y) in corners:
                return 2
            else:
                return 1
