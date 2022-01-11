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


factoryBuildingTestData = [
    (
        [
            (0, 0, Buildings.FACTORY.value)
        ],
        1
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
        ],
        4
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
        ],
        9
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
            (0, 3, Buildings.FACTORY.value),
        ],
        16
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
            (0, 3, Buildings.FACTORY.value),
            (1, 0, Buildings.FACTORY.value),
        ],
        17
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
            (0, 3, Buildings.FACTORY.value),
            (1, 0, Buildings.FACTORY.value),
            (1, 1, Buildings.FACTORY.value),
        ],
        18
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
            (0, 3, Buildings.FACTORY.value),
            (1, 0, Buildings.FACTORY.value),
            (1, 1, Buildings.FACTORY.value),
            (3, 3, Buildings.FACTORY.value),
        ],
        19
    ),
    (
        [
            (0, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.FACTORY.value),
            (0, 3, Buildings.FACTORY.value),
            (1, 0, Buildings.FACTORY.value),
            (1, 1, Buildings.FACTORY.value),
            (3, 3, Buildings.FACTORY.value),
            (3, 0, Buildings.FACTORY.value),
        ],
        20
    ),
]


@pytest.mark.parametrize("buildingPositions, expectedResult", factoryBuildingTestData)
def test_calculateFactoryBuildingScore(buildingPositions, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    assert gridObject.calculateFactoryBuildingsScore() == expectedResult


shopBuildingTestData = [
    (
        [
            (0, 0, Buildings.SHOP.value)
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.SHOP.value),
            (0, 1, Buildings.SHOP.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.SHOP.value),
            (0, 1, Buildings.SHOP.value),
            (1, 0, Buildings.SHOP.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.SHOP.value),
            (0, 1, Buildings.SHOP.value),
            (1, 0, Buildings.FACTORY.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (0, 0, Buildings.SHOP.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.FACTORY.value),
        ],
        (0, 0),
        3
    ),
    (
        [
            (0, 0, Buildings.SHOP.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 0, Buildings.HOUSE.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (0, 1, Buildings.SHOP.value),
            (0, 0, Buildings.HOUSE.value),
            (1, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.SHOP.value),
        ],
        (0, 1),
        3
    ),
    (
        [
            (0, 1, Buildings.SHOP.value),
            (0, 0, Buildings.HOUSE.value),
            (1, 1, Buildings.FACTORY.value),
            (0, 2, Buildings.PARK.value),
        ],
        (0, 1),
        4
    ),
    (
        [
            (0, 1, Buildings.SHOP.value),
            (0, 0, Buildings.SHOP.value),
            (1, 1, Buildings.SHOP.value),
            (0, 2, Buildings.SHOP.value),
        ],
        (0, 1),
        1
    ),
    (
        [
            (1, 1, Buildings.SHOP.value),
            (1, 0, Buildings.SHOP.value),
            (0, 1, Buildings.SHOP.value),
            (1, 2, Buildings.SHOP.value),
            (2, 1, Buildings.FACTORY.value),
        ],
        (1, 1),
        2
    ),
    (
        [
            (1, 1, Buildings.SHOP.value),
            (1, 0, Buildings.FACTORY.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 2, Buildings.HOUSE.value),
            (2, 1, Buildings.FACTORY.value),
        ],
        (1, 1),
        3
    ),
    (
        [
            (1, 1, Buildings.SHOP.value),
            (1, 0, Buildings.HIGHWAY.value),
            (0, 1, Buildings.HOUSE.value),
            (1, 2, Buildings.MONUMENT.value),
            (2, 1, Buildings.FACTORY.value),
        ],
        (1, 1),
        5
    ),
    (
        [
            (1, 1, Buildings.SHOP.value),
            (1, 0, Buildings.SHOP.value),
            (0, 1, Buildings.SHOP.value),
            (1, 2, Buildings.SHOP.value),
            (2, 1, Buildings.SHOP.value),
        ],
        (1, 1),
        1
    ),
    (
        [
            (1, 1, Buildings.SHOP.value),
            (1, 0, Buildings.SHOP.value),
            (0, 1, Buildings.MONUMENT.value),
            (1, 2, Buildings.BEACH.value),
            (2, 1, Buildings.FACTORY.value),
        ],
        (1, 1),
        4
    )
]


@pytest.mark.parametrize("buildingPositions, targetShop, expectedResult", shopBuildingTestData)
def test_retrieveShopBuildingScore(buildingPositions, targetShop, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    dx, dy = targetShop

    assert gridObject.grid[dx][dy].retrieveBuildingScore(gridObject.grid) == expectedResult


highwayBuildingTestData = [
    (
        [
            (0, 0, Buildings.HIGHWAY.value)
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.HIGHWAY.value),
            (0, 1, Buildings.HIGHWAY.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (0, 0, Buildings.HIGHWAY.value),
            (0, 1, Buildings.HIGHWAY.value),
            (0, 2, Buildings.HIGHWAY.value),
        ],
        (0, 0),
        3
    ),
    (
        [
            (0, 0, Buildings.HIGHWAY.value),
            (0, 1, Buildings.HIGHWAY.value),
            (0, 2, Buildings.HIGHWAY.value),
            (0, 3, Buildings.HIGHWAY.value),
        ],
        (0, 0),
        4
    ),
    (
        [
            (0, 0, Buildings.HIGHWAY.value),
            (0, 2, Buildings.HIGHWAY.value),
        ],
        (0, 0),
        1
    ),
    (
        [
            (0, 0, Buildings.HIGHWAY.value),
            (0, 1, Buildings.HIGHWAY.value),
            (0, 3, Buildings.HIGHWAY.value),
        ],
        (0, 0),
        2
    ),
    (
        [
            (3, 3, Buildings.HIGHWAY.value),
            (3, 2, Buildings.HIGHWAY.value),
        ],
        (3, 3),
        2
    ),
    (
        [
            (3, 3, Buildings.HIGHWAY.value),
            (3, 2, Buildings.HIGHWAY.value),
            (3, 1, Buildings.HIGHWAY.value),
        ],
        (3, 3),
        3
    ),
    (
        [
            (3, 3, Buildings.HIGHWAY.value),
            (3, 2, Buildings.HIGHWAY.value),
            (3, 0, Buildings.HIGHWAY.value),
        ],
        (3, 2),
        2
    ),
    (
        [
            (2, 3, Buildings.HIGHWAY.value),
            (2, 2, Buildings.HIGHWAY.value),
            (2, 1, Buildings.HIGHWAY.value),
        ],
        (2, 2),
        3
    ),
    (
        [
            (2, 3, Buildings.HIGHWAY.value),
            (2, 2, Buildings.HIGHWAY.value),
            (2, 1, Buildings.HIGHWAY.value),
            (2, 0, Buildings.HIGHWAY.value),
        ],
        (2, 2),
        4
    ),
    (
        [
            (2, 3, Buildings.HIGHWAY.value),
            (2, 2, Buildings.HIGHWAY.value),
            (2, 1, Buildings.HIGHWAY.value),
            (2, 0, Buildings.BEACH.value),
        ],
        (2, 2),
        3
    ),
    (
        [
            (2, 3, Buildings.HIGHWAY.value),
            (2, 2, Buildings.HIGHWAY.value),
            (2, 1, Buildings.HOUSE.value),
            (2, 0, Buildings.HIGHWAY.value),
        ],
        (2, 2),
        2
    ),
    (
        [
            (2, 2, Buildings.HIGHWAY.value)
        ],
        (2, 2),
        1
    )
]


@pytest.mark.parametrize("buildingPositions, targetHighway, expectedResult", highwayBuildingTestData)
def test_retrieveHighwayBuildingScore(buildingPositions, targetHighway, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    dx, dy = targetHighway

    assert gridObject.grid[dx][dy].retrieveBuildingScore(gridObject.grid) == expectedResult