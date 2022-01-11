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

    assert gridObject.grid[dx][dy].retrieveBuildingScore(
        gridObject.grid) == expectedResult


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

    scores, _ = gridObject.calculateFactoryBuildingsScore()

    assert scores == expectedResult


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

    assert gridObject.grid[dx][dy].retrieveBuildingScore(
        gridObject.grid) == expectedResult


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

    assert gridObject.grid[dx][dy].retrieveBuildingScore(
        gridObject.grid) == expectedResult


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
        # One 1-Square Park
    ),
    (
        [
            (1, 1, Buildings.PARK.value)
        ],
        1
        # One 1-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        2
        # Two 1-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
        ],
        3
        # Three 1-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
            (3, 3, Buildings.PARK.value),
        ],
        4
        # Four 1-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
        ],
        3
        # One 2-Square Park
    ),
    (
        [
            (2, 1, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
        ],
        3
        # One 2-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (2, 0, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
        ],
        6
        # Two 2-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
            (3, 1, Buildings.PARK.value),
        ],
        9
        # Three 2-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
            (3, 1, Buildings.PARK.value),
            (2, 3, Buildings.PARK.value),
            (3, 3, Buildings.PARK.value),
        ],
        12
        # Four 2-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        8
        # One 3-Square Park
    ),
    (
        [
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
        ],
        8
        # One 3-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (2, 0, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
        ],
        16
        # Two 3-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
        ],
        16
        # One 4-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
        ],
        16
        # One 4-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (2, 2, Buildings.PARK.value),
            (2, 3, Buildings.PARK.value),
            (3, 2, Buildings.PARK.value),
            (3, 3, Buildings.PARK.value),
        ],
        32
        # Two 4-Square Park (As they are not horizontally or vertically connected)
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
        ],
        22
        # One 5-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
        ],
        23
        # One 6-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 0, Buildings.PARK.value),
        ],
        24
        # One 7-Square Park
    ),
    (
        [
            (0, 0, Buildings.PARK.value),
            (0, 1, Buildings.PARK.value),
            (0, 2, Buildings.PARK.value),
            (1, 0, Buildings.PARK.value),
            (1, 1, Buildings.PARK.value),
            (1, 2, Buildings.PARK.value),
            (2, 0, Buildings.PARK.value),
            (2, 1, Buildings.PARK.value),
        ],
        25
        # One 8-Square Park
    ),
]


@pytest.mark.parametrize("buildingPositions, expectedResult", parkBuildingTestData)
def test_calculateParkBuildingScore(buildingPositions, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    scores, _ = gridObject.calculateParkBuildingsScore()
    assert scores == expectedResult


monumentBuildingTestData = [
    (
        [
            (0, 1, Buildings.MONUMENT.value)
        ],
        1
    ),
    (
        [
            (0, 1, Buildings.MONUMENT.value),
            (2, 2, Buildings.MONUMENT.value)
        ],
        2
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value)  # corner
        ],
        2
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value),  # corner
            (1, 1, Buildings.MONUMENT.value),
        ],
        3
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value),  # corner
            (0, 3, Buildings.MONUMENT.value),  # corner
        ],
        4
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value),  # corner
            (0, 3, Buildings.MONUMENT.value),  # corner
            (3, 0, Buildings.MONUMENT.value),  # corner
        ],
        12
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value),  # corner
            (0, 3, Buildings.MONUMENT.value),  # corner
            (3, 0, Buildings.MONUMENT.value),  # corner
            (1, 1, Buildings.MONUMENT.value),
        ],
        16
    ),
    (
        [
            (0, 0, Buildings.MONUMENT.value),  # corner
            (0, 3, Buildings.MONUMENT.value),  # corner
            (3, 0, Buildings.MONUMENT.value),  # corner
            (3, 3, Buildings.MONUMENT.value),  # corner
        ],
        16
    ),
]


@pytest.mark.parametrize("buildingPositions, expectedResult", monumentBuildingTestData)
def test_calculateMonumentBuildingScore(buildingPositions, expectedResult):
    gridObject = Grid()

    for x, y, buildingName in buildingPositions:
        gridObject.updateGrid(x, y, buildingName)

    scores, _ = gridObject.retrieveBuildingsScore()
    assert scores == expectedResult
