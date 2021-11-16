def displayMainMenu():

    mainMenu = ("""
    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game

    0. Exit
    """)
    print(mainMenu)
    return mainMenu

def promptMainMenu():
    displayMainMenu
    option = input('Please enter an input: ')
    validateMain(option)

def validateMain(option):
    if option == '0' or option == 0:
        print('---- Game Ended----')
        return ('---- Game Ended----')

    else:
        print(f"You selected option {option}")
        return(f"You selected option {option}")

if __name__ == '__main__':
    promptMainMenu()
