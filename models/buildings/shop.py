from building import Building


class Shop:
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self):
        pass