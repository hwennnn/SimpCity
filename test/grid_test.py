from pathlib import Path
import sys
path = str(Path(Path('grid_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import pytest
from models.player import Player
from process import run

player_test = Player()

# Test the display of a empty grid
def test_EmptyGrid(capfd):
    player_test.displayGrid()
    out, err = capfd.readouterr()
    assert """
    A     B     C     D
 +-----+-----+-----+-----+ 
1|     |     |     |     | 
 +-----+-----+-----+-----+ 
2|     |     |     |     | 
 +-----+-----+-----+-----+ 
3|     |     |     |     | 
 +-----+-----+-----+-----+ 
4|     |     |     |     | 
 +-----+-----+-----+-----+ 
""" in out

# Test exit when player started the game
def test_ExitFromGrid(capfd):
    player_test.validateMain('1')
    out, err = capfd.readouterr()
    run(player_test.validateGame('0'))
    out, err = capfd.readouterr()
    assert "---- Game Ended----" in out