# Unit Test Only

from models.game import Game
from pathlib import Path
import sys
path = str(Path(Path('game_test.py').parent.absolute()).parent.absolute())
sys.path.insert(0, path)

gameObject = Game()


def test_displayLeaderboard(capfd):
    gameObject.displayLeaderboard()

    out, _ = capfd.readouterr()
    
    assert "--------- HIGH SCORES ---------" in out
