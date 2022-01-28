import time
import pytest
import random
from models.configurations import *
from models.game import Game
from models.player import Player
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
    

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


def get_key(val):
    for key, value in citySize.items():
        if val == value:
            return key


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


def buildingPlacements(x, y):
    player = Player()

    row = x if x is not None else player.grid.rowCount
    col = y if y is not None else player.grid.colCount
    total = row * col

    colCounter = 0
    rowCounter = 1
    tempList = []

    for i in range(0, total):
        # Adds building to grid as long as it has Col has not reached the last alphabet in the grid
        # A1 -> B1 -> C1 -> D1
        if colCounter < col:
            tempList.append(str(random.randint(1, 2)))
            tempList.append(citySize[colCounter] + str(rowCounter))
            # Add failing cases

        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A.
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append(str(random.randint(1, 2)))
            tempList.append(citySize[colCounter] + str(rowCounter))

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1

    # print(f"x = {x}, y = {y} ", tempList)
    return tempList


def validGridSize():
    gridSizeList = []

    x = 2
    y = 2

    for i in range(0, 5):
        for i in range(0,5):
            temp1 = []
            tempString = f"{x},{y}"
            temp1.append(tempString)
            gridSizeList.append(temp1)
            y += 1
        y = 2
        x += 1
    return gridSizeList


def invalidGridSize():
    gridSizeList = []

    x = 0
    y = 0

    # Generate [0-1],[0-6] invalid grid sizes
    for i in range(0, 2):
        for i in range(0,7):
            temp1 = []
            tempString = f"{x},{y}"
            temp1.append(tempString)
            gridSizeList.append(temp1)
            y += 1
        y = 0
        x += 1

    # Generate [2-6],[0-1] invalid grid sizes
    for i in range(0, 5):
        for i in range(0,2):
            temp1 = []
            tempString = f"{x},{y}"
            temp1.append(tempString)
            gridSizeList.append(temp1)
            y += 1
        y = 0
        x += 1

    return gridSizeList


##########################################
##### Functional / Integration Tests #####
##########################################

# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Valid Coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=6:6

@pytest.mark.parametrize('execution_number', range(100))
def test_TC_Grid_Fill_001(monkeypatch, capfd, execution_number):
    start_time = time.time()
    game = Game()

    # Choose random valid city size
    randomCitySize = random.choice(validGridSize())
    x, y = randomCitySize[0].split(',')
    tempList = buildingPlacements(int(x), int(y))

    # Iterates through the list of options that mimics user input
    try:
        # Select Options -> Choose City Size -> Valid City Size -> Exit to Main Menu -> Start Game -> Place Buidlings
        responses = iter(["4", "2", randomCitySize[0], "0", "0", "1"] + tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launch()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass
    
    # Check if each coordinate is filled
    for row in range(0, game.player.grid.rowCount):
        for col in range(0, game.player.grid.colCount):
            assert game.player.grid.grid[row][col] is not None

    return ("\n %s seconds" % (time.time() - start_time))

# Type: Integration
# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Valid coordinates.
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=10:10

@pytest.mark.parametrize('execution_number', range(100))
def test_TC_PB_SG_001(monkeypatch, capfd, execution_number):
    game = Game()

    # Choose random valid city size
    randomCitySize = random.choice(validGridSize())
    x, y = randomCitySize[0].split(',')
    randomCoordinate = random.choice([i for i in buildingPlacements(int(x), int(y)) if len(i) == 2])

    # Select Options -> Choose City Size -> Valid City Size -> Exit to Main Menu -> Start Game -> Place Buidling -> Save Game
    tempList =["4", "2", randomCitySize[0], "0", "0", "1", str(random.randint(1,2)), randomCoordinate, "4"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launch()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    # Prints out the saved game file for verification
    f = open("saved_game.txt", "r")
    file = f.readlines()
    for i in file:
        print(i)

    f = open("saved_game.txt", "r")
    gridList = parse_fileToList(f.read())

    # Check if the game file's building placed is the same as the current grid stored in program
    assert game.player.grid.grid[int([i for i in randomCoordinate][1]) - 1][int(get_key([i for i in randomCoordinate][0]))].__dict__['name'] == gridList[int([i for i in randomCoordinate][1]) - 1][int(get_key([i for i in randomCoordinate][0]))]


##########################################
########### UAT Functional Test ##########
##########################################

# Type: Functional
# Description: Verify that user can select city size
# Test Scenario ID: TS_CitySize_001
# Test Data: Valid City Size - Random
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=3:3

@pytest.mark.parametrize('execution_number', range(100))
def test_UAT_TC_CitySize_001(monkeypatch, capfd, execution_number):
    start_time = time.time()
    game = Game()

    # Choose random valid city size
    randomCitySize = random.choice(validGridSize())
    x, y = randomCitySize[0].split(',')

    # Select Options -> Choose Building Pool, Valid Building Pool
    tempList = ["4", "2", randomCitySize[0]]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launch()

    # When list runs out of options, OS error will happen if a input is not given with prompted
    except StopIteration as e:
        pass
    
    # Check if City Size matches the Grid Size
    assert game.player.grid.rowCount == int(x)
    assert game.player.grid.colCount == int(y)
    
    print("\n%s seconds" % (time.time() - start_time))