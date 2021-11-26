# Functional Test / Test the whole flow
from pathlib import Path
import sys
path = str(Path(Path('game_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import pytest
from models.game import Game
from models.player import Player
import test.player_test as unit_Player

game_test = Game()
player_test = Player()

def test_startNewGame(capfd):
    player_test.validateMain('1')
    unit_Player.test_displayGrid(capfd) # Reuse unit test from player_test.py
    assert player_test.turns == 1

# Test exit when player started the game
def test_ExitFromGrid(capfd):
    player_test.validateMain('1')
    player_test.startNewGame() # Init turns == 1
    player_test.validateGame('0')
    player_test.validateMain('0')
    out, err = capfd.readouterr()
    assert player_test.turns == 1
    assert "---- Game Ended----"