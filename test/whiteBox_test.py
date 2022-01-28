# White-box Integration Test
from models.player import Player
from models.game import Game
from models.enums import Buildings
from models.configurations import *
import random
import os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
currentDirectory = Path(dir_path)


def parse_fileToList(f):
    temp = ''
    row = []
    grid = []
    for i in f:
        if i == ',':
            row.append(temp)    # Add a coordinate to a row
            temp = ''
            # Ignore ',' and not append (it will be 'None,' if not included)
            continue

        if i == '\n':
            # Add the last coordinate for the row as it has '\n' instead of ','
            row.append(temp)
            grid.append(row)    # Add the row into a list to form a grid
            row = []
            temp = ''

        else:
            temp += i
    return grid


def saveGridToTextUnderTest(grid):
    # Test saving the current grid (on test) on a separate text file
    gridValue = grid.parseGridAsString()
    with open('testing.txt', 'w+') as f:
        for row in gridValue:
            f.writelines(row + "\n")

    # Test if the program saved the correct coordinates
    f = open("testing.txt", "r")
    f = f.read()
    return f


# Features Under Test
# 1) Building Placement
# Test if all the coordinates in the grid is fillable with buildings. Scaleable to grid size.
def test_fillGridWithBuildings(monkeypatch, capfd):
    player = Player()

    row = player.grid.rowCount
    col = player.grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 0
    tempList = []
    for i in range(0, total):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[
                            (random.randint(0, 1))], rowCounter, colCounter])

        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A.
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[
                            (random.randint(0, 1))], rowCounter, colCounter])

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1

    for i in tempList:
        # Place building
        player.grid.updateGrid(i[1], i[2], i[0])
        assert player.grid.grid[i[1]][i[2]] is not None

# Features Under Test
# 1) Placing Building
# 2) Saving Grid
# Test if the above features can be integrated together


def test_placeAndSave(monkeypatch, capfd):
    player = Player()

    row = player.grid.rowCount
    col = player.grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 0
    tempList = []

    # Halved for testing purposes. a full grid will not be viable as end of game action will kicks in when loaded
    for i in range(0, round(total / 2)):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[
                            (random.randint(0, 1))], rowCounter, colCounter])

        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A.
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[
                            (random.randint(0, 1))], rowCounter, colCounter])

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1

    for i in tempList:
        # Place building
        player.grid.updateGrid(i[1], i[2], i[0])
        # Check if the coordinate where the building is supposed to be place is empty or not
        assert player.grid.grid[i[1]][i[2]] is not None

    # Passing in the state of the current grid to save
    saveGridToTextUnderTest(player.grid)
    rootDirWithFile = currentDirectory.joinpath("testing.txt")
    assert rootDirWithFile.exists() == True

# Features Under Test
# 1) City Size
# 2) Building Pool
# 3) Start Game
# Test if the above features can be integrated together


def test_citySizeBuildingPoolAndStartGame(monkeypatch, capfd):
    player = Player()
    # Add City Size Logic
    player.grid.availableBuildings.updateBuildingPool("1,2,3,6,7")
    player.grid.availableBuildings.displayCurrentBuildingPool()
    out, _ = capfd.readouterr()
    assert "Current Building Pool: BCH,FAC,HWY,MON,PRK" in out
    # When game starts, turn = 1
    assert player.turns == 1

# Features Under Test
# 1) Building Pool
# 2) Remaining Buildings
# 3) Remaining Buildings Count
# Test if the above features can be integrated together


def test_buildingPoolAndRemainingBuildingCount(monkeypatch, capfd):
    player = Player()
    # Selects Beach, Factory, Highway, Monument and Park as part of the building pool.
    player.grid.availableBuildings.updateBuildingPool("1,2,3,6,7")
    print(player.grid.availableBuildings.buildings)
    out, _ = capfd.readouterr()
    # Check if current building pool is those of selected.
    assert "['BCH', 'FAC', 'HWY', 'MON', 'PRK']" in out

    monkeypatch.setattr('builtins.input', lambda _: "A1")
    # Place Park on A1.
    positions = player.promptEnterBuildingPosition("PRK")
    player.validatePlaceBuildingOnPosition("PRK", positions)
    print(player.grid.availableBuildings.availability)
    out, _ = capfd.readouterr()
    # Checks if Park's building count is deducted by 1.
    assert "[8, 8, 8, 8, 7]" in out


def test_whiteBox_flow1(capfd):

    # delete saved leaderboard file generated by other testing before
    try:
        os.remove(savedLeaderboardFilename)
    except OSError:
        pass

    game = Game()

    # Current grid size is 4x4
    # Current Building Pool: BCH,FAC,HSE,SHP,HWY

    # 1. Place Beach on A1
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "A1")

    out, _ = capfd.readouterr()

    assert "Placing BCH at A1..." in out

    # Check if the grid position at (0, 0) has a Beach building now
    assert game.player.grid.grid[0][0].getName() == Buildings.BEACH.value
    assert game.player.turns == 2
    assert game.player.retrieveBuildingsScore() == 3

    # 2. Place Factory on A2
    game.player.validatePlaceBuildingOnPosition(Buildings.FACTORY.value, "A2")

    out, _ = capfd.readouterr()

    assert "Placing FAC at A2..." in out

    # Check if the grid position at (1, 0) has a Factory building now
    assert game.player.grid.grid[1][0].getName() == Buildings.FACTORY.value
    assert game.player.turns == 3
    assert game.player.retrieveBuildingsScore() == 4

    # 3. Place Beach on A1 (Invalid Position)
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "D1")

    out, _ = capfd.readouterr()

    assert "Placing BCH at D1 was unsuccessful." in out
    assert "D1 is an invalid position! You must build next to an existing building." in out
    assert game.player.turns == 3
    assert game.player.retrieveBuildingsScore() == 4

    # 4. Place House on A3
    game.player.validatePlaceBuildingOnPosition(Buildings.HOUSE.value, "A3")

    out, _ = capfd.readouterr()

    assert "Placing HSE at A3..." in out

    # Check if the grid position at (2, 0) has a House building now
    assert game.player.grid.grid[2][0].getName() == Buildings.HOUSE.value
    assert game.player.turns == 4
    assert game.player.retrieveBuildingsScore() == 5

    # 5. Place Shop on B1
    game.player.validatePlaceBuildingOnPosition(Buildings.SHOP.value, "B1")

    out, _ = capfd.readouterr()

    assert "Placing SHP at B1..." in out

    # Check if the grid position at (0, 1) has a Shop building now
    assert game.player.grid.grid[0][1].getName() == Buildings.SHOP.value
    assert game.player.turns == 5
    assert game.player.retrieveBuildingsScore() == 7

    # 6. Place Highway on B2
    game.player.validatePlaceBuildingOnPosition(Buildings.HIGHWAY.value, "B2")

    out, _ = capfd.readouterr()

    assert "Placing HWY at B2..." in out

    # Check if the grid position at (1, 1) has a Highway building now
    assert game.player.grid.grid[1][1].getName() == Buildings.HIGHWAY.value
    assert game.player.turns == 6
    assert game.player.retrieveBuildingsScore() == 9

    # 7. Place BEACH on C1
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "C1")

    out, _ = capfd.readouterr()

    assert "Placing BCH at C1..." in out

    # Check if the grid position at (0, 2) has a Beach Building now
    assert game.player.grid.grid[0][2].getName() == Buildings.BEACH.value
    assert game.player.turns == 7
    assert game.player.retrieveBuildingsScore() == 10

    # 8. Place HOUSE on C2
    game.player.validatePlaceBuildingOnPosition(Buildings.HOUSE.value, "C2")

    out, _ = capfd.readouterr()

    assert "Placing HSE at C2..." in out

    # Check if the grid position at (1, 2) has a House building now
    assert game.player.grid.grid[1][2].getName() == Buildings.HOUSE.value
    assert game.player.turns == 8
    assert game.player.retrieveBuildingsScore() == 12

    # 9. Place FACTORY on C3
    game.player.validatePlaceBuildingOnPosition(Buildings.FACTORY.value, "C3")

    out, _ = capfd.readouterr()

    assert "Placing FAC at C3..." in out

    # Check if the grid position at (2, 2) has a Factory building now
    assert game.player.grid.grid[2][2].getName() == Buildings.FACTORY.value
    assert game.player.turns == 9
    assert game.player.retrieveBuildingsScore() == 14

    # 10. Place HIGHWAY on B3
    game.player.validatePlaceBuildingOnPosition(Buildings.HIGHWAY.value, "B3")

    out, _ = capfd.readouterr()

    assert "Placing HWY at B3..." in out

    # Check if the grid position at (2, 1) has a Highway building now
    assert game.player.grid.grid[2][1].getName() == Buildings.HIGHWAY.value
    assert game.player.turns == 10
    assert game.player.retrieveBuildingsScore() == 15

    # 11. Place FACTORY on D1
    game.player.validatePlaceBuildingOnPosition(Buildings.FACTORY.value, "D1")

    out, _ = capfd.readouterr()

    assert "Placing FAC at D1..." in out

    # Check if the grid position at (0, 3) has a Factory building now
    assert game.player.grid.grid[0][3].getName() == Buildings.FACTORY.value
    assert game.player.turns == 11
    assert game.player.retrieveBuildingsScore() == 20

    # 12. Place BEACH on D2
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "D2")

    out, _ = capfd.readouterr()

    assert "Placing BCH at D2..." in out

    # Check if the grid position at (1, 3) has a Beach building now
    assert game.player.grid.grid[1][3].getName() == Buildings.BEACH.value
    assert game.player.turns == 12
    assert game.player.retrieveBuildingsScore() == 23

    # 13. Place SHP on D3
    game.player.validatePlaceBuildingOnPosition(Buildings.SHOP.value, "D3")

    out, _ = capfd.readouterr()

    assert "Placing SHP at D3..." in out

    # Check if the grid position at (2, 3) has a Shop building now
    assert game.player.grid.grid[2][3].getName() == Buildings.SHOP.value
    assert game.player.turns == 13
    assert game.player.retrieveBuildingsScore() == 26

    # 14. Place HWY on A4
    game.player.validatePlaceBuildingOnPosition(Buildings.HIGHWAY.value, "A4")

    out, _ = capfd.readouterr()

    assert "Placing HWY at A4..." in out

    # Check if the grid position at (3, 9) has a Highway building now
    assert game.player.grid.grid[3][0].getName() == Buildings.HIGHWAY.value
    assert game.player.turns == 14
    assert game.player.retrieveBuildingsScore() == 27

    # 15. Place HOUSE on B4
    game.player.validatePlaceBuildingOnPosition(Buildings.HOUSE.value, "B4")

    out, _ = capfd.readouterr()

    assert "Placing HSE at B4..." in out

    # Check if the grid position at (3, 1) has a House building now
    assert game.player.grid.grid[3][1].getName() == Buildings.HOUSE.value
    assert game.player.turns == 15
    assert game.player.retrieveBuildingsScore() == 27

    # 16. Place BEACH on C4
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "C4")

    out, _ = capfd.readouterr()

    assert "Placing BCH at C4..." in out

    # Check if the grid position at (3, 2) has a House building now
    assert game.player.grid.grid[3][2].getName() == Buildings.BEACH.value
    assert game.player.turns == 16
    assert game.player.retrieveBuildingsScore() == 30

    # 17. Place FACTORY on D4
    game.player.validatePlaceBuildingOnPosition(Buildings.FACTORY.value, "D4")

    out, _ = capfd.readouterr()

    assert "Placing FAC at D4..." in out

    # Check if the grid position at (3, 3) has a Factory building now
    assert game.player.grid.grid[3][3].getName() == Buildings.FACTORY.value
    assert game.player.retrieveBuildingsScore() == 37

    factoryIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.FACTORY.value)
    beachIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.BEACH.value)
    houseIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.HOUSE.value)
    highwayIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.HIGHWAY.value)
    shopIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.SHOP.value)

    assert game.player.grid.availableBuildings.availability[factoryIndex] == 4
    assert game.player.grid.availableBuildings.availability[beachIndex] == 4
    assert game.player.grid.availableBuildings.availability[houseIndex] == 5
    assert game.player.grid.availableBuildings.availability[highwayIndex] == 5
    assert game.player.grid.availableBuildings.availability[shopIndex] == 6

    game.leaderboard.saveScoreIntoLeaderboard(game.player.retrieveBuildingsScore(
        False), game.player.grid.rowCount, game.player.grid.colCount, "hwen")
    out, _ = capfd.readouterr()
    assert "Congratulations! You made the high score board at position 1!" in out
    assert len(game.leaderboard.leaderboard[4][4]) == 1
    assert game.leaderboard.leaderboard[4][4][0].name == "hwen" and game.leaderboard.leaderboard[4][4][0].score == 37


def test_whiteBox_flow3(capfd):

    # delete saved leaderboard file generated by other testing before
    try:
        os.remove(savedLeaderboardFilename)
    except OSError:
        pass

    game = Game()

    # Current grid size is 2x2
    game.player.updateGridSize("2,2")

    # Current Building Pool: BCH,FAC,HSE,MON,PRK
    game.player.validateBuildingPoolOptionMenu("1,2,4,6,7")

    # 1. Place Beach on A1
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "A1")

    out, _ = capfd.readouterr()

    assert "Placing BCH at A1..." in out

    # Check if the grid position at (0, 0) has a Beach building now
    assert game.player.grid.grid[0][0].getName() == Buildings.BEACH.value
    assert game.player.turns == 2
    assert game.player.retrieveBuildingsScore() == 3

    # 2. Place Factory on A2
    game.player.validatePlaceBuildingOnPosition(Buildings.FACTORY.value, "A2")

    out, _ = capfd.readouterr()

    assert "Placing FAC at A2..." in out

    # Check if the grid position at (1, 0) has a Factory building now
    assert game.player.grid.grid[1][0].getName() == Buildings.FACTORY.value
    assert game.player.turns == 3
    assert game.player.retrieveBuildingsScore() == 4

    # 3. Place Beach on A1 (Invalid Position)
    game.player.validatePlaceBuildingOnPosition(Buildings.BEACH.value, "D1")

    out, _ = capfd.readouterr()

    assert "D1 is an invalid position! Please enter a valid building position!" in out
    assert game.player.turns == 3
    assert game.player.retrieveBuildingsScore() == 4

    # 4. Place Park on B1
    game.player.validatePlaceBuildingOnPosition(Buildings.PARK.value, "B1")

    out, _ = capfd.readouterr()

    assert "Placing PRK at B1..." in out

    # Check if the grid position at (0, 1) has a Shop building now
    assert game.player.grid.grid[0][1].getName() == Buildings.PARK.value
    assert game.player.turns == 4
    assert game.player.retrieveBuildingsScore() == 5

    # 5. Place Monument on B2
    game.player.validatePlaceBuildingOnPosition(Buildings.MONUMENT.value, "B2")

    out, _ = capfd.readouterr()

    assert "Placing MON at B2..." in out

    # Check if the grid position at (1, 1) has a Highway building now
    assert game.player.grid.grid[1][1].getName() == Buildings.MONUMENT.value
    assert game.player.turns == 5
    assert game.player.retrieveBuildingsScore() == 7

    factoryIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.FACTORY.value)
    beachIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.BEACH.value)
    houseIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.HOUSE.value)
    monumentIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.MONUMENT.value)
    parkIndex = game.player.grid.availableBuildings.buildings.index(
        Buildings.PARK.value)

    assert game.player.grid.availableBuildings.availability[factoryIndex] == 7
    assert game.player.grid.availableBuildings.availability[beachIndex] == 7
    assert game.player.grid.availableBuildings.availability[houseIndex] == 8
    assert game.player.grid.availableBuildings.availability[monumentIndex] == 7
    assert game.player.grid.availableBuildings.availability[parkIndex] == 7

    game.leaderboard.saveScoreIntoLeaderboard(game.player.retrieveBuildingsScore(
        False), game.player.grid.rowCount, game.player.grid.colCount, "user1")
    out, _ = capfd.readouterr()
    assert "Congratulations! You made the high score board at position 1!" in out
    assert len(game.leaderboard.leaderboard[2][2]) == 1
    assert game.leaderboard.leaderboard[2][2][0].name == "user1" and game.leaderboard.leaderboard[2][2][0].score == 7
