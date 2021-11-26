# Unit Test Only
import os
import sys
import pytest
from models.player import Player
from models.configurations import *
from pathlib import Path

path = str(Path(Path("player_test.py").parent.absolute()).parent.absolute())
sys.path.insert(0, path)

dir_path = os.path.dirname(os.path.realpath(__file__))
currentDirectory = Path(dir_path)

player_test = Player()


def test_displayMainMenu(capfd):
    player_test.displayMainMenu()
    out, err = capfd.readouterr()
    assert """
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game

0. Exit
""" in out

# Test the display of a empty grid
def test_displayGrid(capfd):
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

def test_invalidOptionMain(capfd):
    option = "a"
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" not in out

def test_invalidOptionGame(capfd):
    option = "a"
    player_test.validateGame(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" not in out

def test_nonExit(capfd):
    option = "1"
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" in out


def test_Exit(capfd):
    option = "0"
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert "---- Game Ended----" in out

def test_ExitGame(capfd):
    option = "0"
    player_test.validateGame(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" in out 


def test_checkFileSaved():
    player_test.saveGame()
    rootDirWithFile = currentDirectory.joinpath(savedGameFilename)
    assert rootDirWithFile.exists()
