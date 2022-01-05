# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import random

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
    for i in range(0, total + 1):
        if colCounter < col:
            responses = iter(["1", citySize[colCounter] + str(rowCounter)])
            monkeypatch.setattr('builtins.input', lambda _: next(responses))
            game.launchGameHelper()
        else:
            colCounter = 0
            rowCounter += 1
            responses = iter(["1", citySize[colCounter] + str(rowCounter)])
            monkeypatch.setattr('builtins.input', lambda _: next(responses))
            game.launchGameHelper()

        colCounter += 1