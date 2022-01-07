from models.buildings.building import Building


class House(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

<<<<<<< HEAD
    def retrieveBuildingScore(self):
=======
    def retrieveBuildingScore(self, grid):
>>>>>>> 04888cc4a69a3b38dd45c08fd671adbd18fd1da1
        pass
