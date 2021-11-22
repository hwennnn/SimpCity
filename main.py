from models.player import Player

player = Player()

while True:

    player.displayMainMenu()
    option = player.promptMainMenu()
    player.validateMain(option)

    if option == '0':
        break
    
    elif option == '1':
        player = player.startNewGame()

    elif option == '2':
        player.loadGame()

