# Unit Test Only
import pytest
from models.configurations import savedGameFilename
from models.player import Player
import os

player_test = Player()
player_test.grid.updateGridSize(6, 6)

validXPositions = [
    ("a", True),
    ("b", True),
    ("c", True),
    ("d", True),
    ("e", True),
    ("f", True),
    ("A", True),
    ("B", True),
    ("C", True),
    ("D", True),
    ("E", True),
    ("F", True)
]


@pytest.mark.parametrize("userInput, expectedResult", validXPositions)
def test_isPositionXValid_Pass(userInput, expectedResult):
    result = player_test.grid.isPositionXValid(userInput)

    assert result == expectedResult


invalidXPositions = [
    ("g", False),
    ("h", False),
    ("z", False),
    ("1", False),
    ("2", False),
    ("3", False),
    ("10", False)
]


@pytest.mark.parametrize("userInput, expectedResult", invalidXPositions)
def test_isPositionXValid_Failing(userInput, expectedResult):
    result = player_test.grid.isPositionXValid(userInput)

    assert result == expectedResult


validYPositions = [
    ("1", True),
    ("2", True),
    ("3", True),
    ("4", True),
    ("5", True),
    ("6", True)
]


@pytest.mark.parametrize("userInput, expectedResult", validYPositions)
def test_isPositionYValid_Pass(userInput, expectedResult):
    result = player_test.grid.isPositionYValid(userInput)

    assert result == expectedResult


invalidYPositions = [
    ("7", False),
    ("8", False),
    ("9", False),
    ("10", False),
    ("99", False),
    ("100", False),
    ("100000", False),
    ("abc", False),
    ("efg", False)
]


@pytest.mark.parametrize("userInput, expectedResult", invalidYPositions)
def test_isPositionYValid_Failing(userInput, expectedResult):
    result = player_test.grid.isPositionYValid(userInput)

    assert result == expectedResult


passingBuildingPositionsFromUserInput = [
    ("a1", True),
    ("a2", True),
    ("a3", True),
    ("a4", True),
    ("a5", True),
    ("a6", True),
    ("b1", True),
    ("b2", True),
    ("b3", True),
    ("b4", True),
    ("b5", True),
    ("b6", True),
    ("c1", True),
    ("c2", True),
    ("c3", True),
    ("c4", True),
    ("c5", True),
    ("c6", True),
    ("d1", True),
    ("d2", True),
    ("d3", True),
    ("d4", True),
    ("d5", True),
    ("d6", True),
    ("e1", True),
    ("e2", True),
    ("e3", True),
    ("e4", True),
    ("e5", True),
    ("e6", True),
    ("f1", True),
    ("f2", True),
    ("f3", True),
    ("f4", True),
    ("f5", True),
    ("f6", True),
    ("A1", True),
    ("A2", True),
    ("A3", True),
    ("A4", True),
    ("A5", True),
    ("A6", True),
    ("B1", True),
    ("B2", True),
    ("B3", True),
    ("B4", True),
    ("B5", True),
    ("B6", True),
    ("C1", True),
    ("C2", True),
    ("C3", True),
    ("C4", True),
    ("C5", True),
    ("C6", True),
    ("D1", True),
    ("D2", True),
    ("D3", True),
    ("D4", True),
    ("D5", True),
    ("D6", True),
    ("E1", True),
    ("E2", True),
    ("E3", True),
    ("E4", True),
    ("E5", True),
    ("E6", True),
    ("F1", True),
    ("F2", True),
    ("F3", True),
    ("F4", True),
    ("F5", True),
    ("F6", True)
]


@pytest.mark.parametrize("userInput, expectedResult", passingBuildingPositionsFromUserInput)
def test_validBuildingPositionFromUserInputs_Pass(userInput, expectedResult):
    result = player_test.grid.isPositionValid(userInput)

    assert result == expectedResult


failingBuildingPositionsFromUserInput = [
    ("a10", False),
    ("a11", False),
    ("a13", False),
    ("a", False),
    ("b", False),
    ("c", False),
    ("d", False),
    ("1", False),
    ("2", False),
    ("3", False),
    ("4", False),
    ("10", False),
    ("11", False),
    ("12", False),
    ("13", False),
    ("14", False),
    ("", False),
    (" ", False),
    ("   ", False),
    ("simpcity", False),
    ("devops", False),
    ("].", False),
]


@pytest.mark.parametrize("userInput, expectedResult", failingBuildingPositionsFromUserInput)
def test_validBuildingPositionFromUserInputs_Failing(userInput, expectedResult):
    result = player_test.grid.isPositionValid(userInput)

    assert result == expectedResult


positionFromUserInput = [
    ("a1", (0, 0)),
    ("a2", (1, 0)),
    ("a3", (2, 0)),
    ("a4", (3, 0)),
    ("a5", (4, 0)),
    ("a6", (5, 0)),
    ("b1", (0, 1)),
    ("b2", (1, 1)),
    ("b3", (2, 1)),
    ("b4", (3, 1)),
    ("b5", (4, 1)),
    ("b6", (5, 1)),
    ("c1", (0, 2)),
    ("c2", (1, 2)),
    ("c3", (2, 2)),
    ("c4", (3, 2)),
    ("c5", (4, 2)),
    ("c6", (5, 2)),
    ("d1", (0, 3)),
    ("d2", (1, 3)),
    ("d3", (2, 3)),
    ("d4", (3, 3)),
    ("d5", (4, 3)),
    ("d6", (5, 3)),
    ("e1", (0, 4)),
    ("e2", (1, 4)),
    ("e3", (2, 4)),
    ("e4", (3, 4)),
    ("e5", (4, 4)),
    ("e6", (5, 4)),
    ("f1", (0, 5)),
    ("f2", (1, 5)),
    ("f3", (2, 5)),
    ("f4", (3, 5)),
    ("f5", (4, 5)),
    ("f6", (5, 5))
]


@pytest.mark.parametrize("userInput, expectedResult", positionFromUserInput)
def test_retrieveParsedPosition_Pass(userInput, expectedResult):
    result = player_test.grid.retrieveParsedPosition(userInput)

    assert result == expectedResult


parsedXPosition = [
    ("A", 0),
    ("B", 1),
    ("C", 2),
    ("D", 3),
    ("E", 4),
    ("F", 5),
]


@pytest.mark.parametrize("userInput, expectedResult", parsedXPosition)
def test_parseXPositionInput_Pass(userInput, expectedResult):
    result = player_test.grid.parseXPositionInput(userInput)

    assert result == expectedResult


parsedYPosition = [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 5)
]


@pytest.mark.parametrize("userInput, expectedResult", parsedYPosition)
def test_parseYPositionInput_Pass(userInput, expectedResult):
    result = player_test.grid.parseYPositionInput(userInput)

    assert result == expectedResult


validGridSizes = [
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 6),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5),
    (5, 6),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (6, 6)
]


@pytest.mark.parametrize("gridSize", validGridSizes)
def test_updateGridSize_Pass(gridSize):
    player = Player()
    x, y = gridSize
    player.grid.updateGridSize(x, y)

    assert player.grid.colCount == y and player.grid.rowCount == x


def test_grid2RowDisplay2Col(capfd):
    player = Player()
    player.grid.updateGridSize(2, 2)
    player.grid.displayGrid()
    out, _ = capfd.readouterr()
    assert "\t\t HWY: 8" in out


def test_grid2RowDisplay6Col(capfd):
    player = Player()
    player.grid.updateGridSize(2, 6)
    player.grid.displayGrid()
    out, _ = capfd.readouterr()
    assert "\t\t\t\t\t HWY: 8" in out


def test_gridMoreThan2RowDisplay(capfd):
    player = Player()
    player.displayGrid()
    out, _ = capfd.readouterr()
    assert "3 |     |     |     |     |\t HWY: 8" in out


def test_gridMonumentDisplay(capfd):
    player = Player()
    player.grid.updateGrid(0, 0, "MON")
    player.displayGrid()
    out, _ = capfd.readouterr()
    assert "1 | MON |     |     |     |\t BCH: 8" in out


def test_gridHouseDisplay(capfd):
    player = Player()
    player.grid.updateGrid(0, 2, "PRK")
    player.displayGrid()
    out, _ = capfd.readouterr()
    assert "1 |     |     | PRK |     |\t BCH: 8" in out


validGrids = [
    (["*2\n","(4,4)\n","1,2,3,4,5\n" ,"None,None,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], True),
    (["*2\n","(4,4)\n","1,2,3,4,5\n","BCH,None,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], True)
]


@pytest.mark.parametrize("gridlines, expectedResult", validGrids)
def test_validateSaveFile_Pass(gridlines, expectedResult):
    player = Player()
    isFileValid, _ = player.grid.isSavedGameFileValid(gridlines)
    assert expectedResult == isFileValid


invalidGrids = [
    (["*2\n","(4,4)\n","1,2,3,4,5\n","B,None,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], False),
    (["*2\n","(4,4)\n","1,2,3,4,5\n","BCH,KKK,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], False),
    (["*2\n","(0,4)\n","1,2,3,4,5\n","BCH,None,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], False),
    (["*2\n","(4,0)\n","1,2,3,4,5\n","BCH,None,None,None\n"
    ,"None,None,None,None\n","None,None,None,None\n","None,None,None,None\n"], False)
]


@pytest.mark.parametrize("gridlines, expectedResult",  invalidGrids)
def test_validateSaveFile_Failing(gridlines, expectedResult):
    player = Player()
    isFileValid, _ = player.grid.isSavedGameFileValid(gridlines)
    assert expectedResult == isFileValid
