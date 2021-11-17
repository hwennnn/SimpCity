def displayMainMenu():

    print("""
    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game

    0. Exit
    """)

def promptMainMenu():
    return input('Please enter an input: ')

def validateMain(option):
    if option == '0':
        print('---- Game Ended----')

    else:
        print(f"You selected option {option}")