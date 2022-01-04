import sys
from models.game import Game

game = Game()

while True:

    game.player.displayMainMenu()
    option = game.player.promptMainMenu()
    game.player.validateMain(option)

    if option == '0':
        game.player.exitGame()

    elif option == '1':
        game.launchGame()

    elif option == '2':
        game.player.loadGame()

    elif option == '3':
        game.player.displayOptionMenu()
