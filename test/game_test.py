# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import pytest

# Test Add Building and Saving
def test_placingBuildings(monkeypatch, capfd):
    game = Game()

    ### 1. Build a building at position "A1" -> (0, 0) ###
    responses = iter(["1", "A1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    # Check if the grid position at (0, 0) has a building now and turns == 2
    assert game.player.grid.grid[0][0] is not None
    assert game.player.turns == 2

    ### 2. Build a building at a existing position ###
    responses = iter(["1", "A1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    out, _ = capfd.readouterr()
    # Check if the error message is prompted due to a existing building and turns == 2
    assert game.player.grid.grid[0][0] is not None
    assert "Please enter a valid building position!" in out
    assert game.player.turns == 2

    ### 3. Build a building at position "D4" -> (3, 3) ###
    responses = iter(["2", "D4"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    # Check if the error message is prompted and the grid is not updated at coordinate (3, 3) and turns == 2
    out, _ = capfd.readouterr()
    assert game.player.grid.grid[3][3] is None
    assert "You must build next to an existing building." in out
    assert game.player.turns == 2

    ### 4. Attempt to build a building in an invalid position ###
    responses = iter(["2", "E0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    # Check if the error message is prompted due to out-of-range coordinate and turns == 2
    out, _ = capfd.readouterr()
    assert "Please enter a valid building position!" in out
    assert game.player.turns == 2


def test_continueLoadedGame(monkeypatch, capfd):
    game = Game()

    game.player.loadGame()
    pass


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
