from models.grid import Grid


class Player:  # Player Class
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turns = 0
        self.grid = Grid()

    def startNewGame(self):
        pass

    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        pass
