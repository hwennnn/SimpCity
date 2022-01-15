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
            tempList.append(str(random.randint(1,2)))
            tempList.append(citySize[colCounter] + str(rowCounter))
            # Add failing cases

        # Resets Col back to 0 (A, first alphabet) once last alphabet is reached. D -> A. 
        # Row is increased by 1. A1 -> A2 (from Row 1 to Row 2)
        # Adds exclusively one A column only or else first column will be empty if its only increment
        else:
            colCounter = 0
            rowCounter += 1
            tempList.append(str(random.randint(1,2)))
            tempList.append(citySize[colCounter] + str(rowCounter))
            # Add failing cases

        # Moves to the next Col each loop, A -> B -> C -> D
        colCounter += 1

    return tempList


# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=2:2

def test_TC_CS_BP_SG_001(monkeypatch, capfd):
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["3", "1", "1,2,3,6,7", "0", "0", "1", "0", "Y", "0"]

    # Iterates through the list of options that mimics user input   
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main
    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration and SystemExit as e:
        pass
    

# Type: Intergration
# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def test_TC_CS_BP_SG_002(monkeypatch, capfd):
    main = MainProgram()
    # Add City Size Logic
    # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
    tempList = ["3", "1", "1,2,3,6,7", "0", "0", "1", "0", "Y", "0"]

    # Iterates through the list of options that mimics user input   
    try:
        responses = iter(tempList)
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        import main
        
    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration and SystemExit as e:
        pass
    

# # Type: Intergration
# # Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# # Test Scenario ID: TS_CS_BP_SG_001
# # Test Data: Valid City Size / Invalid Building Pool
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=4:4

# def test_TC_CS_BP_SG_003(monkeypatch, capfd):
#     # Add City Size Logic
#     # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
#     tempList = ["3", "1", "1,2,3,8,10", "0", "0", "1"]

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         import main

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Intergration
# # Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# # Test Scenario ID: TS_CS_BP_SG_001
# # Test Data: Invalid City Size / Invalid Building Pool
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=5:5

# def test_TC_CS_BP_SG_004(monkeypatch, capfd):
#     # Add City Size Logic
#     # Select Options -> Choose Building Pool, Building Pool Selection, Exit to Options Menu, Exit to Main Menu -> Start New Game
#     tempList = ["3", "1", "1,2,3,8,10", "0", "0", "1"]
    
#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         import main

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the possibility of filling the grid with buildings
# # Test Scenario ID: TS_Grid_Fill_001
# # Test Data: Valid Coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=6:6

# def test_TC_Grid_Fill_001(monkeypatch, capfd):
#     game = Game()
#     tempList = buildingPlacements()

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()
    
#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the possibility of filling the grid with buildings
# # Test Scenario ID: TS_Grid_Fill_001
# # Test Data: Inalid Coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=7:7

# def test_TC_Grid_Fill_002(monkeypatch, capfd):
#     game = Game()

#     # Randomly pick between the two building options together with an invalid coordinate
#     tempList = [str(random.randint(1,2)), "11", str(random.randint(1,2)), "!a", str(random.randint(1,2)), "1a", str(random.randint(1,2)), "!/"]

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()
    
#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Integration
# # Description: Verifying the interaction between placing buildings and remaining building count
# # Test Scenario ID: TS_PB_BC_001
# # Test Data: Valid coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=8:8

# def test_TC_PB_BC_001(monkeypatch, capfd):
#     game = Game()

#     # Randomly pick between the two building options together with a valid coordinate
#     tempList = [str(random.randint(1,2)), "A1"]

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Integration
# # Description: Verifying the interaction between placing buildings and remaining building count
# # Test Scenario ID: TS_PB_BC_001
# # Test Data: Invalid coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=9:9

# def test_TC_PB_BC_002(monkeypatch, capfd):
#     game = Game()

#     # Randomly pick between the two building options together with an invalid coordinate
#     tempList = [str(random.randint(1,2)), "!1"]

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Integration
# # Description: Verifying the interaction between placing buildings and the viewing of game score
# # Test Scenario ID: TS_PB_DS_001
# # Test Data: Valid coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=16:16

# def test_TC_PB_DS_001(monkeypatch, capfd):
#     game = Game()

#     # Ignoring the invalid building options and coordinates.
#     # tempList in this test contains only half of the all coordinates possible
#     tempList = buildingPlacements()[8:int(len(buildingPlacements())/2) + 4]

#     # Display Score
#     tempList.append("3")

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Integration
# # Description: Verifying the interaction between placing buildings and the viewing of game score
# # Test Scenario ID: TS_PB_DS_001
# # Test Data: Invalid coordinates
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=17:17

# def test_TC_PB_DS_002(monkeypatch, capfd):
#     game = Game()

#     # tempList in this test contains only invalid coordinates
#     tempList = buildingPlacements()[:8]

#     # Display Score
#     tempList.append("3")

#     # Iterates through the list of options that mimics user input
#     try:
#         responses = iter(tempList)
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         game.launchGame()

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Valid Game Menu Option / Valid Main Menu Option
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=22:22

# def test_TC_Exit_001(monkeypatch, capfd):
#     # Iterates through the list of options that mimics user input
#     # Start New Game -> Exit to Main Menu -> Confirm -> Exit
#     responses = iter(["1", "0", "Y", "0"])
#     monkeypatch.setattr('builtins.input', lambda _: next(responses))

#     with pytest.raises(SystemExit) as e:
#         import main

#     # Make sure that program is exited from system
#     assert e.type == SystemExit
#     assert e.value.code == 0


# # Type: Functional
# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Valid Game Menu Option / Invalid Main Menu Option
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=23:23

# def test_TC_Exit_002(monkeypatch, capfd):
#     # Iterates through the list of options that mimics user input
#     try:
#         # Start New Game -> Exit to Main Menu -> Confirm -> [Invalid Option]
#         responses = iter(["1", "0", "Y", "8"])
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         import main

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs 
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Invalid Game Menu Option
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=24:24

# def test_TC_Exit_003(monkeypatch, capfd):
#     # Iterates through the list of options that mimics user input
#     try:
#         # Start New Game -> [Invalid Option]
#         responses = iter(["1", "8"])
#         monkeypatch.setattr('builtins.input', lambda _: next(responses))
#         import main
    
#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs 
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Valid option for Game Menu and Valid option for Main Menu.
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=25:25

# def test_TC_SG_Exit_001(monkeypatch, capfd):
#     # Iterates through the list of options that mimics user input
#     # Start New Game -> Exit to Main Menu -> Confirm -> Exit
#     responses = iter(["1", "0", "Y", "0"])
#     monkeypatch.setattr('builtins.input', lambda _: next(responses))
#     with pytest.raises(SystemExit) as e:
#         import main

#     assert e.type == SystemExit
#     assert e.value.code == 0


# # Type: Functional
# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Valid option for Game Menu and Invalid option for Main Menu.
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=26:26

# def test_TC_SG_Exit_002(monkeypatch, capfd):
#     # Start New Game -> Exit to Main Menu -> Confirm -> [Invalid Option]
#     responses = iter(["1", "0", "Y", "5"])
#     monkeypatch.setattr('builtins.input', lambda _: next(responses))
#     # Iterates through the list of options that mimics user input
#     try:
#         import main

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs 
#     except StopIteration as e:
#         pass


# # Type: Functional
# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Invalid option for Game Menu.
# # Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=27:27

# def test_TC_SG_Exit_003(monkeypatch, capfd):
#     # Iterates through the list of options that mimics user input
#     # Start New Game -> [Invalid Option]
#     responses = iter(["1", "9"])
#     monkeypatch.setattr('builtins.input', lambda _: next(responses))

#     # Iterates through the list of options that mimics user input
#     try:
#         import main

#     # When list runs out of options, StopIteration error will happen unless game is exited with user inputs 
#     except StopIteration as e:
#         pass

