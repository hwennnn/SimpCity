__docformat__ = "google"
"""
This module deals with the Beach building object.
"""

from models.buildings.building import Building


class Beach(Building):
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

    def retrieveBuildingScore(self, grid=None):
        """
        Args:
            grid (Grid): The grid object which is passed in as parameter (It is not used in Beach class)

        Returns:
            int: The score of the building.

        Override method to retrieve the building score. \n

        A Beach (BCH) scores 3 points if it is built in column A or column D, or 1 point
        otherwise.


        """
        return 3 if self.y in (0, 3) else 1
