from models.player import Player
from models.leaderboard import Leaderboard


class Game:  # Game Class
    def __init__(self):
        self.leaderboard = Leaderboard()
        # init the player object with the game leaderboard
        # so that the player can set their high score in the leaderboard later
        self.player = Player()

    def launch(self):  # pragma: no cover
        while True:
            self.player.displayMainMenu()
            option = self.player.promptMainMenu()
            self.player.validateMain(option)

            if option == '0':
                self.player.exitGame()

            elif option == '1':
                self.launchGame()

            elif option == '2':
                self.player.loadGame()

            elif option == '3':
                self.displayLeaderboard()

            elif option == '4':
                self.player.displayOptionMenu()

    def launchGame(self):  # pragma: no cover
        self.player.startNewGame()
        while True:
            print("\nTurn: {0}".format(self.player.turns))
            self.player.displayGrid()
            self.player.displayGameMenu()
            option = self.player.promptGameMenu()
            self.player.validateGame(option)

            if option == '0':
                if self.player.savedGame == False:
                    subOption = self.player.promptSaveGame()
                    self.player.validateSaveGame(subOption)
                    if subOption == "Y":
                        self.player.saveGame()
                        break

                    elif subOption == "N":
                        break
                else:
                    self.player.validateSaveGame("N")
                    break

            elif option == '3':
                self.player.displayBuildingsScore()

            elif option == '4':
                self.player.saveGame()
                self.player.savedGameSuccessful()

            maxPlayerTurns = min(self.player.grid.rowCount *
                                 self.player.grid.colCount, 40)

            if self.player.turns > maxPlayerTurns:
                self.player.displayGrid(True)  # print final layout of SimpCity
                self.player.displayBuildingsScore()
                playerScore = self.player.retrieveBuildingsScore(False)
                self.leaderboard.saveScoreIntoLeaderboard(playerScore)
                self.displayLeaderboard()
                break

    def displayLeaderboard(self):
        self.leaderboard.displayLeaderboard()
