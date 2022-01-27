# White-box Integration Test
from models.available_buildings import AvailableBuildings
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
from models.available_buildings import AvailableBuildings
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
            continue    # Ignore ',' and not append (it will be 'None,' if not included)

        if i == '\n':
            row.append(temp)    # Add the last coordinate for the row as it has '\n' instead of ','
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
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])
    
        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])

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
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])
    
        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([player.grid.availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])

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
    
