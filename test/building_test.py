from models.buildings import *
from models.enums import *
from models.grid import *
import pytest


beachBuildingTestData = [
    ((0, 0), 3),
    ((0, 1), 1),
    ((0, 2), 1),
    ((0, 3), 3),
    ((1, 0), 3),
    ((1, 1), 1),
    ((1, 2), 1),
    ((1, 3), 3),
    ((2, 0), 3),
    ((2, 1), 1),
    ((2, 2), 1),
    ((2, 3), 3),
    ((3, 0), 3),
    ((3, 1), 1),
    ((3, 2), 1),
    ((3, 3), 3),
]


@pytest.mark.parametrize("option, expectedResult", beachBuildingTestData)
def test_calculateBeachBuildingScore(option, expectedResult):
    gridObject = Grid()
    x, y = option

    beachBuilding = gridObject.createBuilding(Buildings.BEACH.value, x, y)
    assert beachBuilding.retrieveBuildingScore() == expectedResult
