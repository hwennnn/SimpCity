from pathlib import Path
import sys
path = str(Path(Path(file).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from models.player import Player
import pytest

player_test = Player()

def test_checkFileSaved(capfd):
    player_test.saveGame()
    assert "test-save.txt" in path


