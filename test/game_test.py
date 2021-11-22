from pathlib import Path
import sys
path = str(Path(Path('game_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import pytest
from models.game import Game

game_test = Game()

def test_startNewGame(capfd):
    game_test.startNew()
    out, err = capfd.readouterr()
    assert """

1.
2.
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu""" in out
