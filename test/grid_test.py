# Unit Test Only
import pytest
from models.player import Player

player_test = Player()

validXPositions = [
    ("a", True),
    ("b", True),
    ("c", True),
    ("d", True),
    ("A", True),
    ("B", True),
    ("C", True),
    ("D", True),
]

invalidXPositions = [
    ("e", False),
    ("f", False),
    ("g", False),
    ("h", False),
    ("z", False),
    ("1", False),
    ("2", False),
    ("3", False),
    ("10", False)
]


@pytest.mark.parametrize("userInput, expectedResult", validXPositions + invalidXPositions)
def test_isPositionXValid(userInput, expectedResult):
    result = player_test.grid.isPositionXValid(userInput)

    assert result == expectedResult


validYPositions = [
    ("1", True),
    ("2", True),
    ("3", True),
    ("4", True),
]

invalidYPositions = [
    ("5", False),
    ("6", False),
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


@pytest.mark.parametrize("userInput, expectedResult", validYPositions + invalidYPositions)
def test_isPositionYValid(userInput, expectedResult):
    result = player_test.grid.isPositionYValid(userInput)

    assert result == expectedResult


passingBuildingPositionsFromUserInput = [
    ("a1", True),
    ("a2", True),
    ("a3", True),
    ("a4", True),
    ("b1", True),
    ("b2", True),
    ("b3", True),
    ("b4", True),
    ("c1", True),
    ("c2", True),
    ("c3", True),
    ("c4", True),
    ("d1", True),
    ("d2", True),
    ("d3", True),
    ("d4", True),
    ("A1", True),
    ("A2", True),
    ("A3", True),
    ("A4", True),
    ("B1", True),
    ("B2", True),
    ("B3", True),
    ("B4", True),
    ("C1", True),
    ("C2", True),
    ("C3", True),
    ("C4", True),
    ("D1", True),
    ("D2", True),
    ("D3", True),
    ("D4", True),
]

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


@pytest.mark.parametrize("userInput, expectedResult", passingBuildingPositionsFromUserInput + failingBuildingPositionsFromUserInput)
def test_validBuildingPositionFromUserInputs(userInput, expectedResult):
    result = player_test.grid.isPositionValid(userInput)

    assert result == expectedResult


positionFromUserInput = [
    ("a1", (0, 0)),
    ("a2", (1, 0)),
    ("a3", (2, 0)),
    ("a4", (3, 0)),
    ("b1", (0, 1)),
    ("b2", (1, 1)),
    ("b3", (2, 1)),
    ("b4", (3, 1)),
    ("c1", (0, 2)),
    ("c2", (1, 2)),
    ("c3", (2, 2)),
    ("c4", (3, 2)),
    ("d1", (0, 3)),
    ("d2", (1, 3)),
    ("d3", (2, 3)),
    ("d4", (3, 3))
]


@pytest.mark.parametrize("userInput, expectedResult", positionFromUserInput)
def test_retrieveParsedPosition(userInput, expectedResult):
    result = player_test.grid.retrieveParsedPosition(userInput)

    assert result == expectedResult
