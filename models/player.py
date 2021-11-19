from models.grid import Grid


class Player:  # Player Class
    def __init__(self):
        self.score = 0
        self.turns = 0
        self.grid = Grid()

    def displayMainMenu(self):

        print("""
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game

0. Exit
""")

    def promptMainMenu(self):
        return input('Please enter an input: ')

    def validateMain(self, option):
        if option == '0':
            print('---- Game Ended----')

        else:
            print(f"You selected option {option}")

    def startNewGame(self):
        pass

    def displayGrid(self):
        self.grid.displayGrid()

    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def exitToMainMenu(self):
        pass

    def exitGame(self):
        pass
