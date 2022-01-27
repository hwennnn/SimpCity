"""
This module deals with the Factory building object.
"""
__docformat__ = "google"
from models.buildings.building import Building


class Factory(Building):
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

    def retrieveBuildingScore(self, grid):  # pragma: no cover
        """
        Args:
            grid (Grid): The grid object which is passed in as parameter (It is not used in Beach class)

        Returns:
            int: The score of the building.

        Override method to retrieve the building score. \n

        The score calculation for park building only needs to be done once, hence it is implemented in Grid object.

        """
        pass
