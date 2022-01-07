from models.enums import Buildings
import random


class AvailableBuildings:
    def __init__(self):
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
        self.buildings.clear()

        for option in options.split(','):
            buildingIndex = int(option) - 1
            self.buildings.append(self.buildingsPool[buildingIndex])

    def displayCurrentBuildingPool(self):
        print(f"Current Building Pool: {','.join(self.buildings)}")

    # decrease the available building

    def decreaseAvailableBuilding(self, buildingName):
        building_index = self.buildings.index(buildingName)
        self.availability[building_index] -= 1

    # First flatten the current available buildings into 1D array
    # Then use random module to shuffle the array
    # Return the shuffled buildings
    def shuffleCurrentAvailableBuildings(self):
        available_buildings = [[self.buildings[i]] * self.availability[i]
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
