from models.enums import Buildings
import random


class AvailableBuildings:
    def __init__(self):
        self.availability = [8] * 5
        # The sequence follows as:
        # Beaches, Factories, Houses, Shops, Highways
        self.buildings = [Buildings.BEACH, Buildings.FACTORY,
                          Buildings.HOUSE, Buildings.SHOP, Buildings.HIGHWAY]

    # decrease the available building
    def decreaseAvailableBuilding(self, buildingName):
        pass

    # First flatten the current available buildings into 1D array
    # Then use random module to shuffle the array
    # Return the shuffled buildings
    def shuffleCurrentAvailableBuildings(self):
        pass

    # Return the first two element of the shuffled buildings
    # Logically the length of the shuffled buildings should be always greater than two
    def retriveTwoRandomBuildings(self):
        pass
