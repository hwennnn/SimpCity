from models.player import Player


class Game:  # Game Class
    def __init__(self):
        self.player = Player()

    def launchGame(self):
        backToMainMenu = False
        while backToMainMenu != True:
            backToMainMenu = self.launchGameHelper()

    def launchGameHelper(self):
        print("""
Turn: {0}""".format(self.player.turns))
        self.player.displayGrid()
        self.player.displayGameMenu()
        option = self.player.promptGameMenu()
        self.player.validateGame(option)

        if option == '0':
            subOption = self.player.promptSaveGame()
            self.player.validateSaveGame(subOption)
            if subOption == "Y":
                return True

        elif option == '3':
            self.player.displayAvailableBuildings()

        elif option == '5':
            self.player.saveGame()

        return False
