from models.player import Player
from src.home import *

while True:
    displayMainMenu()
    option = promptMainMenu()
    validateMain(option)
    if option == '0': 
        break