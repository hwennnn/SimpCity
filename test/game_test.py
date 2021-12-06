# Functional Test / Test the whole flow
import test.player_test as unit_Player
from models.player import Player
from models.game import Game
import pytest
from pathlib import Path
import sys
path = str(Path(Path('game_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)


game_test = Game()
player_test = Player()


def test_startNewGame(capfd):
    player_test.validateMain('1')
    # Reuse unit test from player_test.py
    unit_Player.test_displayGrid(capfd)
    assert player_test.turns == 1

# Test exit when player started the game


def test_ExitFromGrid(capfd):
    player_test.validateMain('1')
    player_test.startNewGame()  # Init turns == 1
    player_test.validateGame('0')
    assert player_test.turns == 1
    # Reuse unit test from player_test.py
    unit_Player.test_ExitGame(capfd, "0", "---- Game Ended----")
