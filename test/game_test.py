# Functional / Integration Test
from typing_extensions import Self
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import pytest
from pathlib import Path
import sys
path = str(Path(Path('game_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)


game_test = Game()
player_test = Player()
grid_test = Grid()

# Test Add Building and Saving
# x = Row
# y = Column
def test_SavePlacedBuildings():
    grid_test.createBuilding(Buildings.BEACH, '1', 'A')
    gridValue = grid_test.parseGridAsString()
    with open('testing.txt', 'w+') as f:
        for row in gridValue:
            f.writelines(row + "\n")

    row = []
    grid = []
    f = open("testing.txt", "r")
    f = f.read()

    temp = ''

    for i in f:
        if i == ',':
            row.append(temp)    # Add a coordinate to a row
            temp = ''
            continue    # Ignore ',' and not append
        if i == '\n':
            row.append(temp)    # Add the last coordinate for the row as it has '\n' instead of ','
            grid.append(row)    # Add the row into a list to form a grid
            row = []
            temp = ''
        else:
            temp += i
    assert grid[0][0] == 'A1'
    