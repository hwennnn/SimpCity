# Functional / Integration Test - Black Box Edition
from models.available_buildings import AvailableBuildings
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
from models.available_buildings import AvailableBuildings
import random

def test_fillGridWithBuildings(monkeypatch, capfd):
    grid = Grid()
    game = Game()
    player = Player()
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
        grid.updateGrid(i[1], i[2], i[0])
        assert grid.grid[i[1]][i[2]] is not None
