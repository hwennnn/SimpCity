# Unit Test Only

from models.leaderboard import Leaderboard
from models.configurations import savedLeaderboardFilename
from pathlib import Path
import sys
import pytest
import os
path = str(Path(Path('leaderboard_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

# configurations used in the unit tests
rowCount = colCount = 4


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


@pytest.mark.parametrize("option, expectedResult", validLeaderboardPlayerNameTestData)
def test_checkIsLeaderboardPlayerNameValid_Pass(option, expectedResult):
    leaderboard = Leaderboard()

    assert leaderboard.isLeaderboardPlayerNameValid(option) == expectedResult


invalidLeaderboardPlayerNameTestData = \
    [("", False),
     ("this is a very long sentence", False),
     ("123456789012345678901", False),
     ]


@pytest.mark.parametrize("option, expectedResult", invalidLeaderboardPlayerNameTestData)
def test_checkIsLeaderboardPlayerNameValid_Failing(option, expectedResult):
    leaderboard = Leaderboard()

    assert leaderboard.isLeaderboardPlayerNameValid(option) == expectedResult


validSavedLeaderboardFileTestData = \
    [
        ([
            "# 4, 4",
            "zachary, 70, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
            "glenn, 20, 12381237872",
        ], True),
    ]


@pytest.mark.parametrize("option, expectedResult", validSavedLeaderboardFileTestData)
def test_checkIsSavedLeaderboardFileValid_Pass(option, expectedResult):
    leaderboard = Leaderboard()
    isValid, _ = leaderboard.isSavedLeaderboardFileValid(option)

    assert isValid == expectedResult


invalidSavedLeaderboardFileTestData = \
    [
        ([
            "# 4, 4",
            "this is a very long sentence!!!!!, 70, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
            "glenn, 20, 12381237872",
        ], False),
        ([
            # failed because exceed 10 lines for leaderboard data
            "# 4, 4",
            "zachary, 69, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
            "glenn, 20, 12381237872",
            "zachary, 69, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
            "glenn, 20, 12381237872",
            "zachary, 69, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
        ], False),
        ([
            # failed because without indicating grid size
            "zachary, 70, 1642677335555",
            "hwen, 40, 1642677336958",
            "yong teng, 39, 1642677336951",
            "glenn, 20, 12381237872",
        ], False),
    ]


@pytest.mark.parametrize("option, expectedResult", invalidSavedLeaderboardFileTestData)
def test_checkIsSavedLeaderboardFileValid_Failing(option, expectedResult):
    leaderboard = Leaderboard()
    isValid, _ = leaderboard.isSavedLeaderboardFileValid(option)

    assert isValid == expectedResult


def test_saveScoreIntoLeaderboard():
    leaderboard = Leaderboard()

    for i in range(10):
        leaderboard.saveScoreIntoLeaderboard(
            i + 1, rowCount, colCount, chr(ord('a') + i))

    assert len(leaderboard.leaderboard[rowCount][colCount]) == 10
    assert leaderboard.isSavedLeaderboardExist() == True

    newRanking = leaderboard.getRankingInLeaderBoard(30, rowCount, colCount)
    assert newRanking == 0

    leaderboard.saveScoreIntoLeaderboard(30, rowCount, colCount, "hwen")


def test_loadLeaderboardFromFile(capfd):
    leaderboard = Leaderboard()

    leaderboard.loadLeaderboardFromFile()

    out, _ = capfd.readouterr()

    assert len(leaderboard.leaderboard) > 0


def test_readFiles():
    leaderboard = Leaderboard()

    # 10 leaderboard data including one header
    assert len(leaderboard.readFiles()) == 11


def test_displayLeaderboard(capfd):
    leaderboard = Leaderboard()

    leaderboard.displayLeaderboard(rowCount, colCount)

    out, _ = capfd.readouterr()

    assert "\n--------- HIGH SCORES ---------" in out


def test_failToSaveScoreIntoLeaderBoard(capfd):
    leaderboard = Leaderboard()

    leaderboard.saveScoreIntoLeaderboard(0, rowCount, colCount)

    out, _ = capfd.readouterr()

    assert "Sorry! You didn't make it to top 10 in the leaderboard!" in out
