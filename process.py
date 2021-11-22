def run(player):
    while True:
        print("""
Turn: {0}""".format(player.turns))
        player.displayGrid()
        player.displayGameMenu()
        option = player.promptGameMenu()
        player.validateGame(option)
        
        if option == '0':
            break
        
        elif option == '5':
            player.saveGame()
        