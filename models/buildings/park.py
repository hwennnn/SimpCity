from models.buildings.building import Building


class Park(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    # the score calculation for park building only needs to be done once, hence it is implemented in grid.py
    def retrieveBuildingScore(self, grid):
        pass
