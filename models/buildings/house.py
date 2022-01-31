"""
This module deals with the House building object.
"""
__docformat__ = "google"
from models.buildings.building import Building
from models.enums import Buildings


class House(Building):
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

        A House (HSE) scores 1 point for each adjacent House or Shop (SHP) Building.
        It also scores 2 points for each adjacent Beach (BCH) Building.
        However, if there is a Factory (FAC) built adjacent to the House, it will only score
        1 point no matter what building is built adjacent to the House.
        When calculating scoring for the House, the target House building does not have any point values
        and only gains its point values from its adjacent buildings (HSE/SHOP/BCH/FAC).

        """
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
