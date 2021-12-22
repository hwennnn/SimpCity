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

def saveGridToTextUnderTest():
    # Test saving the current grid (on test) on a separate text file
    gridValue = grid_test.parseGridAsString()  
    with open('testing.txt', 'w+') as f:
        for row in gridValue:
            f.writelines(row + "\n")

    # Test if the program saved the correct coordinates
    f = open("testing.txt", "r")
    f = f.read()
    return f

# Test Add Building and Saving
def test_SavePlacedBuildings():
    grid_test.createBuilding(Buildings.BEACH.value, '1', 'A')     # Building Name, x, y
    f = saveGridToTextUnderTest()

    # parse_fileToString = Grid will be tested in nested list format
    # [[None, None, None, None]
    #  [None, None, None, None]
    #  [None, None, None, None]
    #  [None, None, None, None]]
    assert parse_fileToList(f)[0][0] == 'BCH'

# Test loading a saved game file and continue where it left off
def test_ContinueLoadedGame(capfd):
    f = open("testing.txt", "r")
    f = f.read()

    # Verify and load valid game file to grid
    validity = grid_test.isSavedGameFileValid(f)
    grid_test.readGridFromFile(f) if grid_test.isSavedGameFileValid(f) == True else "" if validity == False else "" # "" = Placeholder / Do Nothing

    # Convert Grid to String and Check if the file uploaded is correct (A1 = BCH)
    f = saveGridToTextUnderTest()
    assert parse_fileToList(f)[0][0] == 'BCH'
    assert player_test.turns == 2

    out, _ = capfd.readouterr()
    assert """
    A     B     C     D
 +-----+-----+-----+-----+ 
1| BCH |     |     |     | 
 +-----+-----+-----+-----+ 
2|     |     |     |     | 
 +-----+-----+-----+-----+ 
3|     |     |     |     | 
 +-----+-----+-----+-----+ 
4|     |     |     |     | 
 +-----+-----+-----+-----+ 
""" in out

    # Check Score
    

def test_BuildingScore():
    pass