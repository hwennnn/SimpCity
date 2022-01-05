# Functional / Integration Test - Black Box Edition
from models.player import Player
from models.game import Game
from models.grid import Grid
from models.enums import Buildings
from models.configurations import *
import pytest

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
