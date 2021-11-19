from models.player import Player

def process(player):
    while True:
        print("""
Turn: {0}""".format(player.turns))
        player.displayGrid()
        player.displayGameMenu()
        option = player.promptGameMenu()
        player.validateMain(option)
        
        if option == '0':
            break
        
        elif option == '5':
            player.saveGame()
        