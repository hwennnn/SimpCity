import sys
from models.game import Game

game = Game()

game.launchGameHelper()
print(game.player.grid.grid[0][0] is not None)
