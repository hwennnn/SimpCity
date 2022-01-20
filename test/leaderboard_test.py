# Unit Test Only

from models.leaderboard import Leaderboard
from models.configurations import savedLeaderboardFilename
from pathlib import Path
import sys
import pytest
import os
path = str(Path(Path('leaderboard_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)


def test_checkIfLeaderboardFileExist():
    try:
        os.remove(savedLeaderboardFilename)
    except OSError:
        pass

    leaderboard = Leaderboard()

    assert leaderboard.isSavedLeaderboardExist() == False


validLeaderboardPlayerNameTestData = \
    [("glenn", True),
     ("hou man", True),
     ("yong teng", True),
     ("zachary", True),
     ("12345678901234567890", True),
     ]

invalidLeaderboardPlayerNameTestData = \
    [("", False),
     ("this is a very long sentence", False),
     ("123456789012345678901", False),
     ]


@pytest.mark.parametrize("option, expectedResult", validLeaderboardPlayerNameTestData + invalidLeaderboardPlayerNameTestData)
def test_validateMainOption(option, expectedResult):
    leaderboard = Leaderboard()

    assert leaderboard.isLeaderboardPlayerNameValid(option) == expectedResult


validSavedLeaderboardFileTestData = \
    [([
        "zachary, 69, 1642677335555",
        "hwen, 40, 1642677336958",
        "yong teng, 39, 1642677336951",
        "glenn, 20, 12381237872",
    ], True),
    ]

invalidSavedLeaderboardFileTestData = \
    [([
        "this is a very long sentence, 69, 1642677335555",
        "hwen, 40, 1642677336958",
        "yong teng, 39, 1642677336951",
        "glenn, 20, 12381237872",
    ], True),
    ]


@pytest.mark.parametrize("option, expectedResult", validSavedLeaderboardFileTestData + invalidSavedLeaderboardFileTestData)
def test_validateMainOption(option, expectedResult):
    leaderboard = Leaderboard()
    isValid, _ = leaderboard.isSavedLeaderboardFileValid(option)

    assert isValid == expectedResult


def test_saveScoreIntoLeaderboard():
    leaderboard = Leaderboard()

    for i in range(10):
        leaderboard.saveScoreIntoLeaderboard(i + 1, chr(ord('a') + i))

    assert len(leaderboard.leaderboard) == 10
    assert leaderboard.isSavedLeaderboardExist() == True

    newRanking = leaderboard.getRankingInLeaderBoard(30)

    assert newRanking == 0


def test_loadLeaderboardFromFile(capfd):
    leaderboard = Leaderboard()

    leaderboard.loadLeaderboardFromFile()

    out, _ = capfd.readouterr()

    assert "Successfully loaded the leaderboard!" in out


def test_readFiles():
    leaderboard = Leaderboard()

    assert len(leaderboard.readFiles()) == 10


def test_displayLeaderboard(capfd):
    leaderboard = Leaderboard()

    leaderboard.displayLeaderboard()

    out, _ = capfd.readouterr()

    assert "--------- HIGH SCORES ---------" in out
