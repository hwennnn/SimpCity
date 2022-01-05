# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import random

# This test must be isolated. For some reasons grid is set to default 'None' for all coordinates
# when placed in the common functional test file
# def test_savePlacedBuildings(monkeypatch, capfd):
    # game = Game()

    # ### 1. Build a building at position "A1" -> (0, 0) ###
    # responses = iter(["1", "A1"])
    # monkeypatch.setattr('builtins.input', lambda _: next(responses))
    # game.launchGameHelper()
    # assert game.player.turns == 2
    # out, _ = capfd.readouterr()
    
    # responses = iter(["1", "B1"])
    # monkeypatch.setattr('builtins.input', lambda _: next(responses))
    # game.launchGameHelper()
    # assert game.player.turns == 3
    # out, _ = capfd.readouterr()

    # responses = iter(["1", "C1"])
    # monkeypatch.setattr('builtins.input', lambda _: next(responses))
    # game.launchGameHelper()
    # assert game.player.turns == 4
    # out, _ = capfd.readouterr()

    # responses = iter(["1", "D1"])
    # monkeypatch.setattr('builtins.input', lambda _: next(responses))
    # game.launchGameHelper()
    # assert game.player.turns == 5
    # out, _ = capfd.readouterr()

    # monkeypatch.setattr('builtins.input', lambda _: "5")
    # game.launchGameHelper()
    # out, _ = capfd.readouterr()

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
    grid = Grid()
    # Test saving the current grid (on test) on a separate text file
    gridValue = grid.parseGridAsString()  
    with open('testing.txt', 'w+') as f:
        for row in gridValue:
            f.writelines(row + "\n")

    # Test if the program saved the correct coordinates
    f = open("testing.txt", "r")
    f = f.read()
    return f

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

# def test_randomPlacementAndSave(monkeypatch, capfd):
#     grid = Grid()
#     game = Game()

#     row = grid.rowCount
#     col = grid.colCount
#     total = row * col

#     rowRand, colRand = randomRoll(row, col)
#     assert rowRand != 0


#     for i in range(0, round(total / 2)):    # 7.4 rounded down to 7, 7.5 rounded up to 8
#         rowRand, colRand = randomRoll(row, col)
#         try:
#             assert grid.grid[rowRand][colRand] is None
#         except:
#             rowRand, colRand = randomRoll(row, col)
            
#         responses = iter(["1", citySize[colRand] + str(rowRand)])
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGameHelper()

#         f = saveGridToTextUnderTest
#         gridList = parse_fileToList(f)
        
#     out, _ = capfd.readouterr()
#     assert out == "[]"

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

    tempList.append("0")
    tempList.append("Y")
    responses = iter(tempList)
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    import main