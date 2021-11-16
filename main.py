
# Driver code (Please delete this once you have worked on the main menu)
# while True:
#     option = input('Please enter an option: ')

#     if option == '0':
#         print('Exit game ...')
#         break
#     else:
#         print(f'You have selected an option {option}')

from adminFunction import *

while True:
    displayMainMenu()
    if(validateMain(promptMainMenu()) == '---- Game Ended----'):
        break
