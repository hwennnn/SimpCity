from abc import ABC, abstractmethod


class Building(ABC):  # use absract class as the buildings have some common traits (so dont have to re-initialised in each class)
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        return self.name

    @abstractmethod
    def retrieveBuildingScore(self):
        pass
