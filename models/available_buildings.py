from models.enums import Buildings
import random


class AvailableBuildings:
    def __init__(self):
        self.availability = [8] * 5
<<<<<<< HEAD
        # The sequence follows as:
        # Beaches, Factories, Houses, Shops, Highways
        self.buildings = [Buildings.BEACH.value, Buildings.FACTORY.value,
                          Buildings.HOUSE.value, Buildings.SHOP.value, Buildings.HIGHWAY.value]

    # decrease the available building
=======

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

>>>>>>> 04888cc4a69a3b38dd45c08fd671adbd18fd1da1
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

<<<<<<< HEAD
        return shuffled_buildings[:2]

    # Displays remaining buildings for the current turn
    # Goes through list of buildings and display their availability based on indexes
    def displayAvailableBuilding(self):
        print(f"\nBuilding\tRemaining\n--------\t--------")
        for i in range(len(self.buildings)):
            print(self.buildings[i] + "\t\t" + str(self.availability[i]))
=======
        return shuffled_buildings[:2]
>>>>>>> 04888cc4a69a3b38dd45c08fd671adbd18fd1da1
