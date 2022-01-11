# Unit Test Only
import os
import sys
import pytest
from models.available_buildings import AvailableBuildings
from models.player import Player
from models.configurations import *
from pathlib import Path
from itertools import permutations

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
3. Options

0. Exit
""" in out


validMainOptionTestData = \
    [("1", "You selected option 1"),
     ("2", "You selected option 2"),
     ("3", "You selected option 3")]

invalidMainOptionTestData = \
    [("4", "Invalid option!"),
     ("10", "Invalid option!"),
     ("a", "Invalid option!"),
     ("abc", "Invalid option!")]


@pytest.mark.parametrize("option, expectedResult", validMainOptionTestData + invalidMainOptionTestData)
def test_validateMainOption(capfd, option, expectedResult):
    player_test.validateMain(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


def test_displayOptionMenu(capfd):
    player_test.displayOptionMenuHelper()
    out, _ = capfd.readouterr()
    assert """
SimpCity Game Options
---------------------
1. Choose Building Pool

0. Return to Main Menu
""" in out


validOptionMenuTestData = \
    [("0", "---- Back to Main Menu ----"),
     ("1", "You selected option 1")]

invalidOptionMenuTestData = \
    [("2", "Invalid option!"),
     ("3", "Invalid option!"),
     ("4", "Invalid option!"),
     ("5", "Invalid option!"),
     ("10", "Invalid option!")]


@pytest.mark.parametrize("option, expectedResult", validOptionMenuTestData + invalidOptionMenuTestData)
def test_validateOptionMenu(capfd, option, expectedResult):
    player_test.validateOptionMenu(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


def test_displayBuildingPoolOptionMenu(capfd):
    player_test.displayBuildingPoolOptionMenuHelper()
    out, _ = capfd.readouterr()
    assert """
Choose Building Pool
--------------------
1. Beach
2. Factory
3. Highway
4. House
5. Shop
6. Monument
7. Park 

0. Return to Option Menu
""" in out


def generateValidBuildingPoolOptions():
    A = map(str, list(range(1, 8)))

    validBuildingPoolOptions = []

    for perm in permutations(A, 5):
        validBuildingPoolOptions.append((",".join(perm), True))

    return validBuildingPoolOptions


invalidBuildingPoolOptions = [
    ("1,2,1,3,4", False),
    ("1,2,3,5,8", False),
    ("1,2,3,8,2", False),
    ("1,2,1,3,4", False),
    ("1,2,10,5,6", False),
    ("1,2,2,3,4", False),
    ("1,5,5,6,6", False),
]


@pytest.mark.parametrize("option, expectedResult", generateValidBuildingPoolOptions() + invalidBuildingPoolOptions)
def test_validateBuildingPoolOptions(option, expectedResult):
    result = player_test.isBuildingPoolOptionsValid(option)
    assert result == expectedResult


validBuildingPoolOptionMenuTestData = [
    ("0", "---- Back to Option Menu ----"),
    ("1,2,3,4,5", "Sucessfully updated building pool!"),
    ("1,2,4,5,7", "Sucessfully updated building pool!"),
    ("5,4,3,6,7", "Sucessfully updated building pool!"),
    ("1,4,5,6,7", "Sucessfully updated building pool!"),
]

invalidBuildingPoolOptionMenuTestData = [
    ("1,2,1,3,4", "Invalid option!"),
    ("1,2,3,5,8", "Invalid option!"),
    ("1,2,3,8,2", "Invalid option!"),
    ("1,2,1,3,4", "Invalid option!"),
    ("1,2,10,5,6", "Invalid option!"),
    ("1,2,2,3,4", "Invalid option!"),
    ("1,5,5,6,6", "Invalid option!"),
    ("2", "Invalid option!"),
    ("3", "Invalid option!"),
    ("5", "Invalid option!"),
    ("10", "Invalid option!"),
]


@pytest.mark.parametrize("option, expectedResult", validBuildingPoolOptionMenuTestData + invalidBuildingPoolOptionMenuTestData)
def test_validateBuildingPoolOptionMenu(capfd, option, expectedResult):
    player_test.validateBuildingPoolOptionMenu(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


updateBuildingPoolFromOptionTestData = [
    ("1,2,3,4,5", "Current Building Pool: BCH,FAC,HWY,HSE,SHP"),
    ("1,2,4,5,7", "Current Building Pool: BCH,FAC,HSE,SHP,PRK"),
    ("5,4,3,6,7", "Current Building Pool: SHP,HSE,HWY,MON,PRK"),
    ("1,4,5,6,7", "Current Building Pool: BCH,HSE,SHP,MON,PRK"),
    ("4,2,1,3,7", "Current Building Pool: HSE,FAC,BCH,HWY,PRK"),
    ("6,2,4,3,1", "Current Building Pool: MON,FAC,HSE,HWY,BCH"),
    ("7,4,3,1,5", "Current Building Pool: PRK,HSE,HWY,BCH,SHP"),
    ("1,5,4,2,7", "Current Building Pool: BCH,SHP,HSE,FAC,PRK"),
    ("4,2,7,1,3", "Current Building Pool: HSE,FAC,PRK,BCH,HWY"),
    ("6,4,5,2,7", "Current Building Pool: MON,HSE,SHP,FAC,PRK"),
]


@pytest.mark.parametrize("option, expectedResult", updateBuildingPoolFromOptionTestData)
def test_updateBuildingPoolFromOption(capfd, option, expectedResult):
    player = Player()
    player.updateBuildingPoolFromOption(option)
    player.displayCurrentBuildingPool()
    out, _ = capfd.readouterr()
    assert expectedResult in out

# Test the display of a empty grid


# def test_displayGrid(capfd):
#     player_test.displayGrid()
#     out, _ = capfd.readouterr()
#     assert """
#     A     B     C     D
#  +-----+-----+-----+-----+
# 1|     |     |     |     |
#  +-----+-----+-----+-----+
# 2|     |     |     |     |
#  +-----+-----+-----+-----+
# 3|     |     |     |     |
#  +-----+-----+-----+-----+
# 4|     |     |     |     |
#  +-----+-----+-----+-----+
# """ in out


exitGameTestData = \
    [("0", "---- Game Ended ----")]


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
     #  ("1", "Build Where? "),
     #  ("2", "Build Where? "),
     ("3", "You selected option 3"),
     ("4", "You selected option 4")]


@pytest.mark.parametrize("option, expectedResult", validGameOptionTestData)
def test_validGameOption(capfd, option, expectedResult):
    player_test.validateGame(option)
    out, _ = capfd.readouterr()
    assert expectedResult in out


invalidGameOptionTestData = \
    [("5", "Invalid option!"),
     ("6", "Invalid option!"),
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

    assert len(shuffled_buildings) >= 2


def test_retriveTwoRandomBuildings():
    two_random_buildings = player_test.retrieveTwoRandomBuildings()

    assert len(two_random_buildings) == 2


def generateRandomBuildingsMenuContent():
    gameMenuContentTestData = []

    for _ in range(10):
        firstBuilding, secondBuilding = player_test.retrieveTwoRandomBuildings()
        gameMenuContentTestData.append(
            ((firstBuilding, secondBuilding), player_test.gameMenuContent(firstBuilding, secondBuilding)))

    return gameMenuContentTestData


@pytest.mark.parametrize("option, expectedResult", generateRandomBuildingsMenuContent())
def test_displayGameMenuWithTwoRandomBuildings(capfd, option, expectedResult):
    firstBuilding, secondBuilding = option
    player_test.displayGameMenu(firstBuilding, secondBuilding)
    out, _ = capfd.readouterr()
    assert expectedResult in out


def test_availableBuildings():
    # Each Buildings be less than 0, more than 8
    # Total Buildings cannot be less than 24, more than 40

    for i in player_test.grid.availableBuildings.availability:
        assert i in range(0, 9)

    assert sum(player_test.grid.availableBuildings.availability) in range(24, 41)
