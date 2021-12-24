# Functional / Integration Test
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *

# Test Add Building and Saving


def test_placingBuildings(monkeypatch, capfd):
    game = Game()

    ### 1. Build a building at position "A1" -> (0, 0) ###
    responses = iter(["1", "A1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    game.launchGameHelper()

    # Check if the grid position at (0, 0) has a building now
    assert game.player.grid.grid[0][0] is not None
    assert game.player.turns == 2

    ### 2. Attempt to build a building in an invalid position ###
    responses = iter(["2", "E0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    game.launchGameHelper()

    # Check if the error message is prompted
    out, _ = capfd.readouterr()
    assert "Please enter a valid building position!" in out
    assert game.player.turns == 2

    ### 3. Build a building at position "A2" -> (1, 0) ###
    responses = iter(["2", "A2"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    game.launchGameHelper()

    # Check if the error message is prompted
    out, _ = capfd.readouterr()
    assert game.player.grid.grid[1][0] is not None
    assert game.player.turns == 3

    ### 4. Build a building at position "D4" -> (3, 3) ###
    responses = iter(["2", "D4"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    game.launchGameHelper()

    # Check if the error message is prompted and the grid is not updated at position (3, 3)
    out, _ = capfd.readouterr()
    assert game.player.grid.grid[3][3] is None
    assert "You must build next to an existing building." in out
    assert game.player.turns == 3
