from models.player import Player

class Game: #Game Class
    def __init__(self, player = Player()):
        self.player = player

    def launchGame(self):
        self.player.startNewGame()
        while True:
            print("\nTurn: {0}".format(self.player.turns))
            self.player.displayGrid()
            self.player.displayGameMenu()
            option = self.player.promptGameMenu()
            self.player.validateGame(option)
        
            if option == '0':
                subOption = self.player.promptSaveGame()
                self.player.validateSaveGame(subOption)
                if subOption == "Y":
                    break
                
                elif subOption == "N":
                    continue

            elif option == '3':
                self.player.retrieveBuildingsScore()

            elif option == '4':
                self.player.saveGame()

