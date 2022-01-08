# Functional / Integration Test - Black Box Edition
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

def test_fillGridWithBuildings(monkeypatch, capfd):
    grid = Grid()
    availableBuildings = AvailableBuildings()

    row = grid.rowCount
    col = grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 0
    tempList = []
    for i in range(0, total):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append([availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])
    
        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1
    
    for i in tempList:
        # Place building
        grid.updateGrid(i[1], i[2], i[0])
        assert grid.grid[i[1]][i[2]] is not None

def test_placeAndSave(monkeypatch, capfd):
    grid = Grid()
    player = Player()
    availableBuildings = AvailableBuildings()

    row = grid.rowCount
    col = grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 0
    tempList = []

    # Halved for testing purposes. a full grid will not be viable as end of game action will kicks in when loaded
    for i in range(0, round(total / 2)):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append([availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])
    
        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append([availableBuildings.retriveTwoRandomBuildings()[(random.randint(0,1))], rowCounter, colCounter])

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1
    
    for i in tempList:
        # Place building
        grid.updateGrid(i[1], i[2], i[0])
        assert grid.grid[i[1]][i[2]] is not None
    
    # Passing in the state of the current grid
    saveGridToTextUnderTest(grid)
    rootDirWithFile = currentDirectory.joinpath("testing.txt")
    assert rootDirWithFile.exists() == True

def test_citySizeBuildingPoolAndStartGame(monkeypatch, capfd):
    player = Player()
    availableBuildings = AvailableBuildings()
    # Add City Size Logic
    availableBuildings.updateBuildingPool("1,2,3,6,7")
    availableBuildings.displayCurrentBuildingPool()
    out, _ = capfd.readouterr()
    assert "Current Building Pool: BCH,FAC,HWY,MON,PRK" in out
    # When game starts, turn = 1
    assert player.turns == 1

def test_buildingPoolAndRemainingBuildings(monkeypatch, capfd):
    player = Player()
    grid = Grid()
    player.grid.availableBuildings.updateBuildingPool("1,2,3,6,7")
    # Check if current building pool is those of selected
    print(player.grid.availableBuildings.buildings)
    out, _ = capfd.readouterr()
    assert "['BCH', 'FAC', 'HWY', 'MON', 'PRK']" in out

def test_buildingPoolAndRemainingBuildingCount(monkeypatch, capfd):
    player = Player()
    grid = Grid()
    player.grid.availableBuildings.updateBuildingPool("1,2,3,6,7")
    # Check if current building pool is those of selected
    print(player.grid.availableBuildings.buildings)
    out, _ = capfd.readouterr()
    assert "['BCH', 'FAC', 'HWY', 'MON', 'PRK']" in out
    
    monkeypatch.setattr('builtins.input', lambda _: "A1")
    player.promptEnterBuildingPosition("PRK")
    print(player.grid.availableBuildings.availability)
    out, _ = capfd.readouterr()
    assert "[8, 8, 8, 8, 7]" in out