"""
This module deals with the Highway building object.
"""
__docformat__ = "google"
from models.buildings.building import Building
from models.enums import Buildings


class Highway(Building):
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

        A Highway (HWY) scores 1 point per Highway that is connected horizontally to the target highway.
        If a Highway is placed on A1, B1 and C1, there will be 3 horizontally connected highway. Therefore,
        each Highway in that connection will score 3 points.
        If a Highway is placed on A1 and C1, there is no connection. Therefore, each Highway only scores 1 point.

        """
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
