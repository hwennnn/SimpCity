# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import random
import pytest

citySize = { 
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
}

def test_fillGridWithBuildings(monkeypatch, capfd):
    grid = Grid()
    game = Game()

    row = grid.rowCount
    col = grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 1
    tempList = ["1"]
    for i in range(0, total):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append(str(random.randint(1,2)))
            tempList.append(citySize[colCounter] + str(rowCounter))
    
        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append(str(random.randint(1,2)))
            tempList.append(citySize[colCounter] + str(rowCounter))

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1
    
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main
    except Exception as e:
        print(e)

def test_Exit(monkeypatch, capfd):
    game = Game()

    # Iterations: Start New Game -> Exit Game Menu -> Confirm Exit w/o Save -> Exit Main Menu (Exit Program)
    responses = iter(["1", "0", "Y", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    with pytest.raises(SystemExit) as e:
        import main

    out, _ = capfd.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 0
