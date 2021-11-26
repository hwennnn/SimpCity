from models.game import Game

game = Game()

while True:

    game.player.displayMainMenu()
    option = game.player.promptMainMenu()
    game.player.validateMain(option)

    if option == '0':
        break
    
    elif option == '1':
        game.launchGame()

    elif option == '2':
        game.player.loadGame()

