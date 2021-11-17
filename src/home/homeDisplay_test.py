from homeDisplay import *
import pytest

def test_displayMainMenu(capfd):
    displayMainMenu()
    out, err = capfd.readouterr()
    assert """
    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game

    0. Exit
    """ in out

def test_nonExit(capfd):
    option = "1"
    validateMain(option)
    out, err = capfd.readouterr()
    assert f"You selected option {option}" in out

def test_Exit(capfd):
    option = "0"
    validateMain(option)
    out, err = capfd.readouterr()
    assert "---- Game Ended----" in out
