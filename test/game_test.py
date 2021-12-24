# Functional / Integration Test
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
def test_savePlacedBuildings(monkeypatch, capfd):
    player_test = Player()
    player_test.displayMainMenu()

    monkeypatch.setattr('builtins.input', lambda _: "1")
    player_test.validateMain(player_test.promptMainMenu())
    out, _ = capfd.readouterr()

    assert "You selected option 1" in out

    monkeypatch.setattr('builtins.input', lambda _: "1")
    # responses = iter(['1', 'A1'])
    # monkeypatch.setattr('builtins.input', lambda _: next(responses))
    player_test.validateGame(player_test.promptGameMenu())
    monkeypatch.setattr('builtins.input', lambda _: "A1")

    out, _ = capfd.readouterr()
    assert "1" in out
    

    # f = saveGridToTextUnderTest()
    # assert parse_fileToList(f)[0][0] == 'BCH'

# Test loading a saved game file and continue where it left off
def test_continueLoadedGame(capfd):
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

    # Check Score. Score == 3. BCH = 3 Points if Col A / D, else 1 Point.
    assert grid_test.retrieveBuildingsScore == 3


def test_buildingScore():
    pass