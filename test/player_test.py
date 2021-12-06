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


validOptionMainTestData = \
    [("1", "You selected option 1"),
     ("2", "You selected option 2")]


@pytest.mark.parametrize("option, expectedResult", validOptionMainTestData)
def test_validOptionMain(capfd, option, expectedResult):
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert expectedResult in out


invalidOptionMainTestData = \
    [("3", "Invalid option!"),
     ("4", "Invalid option!"),
     ("10", "Invalid option!"),
     ("a", "Invalid option!")]


@pytest.mark.parametrize("option, expectedResult", invalidOptionMainTestData)
def test_invalidOptionMain(capfd, option, expectedResult):
    player_test.validateMain(option)
    out, err = capfd.readouterr()
    assert expectedResult in out


exitGameTestData = \
    [("0", "---- Game Ended----")]


@pytest.mark.parametrize("option, expectedResult", exitGameTestData)
def test_ExitGame(capfd, option, expectedResult):
    with pytest.raises(SystemExit) as e:
        player_test.validateMain(option)

    out, err = capfd.readouterr()
    assert expectedResult in out
    assert e.type == SystemExit
    assert e.value.code == 0


def test_validOptionGame(capfd):
    option = "2"
    player_test.validateGame(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" in out


def test_invalidOptionGame(capfd):
    option = "a"
    player_test.validateGame(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" not in out


def test_ExitGame11(capfd):
    option = "0"
    player_test.validateGame(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" in out


def test_checkFileSaved():
    player_test.saveGame()
    rootDirWithFile = currentDirectory.joinpath(savedGameFilename)
    assert rootDirWithFile.exists()
