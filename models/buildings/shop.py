"""
This module deals with the Shop building object.
"""
__docformat__ = "google"
from models.buildings.building import Building
from models.enums import Buildings


class Shop(Building):
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

        A Shop (SHP) scores 1 point for each unique building type adjacent to the target Shop.
        The Shop building scores 1 point on its own for being a unique building value.
        If there are 4 different building types adjacent to the target shop, it scores 5 points
        If there are 3 different building types adjacent to the target shop, it scores 4 points
        If the target shop is surrounded by other Shops, it is counted as 1 unique building type,
        thus scoring 1 point.

        """
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