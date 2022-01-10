from models.buildings import *
from models.enums import *
from models.grid import *
import pytest


houseBuildingTestData = [
    (
        [
            (0, 0, Buildings.HOUSE.value),
            (0, 1, Buildings.HOUSE.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.HOUSE.value),
            (1, 0, Buildings.HOUSE.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.HOUSE.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.HOUSE.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (0, 1, Buildings.HOUSE.value),
            (0, 2, Buildings.HOUSE.value),
            (0, 0, Buildings.HOUSE.value),
            (1, 1, Buildings.HOUSE.value),
        ],
        (0, 1),
        3
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.HOUSE.value),
            (2, 1, Buildings.HOUSE.value),
            (1, 2, Buildings.HOUSE.value),
        ],
        (1, 1),
        4
    ),
    (
        [
            (0, 0, Buildings.HOUSE.value),
            (0, 1, Buildings.SHOP.value),
            (1, 0, Buildings.HOUSE.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.SHOP.value),
            (2, 1, Buildings.SHOP.value),
            (1, 2, Buildings.HOUSE.value),
        ],
        (1, 1),
        4
    ),
    (
        [
            (0, 1, Buildings.HOUSE.value),
            (0, 0, Buildings.BEACH.value),
            (1, 1, Buildings.SHOP.value),
            (0, 2, Buildings.HOUSE.value),
        ],
        (0, 1),
        4
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.HOUSE.value),
            (2, 1, Buildings.BEACH.value),
            (1, 2, Buildings.BEACH.value),
            (0, 1, Buildings.SHOP.value),
        ],
        (1, 1),
        6
    ),
    (
        [
            (0, 0, Buildings.HOUSE.value),
            (0, 1, Buildings.HIGHWAY.value),
            (1, 0, Buildings.HOUSE.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.HIGHWAY.value),
            (2, 1, Buildings.PARK.value),
            (1, 2, Buildings.MONUMENT.value),
            (0, 1, Buildings.HIGHWAY.value),
        ],
        (1, 1),
        0
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.FACTORY.value),
            (2, 1, Buildings.BEACH.value),
            (1, 2, Buildings.HOUSE.value),
            (0, 1, Buildings.SHOP.value),
        ],
        (1, 1),
        1
    ),
    (
        [
            (1, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.FACTORY.value),
            (2, 1, Buildings.FACTORY.value),
            (1, 2, Buildings.BEACH.value),
            (0, 1, Buildings.SHOP.value),
        ],
        (1, 1),
        1
    ),
    (
        [
            (1, 3, Buildings.HOUSE.value),
            (0, 3, Buildings.BEACH.value),
            (1, 2, Buildings.BEACH.value),
            (2, 3, Buildings.BEACH.value),
        ],
        (1, 3),
        6
    )
]


@pytest.mark.parametrize("buildingPositions, targetHouse, expectedResult", houseBuildingTestData)
def test_retrieveHouseBuildingScore(buildingPositions, targetHouse, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    dx, dy = targetHouse

    assert gridObject.grid[dx][dy].retrieveBuildingScore(gridObject.grid) == expectedResult