# Unit Test Only
import os
import sys
import pytest
from models.available_buildings import AvailableBuildings
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
    out, _ = capfd.readouterr()
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
    out, _ = capfd.readouterr()
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


validMainOptionTestData = \
    [("1", "You selected option 1"),
     ("2", "You selected option 2")]


@pytest.mark.parametrize("option, expectedResult", validMainOptionTestData)
def test_validMainOption(capfd, option, expectedResult):
    player_test.validateMain(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


invalidMainOptionTestData = \
    [("3", "Invalid option!"),
     ("4", "Invalid option!"),
     ("10", "Invalid option!"),
     ("a", "Invalid option!"),
     ("abc", "Invalid option!")]


@pytest.mark.parametrize("option, expectedResult", invalidMainOptionTestData)
def test_invalidMainOption(capfd, option, expectedResult):
    player_test.validateMain(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


exitGameTestData = \
    [("0", "---- Game Ended----")]


@pytest.mark.parametrize("option, expectedResult", exitGameTestData)
def test_ExitGame(capfd, option, expectedResult):
    with pytest.raises(SystemExit) as e:
        player_test.validateMain(option)

    out, _ = capfd.readouterr()
    assert expectedResult in out
    assert e.type == SystemExit
    assert e.value.code == 0


validGameOptionTestData = \
    [("0", "You selected option 0"),
     ("1", "You selected option 1"),
     ("2", "You selected option 2"),
     ("3", "You selected option 3"),
     ("4", "You selected option 4"),
     ("5", "You selected option 5")]


@pytest.mark.parametrize("option, expectedResult", validGameOptionTestData)
def test_validGameOption(capfd, option, expectedResult):
    player_test.validateGame(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


invalidGameOptionTestData = \
    [("6", "Invalid option!"),
     ("7", "Invalid option!"),
     ("8", "Invalid option!"),
     ("9", "Invalid option!"),
     ("10", "Invalid option!"),
     ("abc", "Invalid option!")]


@pytest.mark.parametrize("option, expectedResult", invalidGameOptionTestData)
def test_invalidGameOption(capfd, option, expectedResult):
    player_test.validateGame(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


def test_checkFileSaved():
    player_test.saveGame()
    rootDirWithFile = currentDirectory.joinpath(savedGameFilename)
    assert rootDirWithFile.exists()


def test_shuffleCurrentAvailableBuildings():
    available_buildings = player_test.grid.availableBuildings
    shuffled_buildings = available_buildings.shuffleCurrentAvailableBuildings()

    assert len(shuffled_buildings) >= 2 and len(
        shuffled_buildings) == len(available_buildings)


def test_retriveTwoRandomBuildings():
    available_buildings = player_test.grid.availableBuildings
    two_random_buildings = available_buildings.shuffleCurrentAvailableBuildings()

    assert len(two_random_buildings) == 2
