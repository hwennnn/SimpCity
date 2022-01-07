from abc import ABC, abstractmethod


class Building(ABC):  # use absract class as the buildings have some common traits (so dont have to re-initialised in each class)
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        return self.name

    @abstractmethod
<<<<<<< HEAD
    def retrieveBuildingScore(self):
=======
    def retrieveBuildingScore(self, grid):
>>>>>>> 04888cc4a69a3b38dd45c08fd671adbd18fd1da1
        pass
