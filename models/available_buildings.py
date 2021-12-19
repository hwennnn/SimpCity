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
        available_buildings = [[self.buildings[i].value] * self.availability[i]
                               for i in range(len(self.availability)) if self.availability[i] > 0]

        # flatten 2d array into 1d array
        flatten_buildings = sum(available_buildings, [])

        random.shuffle(flatten_buildings)

        return flatten_buildings

    # Return the first two element of the shuffled buildings
    # Logically the length of the shuffled buildings should be always greater than two
    def retriveTwoRandomBuildings(self):
        shuffled_buildings = self.shuffleCurrentAvailableBuildings()

        return shuffled_buildings[:2]

    # Displays remaining buildings for the current turn
    # Goes through list of buildings and display their availability based on indexes
    def displayAvailableBuilding(self):
        for building in self.buildings:
            
