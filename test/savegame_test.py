import os
from models.player import Player
from models.configurations import *
from pathlib import Path


dir_path = os.path.dirname(os.path.realpath(__file__))
currentDirectory = Path(dir_path)


def test_checkFileSaved():
    player_test = Player()
    player_test.saveGame()
    rootDirWithFile = currentDirectory.joinpath(savedGameFilename)
    assert rootDirWithFile.exists()
