from models.player import Player

class Game: #Game Class
    def __init__(self):
        self.player = Player()

    def startNew(self):
        self.player.startNewGame()
        while True:
            print("""
Turn: {0}""".format(self.player.turns))
            self.player.displayGrid()
            self.player.displayGameMenu()
            option = self.player.promptGameMenu()
            self.player.validateGame(option)
        
            if option == '0':
                break
        
            elif option == '5':
                self.player.saveGame()

