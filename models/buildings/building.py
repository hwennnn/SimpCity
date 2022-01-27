"""
This module deals with the building abstract object. 
This is the building absract class as the buildings have some common traits, 
hence we don't have to re-initialised those fields in each class.
"""
__docformat__ = "google"

from abc import ABC, abstractmethod


class Building(ABC):
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
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        """
        Returns:
            str: The name of the building.

        Retrieve the name of the building.
        """
        return self.name

    # pragma: no cover
    @abstractmethod
    def retrieveBuildingScore(self, grid):  # pragma: no cover
        """
        Args:
            grid (Grid): The grid object which is passed in as parameter.

        Returns:
            int: The score of the building.

        Abstract method to retrieve the building score.
        """
        pass
