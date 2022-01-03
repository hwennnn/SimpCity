# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *

# This test must be isolated. For some reasons grid is set to default 'None' for all coordinates
# when placed in the common functional test file
def test_savePlacedBuildings(monkeypatch, capfd):
    game = Game()

    ### 1. Build a building at position "A1" -> (0, 0) ###
    responses = iter(["1", "A1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    assert game.player.turns == 2
    out, _ = capfd.readouterr()

    responses = iter(["1", "B1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    assert game.player.turns == 3
    out, _ = capfd.readouterr()

    responses = iter(["1", "C1"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    game.launchGameHelper()
    assert game.player.turns == 4
    out, _ = capfd.readouterr()

    monkeypatch.setattr('builtins.input', lambda _: "5")
    game.launchGameHelper()
    out, _ = capfd.readouterr()
