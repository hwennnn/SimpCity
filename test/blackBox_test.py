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


def buildingPlacements():
    player = Player()

    row = player.grid.rowCount
    col = player.grid.colCount
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


def gridSize():
    gridSizeList = []

    x = 2
    y = 2

    for i in range(0, 4):
        for i in range(0,5):
            temp1 = []
            tempString = f"{x},{y}"
            temp1.append(tempString)
            gridSizeList.append(temp1)
            y += 1
        y = 2
        x += 1
    return gridSizeList


##########################################
##### Functional / Integration Tests #####
##########################################

# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size, Valid Building Pool - 1,2,3,6,7
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=2:2

def test_TC_CS_BP_SG_001(monkeypatch, capfd):
    start_time = time.time()
    game = Game()
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["4", "1", "1,2,3,6,7", "0", "0", "1", "0", "Y", "0"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launch()
    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration and SystemExit as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size, Valid Building Pool - 1,2,3,6,7
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def test_TC_CS_BP_SG_002(monkeypatch, capfd):
    start_time = time.time()
    game = Game()
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["4", "1", "1,2,3,6,7", "0", "0", "1", "0", "Y", "0"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launch()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration and SystemExit as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size, Invalid Building Pool - 1,2,3,8,10
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=4:4

def test_TC_CS_BP_SG_003(monkeypatch, capfd):
    start_time = time.time()
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["4", "1", "1,2,3,8,10", "0", "0", "1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size, Invalid Building Pool - 1,2,3,8,10
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=5:5

def test_TC_CS_BP_SG_004(monkeypatch, capfd):
    start_time = time.time()
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["4", "1", "1,2,3,8,10", "0", "0", "1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Valid Coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=6:6

def test_TC_Grid_Fill_001(monkeypatch, capfd):
    start_time = time.time()
    
    # game = Game()
    # randomCitySize = random.choice(gridSize())
    # x, y = randomCitySize[0].split(',')
    # tempList = buildingPlacements(int(x), int(y))

    # # Iterates through the list of options that mimics user input
    # try:
    #     responses = iter(["3", "2", randomCitySize[0], "0", "1"] + tempList)
    #     monkeypatch.setattr('builtins.input', lambda _: next(responses))
    #     game.launch()

    # # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    # except StopIteration as e:
    #     pass

    game = Game()
    tempList = buildingPlacements()

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Inalid Coordinates - 11, !a, 1a,!/
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=7:7

def test_TC_Grid_Fill_002(monkeypatch, capfd):
    start_time = time.time()
    game = Game()

    # Randomly pick between the two building options together with an invalid coordinate
    tempList = [str(random.randint(1, 2)), "11", str(random.randint(1, 2)), "!a", str(
        random.randint(1, 2)), "1a", str(random.randint(1, 2)), "!/"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Valid coordinates - A1
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=8:8

def test_TC_PB_BC_001(monkeypatch, capfd):
    start_time = time.time()
    game = Game()

    # Randomly pick between the two building options together with a valid coordinate
    tempList = [str(random.randint(1, 2)), "A1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Invalid coordinates - !1
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=9:9

def test_TC_PB_BC_002(monkeypatch, capfd):
    start_time = time.time()
    game = Game()

    # Randomly pick between the two building options together with an invalid coordinate
    tempList = [str(random.randint(1, 2)), "!1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Valid coordinates.
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=10:10

def test_TC_PB_SG_001(monkeypatch, capfd):
    game = Game()

    # # Add random picking of city size and random coordinate

    # randomCitySize = random.choice(gridSize())
    # x, y = randomCitySize[0].split(',')
    # tempList = buildingPlacements(int(x), int(y))

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(["1", str(random.randint(1,2)), "A4", "4"])
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


# Type: Integration
# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_SG_001
# Test Data: Invalid coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=11:11

def test_TC_PB_SG_002(monkeypatch, capfd):
    game = Game()

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(["1", str(random.randint(1,2)), "A20", "4"])
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


# Type: Integration
# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_CG_001
# Test Data: Valid Game File
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=12:12

def test_TC_LG_CG_001(monkeypatch, capfd):
    pass


# Type: Integration
# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_DS_001
# Test Data: Invalid Game File
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=14:14

def test_TC_LG_DS_001(monkeypatch, capfd):
    pass


# Type: Integration
# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_DS_001
# Test Data: Invalid Game File
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=15:15

def test_TC_LG_DS_001(monkeypatch, capfd):
    pass


# Type: Integration
# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Valid coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=16:16

def test_TC_PB_DS_001(monkeypatch, capfd):
    start_time = time.time()
    game = Game()

    # Ignoring the invalid building options and coordinates.
    # tempList in this test contains only half of the all coordinates possible
    tempList = buildingPlacements()[0:int(len(buildingPlacements())/2)]
    # Display Score
    tempList.append("3")

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Invalid coordinates - 11, 1a, 1a, !/
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=17:17

def test_TC_PB_DS_002(monkeypatch, capfd):
    start_time = time.time()
    game = Game()

    # tempList in this test contains only invalid coordinates
    tempList = [str(random.randint(1, 2)), "11", str(random.randint(1, 2)), "!a", str(
        random.randint(1, 2)), "1a", str(random.randint(1, 2)), "!/"]

    # Display Score
    tempList.append("3")

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        game.launchGame()

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Valid Coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=18:18

def test_TC_EOGA_001(monkeypatch, capfd):
    pass


# Type: Functional
# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Invalid Coordinates
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=19:19

def test_TC_EOGA_002(monkeypatch, capfd):
    pass


# Type: Functional
# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Valid option for Main Menu.
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=20:20

def test_TC_HS_001(monkeypatch, capfd):
    pass


# Type: Functional
# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Invalid option for Main Menu.
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=21:21

def test_TC_HS_001(monkeypatch, capfd):
    pass


# Type: Functional
# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option - 1, Valid Main Menu Option - 0, Y, 0
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=22:22

def test_TC_Exit_001(monkeypatch, capfd):
    start_time = time.time()
    # Iterates through the list of options that mimics user input
    # Start New Game -> Exit to Main Menu -> Confirm -> Exit
    responses = iter(["1", "0", "Y", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    with pytest.raises(SystemExit) as e:
        import main

    # Make sure that program is exited from system
    assert e.type == SystemExit
    assert e.value.code == 0

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option - 1, Invalid Main Menu Option 0, Y, 8
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=23:23

def test_TC_Exit_002(monkeypatch, capfd):
    start_time = time.time()
    # Iterates through the list of options that mimics user input
    try:
        # Start New Game -> Exit to Main Menu -> Confirm -> [Invalid Option]
        responses = iter(["1", "0", "Y", "8"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Main Menu Option - 1, Invalid Game Menu Option - 8
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=24:24

def test_TC_Exit_003(monkeypatch, capfd):
    start_time = time.time()
    # Iterates through the list of options that mimics user input
    try:
        # Start New Game -> [Invalid Option]
        responses = iter(["1", "8"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid Option for Main Menu - 1, Valid Option for Game Menu - 0, Y, Valid Option for Main Menu - 0
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=25:25

def test_TC_SG_Exit_001(monkeypatch, capfd):
    start_time = time.time()
    # Iterates through the list of options that mimics user input
    # Start New Game -> Exit to Main Menu -> Confirm -> Exit
    responses = iter(["1", "0", "Y", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    with pytest.raises(SystemExit) as e:
        import main

    assert e.type == SystemExit
    assert e.value.code == 0

    print("\n %s seconds" % (time.time() - start_time))


# Type: Integration
# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid Option for Main Menu - 1, Valid Option for Game Menu - 0, Y, Invalid Option for Main Menu - 5
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=26:26

def test_TC_SG_Exit_002(monkeypatch, capfd):
    start_time = time.time()
    # Start New Game -> Exit to Main Menu -> Confirm -> [Invalid Option]
    responses = iter(["1", "0", "Y", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    # Iterates through the list of options that mimics user input
    try:
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu - 1, Invalid option for Game Menu - 9
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=27:27

def test_TC_SG_Exit_003(monkeypatch, capfd):
    start_time = time.time()
    # Iterates through the list of options that mimics user input
    # Start New Game -> [Invalid Option]
    responses = iter(["1", "9"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    # Iterates through the list of options that mimics user input
    try:
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


##########################################
########### UAT Functional Test ##########
##########################################

# Type: Functional
# Description: Verify that user can see main menu
# Test Scenario ID: UAT_TS_MainMenu_001
# Test Data: NA
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=2:2

def test_UAT_TC_MainMenu_001(monkeypatch, capfd):
    start_time = time.time()

    # Start New Game
    try:
        import main

    # When list runs out of options, OS error will happen if a input is not given with prompted
    except OSError as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Valid Building Pool - 1,2,4,6,7
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=4:4

def test_UAT_TC_BuildingPool_001(monkeypatch, capfd):
    start_time = time.time()
    # Select Options -> Choose Building Pool, Building Pool Selection
    tempList = ["3", "1", "1,2,3,6,7"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Invalid Building Pool - 1,2,8,9,10
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=5:5

def test_UAT_TC_BuildingPool_002(monkeypatch, capfd):
    start_time = time.time()
    # Select Options -> Choose Building Pool, Building Pool Selection
    tempList = ["3", "1", "1,2,3,8,10"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Valid Main Menu Option - 1
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=6:6

def test_UAT_TC_StartGame_001(monkeypatch):
    start_time = time.time()
    # Start Game
    tempList = ["1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Invalid Main Menu Option - 5
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=7:7

def test_UAT_TC_StartGame_002(monkeypatch, capfd):
    start_time = time.time()
    # Attempt to Start Game with invalid option
    tempList = ["5"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n %s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Valid Coordinate - A1
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=8:8

def test_UAT_TC_PlaceBuilding_001(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building
    tempList = ["1", str(random.randint(1, 2)), "A1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Invalid Coordinate - A9
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=9:9

def test_UAT_TC_PlaceBuilding_002(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building
    tempList = ["1", str(random.randint(1, 2)), "A9"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Valid Coordinate - A1
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=10:10

def test_UAT_TC_BuildingCount_001(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building, Check building count
    tempList = ["1", str(random.randint(1, 2)), "A1"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Invalid Coordinate - A9
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=11:11

def test_UAT_TC_BuildingCount_002(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building with invalid coordinate, Check building count
    tempList = ["1", str(random.randint(1, 2)), "A9"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that user can save game
# Test Scenario ID: UAT_TS_SaveGame_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 4
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=12:12

def test_UAT_TC_SaveGame_001(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building with invalid coordinate, Save game
    tempList = ["1", str(random.randint(1, 2)), "A1", "4"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    # Prints out the saved game file for verification
    f = open("saved_game.txt", "r")
    file = f.readlines()
    for i in file:
        print(i)

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 3
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=15:15

def test_UAT_TC_GameScore_001(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building, Check game score
    tempList = ["1", str(random.randint(1, 2)), "A1", "3"]
    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))


# Type: Functional
# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Invalid Coordinate - A9, Valid Game Menu Option - 3
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit#gid=1826582149&range=16:16

def test_UAT_TC_GameScore_002(monkeypatch, capfd):
    start_time = time.time()
    # Start Game, Select a random building, Place a building with invalid coordinate, Check game score
    tempList = ["1", str(random.randint(1, 2)), "A9", "3"]

    # Iterates through the list of options that mimics user input
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))
