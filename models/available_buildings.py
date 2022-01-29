"""
This module deals with the AvailableBuildings object.
"""
__docformat__ = "google"

from models.enums import Buildings
from collections import Counter
import random


class AvailableBuildings:
    availability: list[str]
    """
    The availability of each building based on the current buildings array. \n
    For example,
    buildings[i] would still have availability[i] pieces available to be placed in the grid.
    """
    buildings: list[str]
    """
    The current available buildings selected by the user. \n
    Initially it consists of BCH, FAC, HSE, SHP, HWY. However it can later be configured in the user option menu.
    """
    buildingsPool: list[str]
    """
    The available buildings pool for selection. \n
    It consists of BCH, FAC, HSE, SHP, HWY, MON, PRK.
    """

    def __init__(self):
        """
        Initialise the AvailableBuildings object with default value for availability, current buildings pool and total buildings pool.
        """
        self.availability = [8] * 5

        self.buildings = [
            Buildings.BEACH.value, Buildings.FACTORY.value,
            Buildings.HOUSE.value, Buildings.SHOP.value, Buildings.HIGHWAY.value
        ]

        self.buildingsPool = [
            Buildings.BEACH.value, Buildings.FACTORY.value,
            Buildings.HIGHWAY.value, Buildings.HOUSE.value, Buildings.SHOP.value,
            Buildings.MONUMENT.value, Buildings.PARK.value
        ]

    def updateBuildingPool(self, options):
        """
        Args:
            options (str): The options entered by user for the update of buildings pool.

        The method will first clear the current buildings pool. Then, it will append each building based on the user option.

        """
        self.buildings.clear()

        for option in options.split(','):
            buildingIndex = int(option) - 1
            self.buildings.append(self.buildingsPool[buildingIndex])

    def displayCurrentBuildingPool(self):
        """
        The method will display the current building pool based on the buildings array.

        """
        print(f"Current Building Pool: {','.join(self.buildings)}")
        
    def decreaseAvailableBuilding(self, buildingName):
        """
        Args:
            buildingName (str): The buildingName entered by the user.

        The method will be called when the user placed a building on the grid. 
        Then, it will decrease the building availaibility count according based on the user option.

        """
        building_index = self.buildings.index(buildingName)
        self.availability[building_index] -= 1

    def shuffleCurrentAvailableBuildings(self):
        """
        Returns:
            list[str]: An array of shuffled buildings.

        This method will shuffle the current available buildings from the building pool for the randomised building selection feature. \n
        First, it will flatten the current available buildings into 1D array, then it will use random module to shuffle the array.


        """
        available_buildings = [[self.buildings[i]] * self.availability[i]
                               for i in range(len(self.availability)) if self.availability[i] > 0]

        # flatten 2d array into 1d array
        flatten_buildings = sum(available_buildings, [])

        random.shuffle(flatten_buildings)

        return flatten_buildings

    def retriveTwoRandomBuildings(self):
        """
        Returns:
            list[str]: The first two element of the shuffled buildings

        This method will return the first two element of the shuffled buildings.
        Logically the length of the shuffled buildings should be always greater than two.


        """
        shuffled_buildings = self.shuffleCurrentAvailableBuildings()

        return shuffled_buildings[:2]

    # Update the available buildings 
    def updateAvailableBuildings(self, buildings):
        self.availability = [8] * 5 # init availabilities for each building
        buildingCounter = Counter(buildings)
        for building in buildingCounter.keys():
            if building != "None":
                building_index = self.buildingsPool.index(building)
                self.availability[building_index] -= buildingCounter[building]

    # Return list of buildings as string of indexes
    def exportBuildings(self): 
        return ",".join(str(self.buildingsPool.index(building) + 1 ) for building in self.buildings)

    # Return list of buildings as string of building names
    def exportBuildingsNames(self):
        return ",".join(self.buildingsPool[int(building)-1] for building in self.exportBuildings().split(","))
      
