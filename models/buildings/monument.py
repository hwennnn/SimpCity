__docformat__ = "google"
"""
This module deals with the Monument building object.
"""
from models.buildings.building import Building
from models.enums import Buildings


class Monument(Building):
    name: str
    """The name of the building"""
    x: int
    """The position of the building placed on x-axis in the grid."""
    y: int
    """The position of the building placed on y-axis in the grid."""

    def __init__(self, name, x, y):
        """
        Initialise the building object with name, position on x-axis and position on y-axis.
        """
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        """
        Args:
            grid (Grid): The grid object which is passed in as parameter (It is not used in Beach class)

        Returns:
            int: The score of the building.

        Override method to retrieve the building score. \n

        A Monument is a new type of building. If it is not
        built on a corner square (i.e., A1, A4, D1 or D4), it scores 1 point. If it is
        built on a corner square, it scores 2 points. However, if there are at least
        3 monuments in the city that are built on corner squares, then all
        monuments score 4 points each (including those that are not built on
        corner squares).

        """
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
