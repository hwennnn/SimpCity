"""
This module deals with all game related functions (driver code of SimpCity).
"""

from models.player import Player
from models.leaderboard import Leaderboard


class Game:
    leaderboard: Leaderboard
    """The leaderboard object associated with the game."""
    player: Player
    """The player object associated with the player"""

    def __init__(self):
        """Initialise the game object with leaderboard and player object."""
        self.leaderboard = Leaderboard()
        self.player = Player()

    def launch(self):  # pragma: no cover
        '''
        The driver function to launch the game, and it will react based on user option. \n
        The first part of the code will display the main menu, and prompt option from user.
        The later part of the code will act based on the user option: \n
        Option 0 -> Exit Game \n
        Option 1 -> Start New Game \n
        Option 2 -> Load Game \n
        Option 3 -> Display Leaderboard \n
        Option 4 -> Display Option Menu \n
        '''

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
        '''
        The driver function to start new game for the player, and it will react accordingly based on user option. \n
        First, it will initialise the player by clearing the game turns and re-initialising the whole new grid.
        The later part of the code acts similarly, which it display the game menu, and prompt for user option. \n

        Besides, this function handles the logic to end the game when the player turns exceed maximum playable turns available.
        It will display the final layout of the SimpCity and the player scores, and it will prompt the player to enter the username
        if the player score is top 10 in the leaderboard. Then, it will return the main menu.


        This function mainly calls methods residing in the player object. \n
        Option 0 -> Back to Main Menu (It will prompt user to save game if the state is not saved yet.) \n
        Option 1/2 -> Place buildings on the grid \n
        Option 3 -> Display buildings score \n
        Option 4 -> Save Game \n
        '''

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
        """The driver function to call the leaderboard object to display the score leaderboard."""
        self.leaderboard.displayLeaderboard()
