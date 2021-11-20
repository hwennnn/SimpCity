from pathlib import Path
import sys
path = str(Path(Path('grid_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import pytest
from models.player import Player

player_test = Player()

def test_displayMainMenu(capfd):
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

def test_ExitGame(capfd):
    player_test.displayGrid()
    option = "0"
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert "---- Game Ended----" in out



