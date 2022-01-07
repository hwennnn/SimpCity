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


parkBuildingTestData = [
    (
        [
            (0, 0, Buildings.PARK.value)
        ],
        1
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        2
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        3
    ),
    (
        # 2-square Park Building
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        3
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
        ],
        4
    ),
    (
        # 3-square Park Building
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 0, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
        ],
        8
    ),
]


@pytest.mark.parametrize("buildingPositions, expectedResult", parkBuildingTestData)
def test_calculateParkBuildingScore(buildingPositions, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    assert gridObject.calculateParkBuildingsScore() == expectedResult
