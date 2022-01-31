import pygsheets
# For Github Actions
gc = pygsheets.authorize(service_file='modular-sign-296911-2bec11f42e5a.json')

# For QA Testing
# gc = pygsheets.authorize(service_file='modular-sign-296911-116ce6ea3ff9.json')

f = open("output.txt", "r")
file = f.readlines()

funtionalIntegrationCol = "I"
funtionalIntegrationTime = "J"
uatFunctionalCol = "G"
uatFunctionalTime = "H"

# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=2:2

def TC_CS_BP_SG_001():
    output = ""
    # Test ID
    output += file[9]
    output += "\n"

    # City Size
    for i in file[41:55]:
        output += i
    output += "\n"

    # Current Building Pool
    for i in file[78:93]:
        output += i

    # Display Grid to check if remaining building is using updated building pool
    for i in file[115:131]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '2', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '2', file[155])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_002():
    output = ""
    # Test ID
    output += file[156]
    output += "\n"

    # Update Grid Size
    for i in file[188:200]:
        output += i
    output += "\n"

    # Display Building Pool
    for i in file[223:238]:
        output += i
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[260:274]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '3', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '3', file[298])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_003():
    output = ""
    # Test ID
    output += file[299]
    output += "\n"

    # Update Grid Size
    for i in file[331:345]:
        output += i
    output += "\n"

    # Display Building Pool
    for i in file[368:383]:
        output += i
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[405:421]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '4', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '4', file[429])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_004():
    output = ""
    # Test ID
    output += file[430]
    output += "\n"

    # Update City Size
    for i in file[462:474]:
        output += i
    output += "\n"

    # Current Building Pool
    for i in file[497:512]:
        output += i
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[534:548]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '5', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '5', file[556])


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Valid Coordinates

def TC_Grid_Fill_001():
    output = ""
    # Test ID
    output += file[557]
    output += "\n"

    # Display Turn and Grid
    for i in file[1201:1218]:
        output += i

    # Display Turn and Grid
    for i in file[1225:1242]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '6', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '6', file[1253])


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Inalid Coordinates

def TC_Grid_Fill_002():
    output = ""
    # Test ID
    output += file[1254]
    output += "\n"

    # Display Turn and Grid
    for i in file[1415:1431]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '7', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '7', file[1439])


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Valid coordinates

def TC_PB_BC_001():
    output = ""
    # Test ID
    output += file[1440]
    output += "\n"

    # Display Turn and Grid
    for i in file[1474:1489]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '8', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '8', file[1497])


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Invalid coordinates

def TC_PB_BC_002():
    output = ""
    # Test ID
    output += file[1498]
    output += "\n"

    # Display Turn and Grid
    for i in file[1532:1546]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '9', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '9', file[1554])


# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Valid coordinates

def TC_PB_SG_001():
    output = ""
    # Test ID
    output += file[1555]
    output += "\n"

    # Display Turn and Grid
    for i in file[1589:1604]:
        output += i
    output += "\n"

    # Output after user input
    output += file[1614]
    output += "\n"

    # Display Game File
    for i in file[1637:1650]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '10', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '10', file[1652])


# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Invalid coordinates

def TC_PB_SG_002():
    output = ""
    # Test ID
    output += file[1653]
    output += "\n"

    # Display Turn and Grid
    for i in file[1687:1701]:
        output += i
    output += "\n"

    # Display Game File
    for i in file[1734:1747]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '11', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '11', file[1749])


# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_CG_001
# Test Data: Valid Game File

def TC_LG_CG_001():
    output = ""
    # Test ID
    output += file[1750]
    output += "\n"

    # Display Load Game and Grid
    for i in file[1762:2353]:
        output += i
    output += "\n"

    # Display Grid
    for i in file[2333:2350]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '12', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '12', file[2365])


# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_CG_001
# Test Data: Valid Game File

def TC_LG_CG_002():
    output = ""
    # Test ID
    output += file[2366]
    output += "\n"

    # Display Turn and Grid
    for i in file[2378:2394]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '13', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '13', file[2402])


# Description: Verifying the interaction between loading the game file and displaying score.
# Test Scenario ID: TS_LG_DS_001
# Test Data: Invalid Game File

def TC_LG_DS_001():
    output = ""
    # Test ID
    output += file[2403]
    output += "\n"

    # Display Turn and Grid
    for i in file[2415:2431]:
        output += i
    output += "\n"

    # Display Score
    for i in file[2441:2448]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '14', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '14', file[2471])


# Description: Verifying the interaction between loading the game file and displaying score.
# Test Scenario ID: TS_LG_DS_001
# Test Data: Invalid Game File

def TC_LG_DS_002():
    output = ""
    # Test ID
    output += file[2472]
    output += "\n"

    # Display Turn and Grid
    for i in file[2484:2500]:
        output += i
    output += "\n"

    # Display Score
    for i in file[2510:2517]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '15', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '15', file[2538])


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Valid coordinates

def TC_PB_DS_001():
    output = ""
    # Test ID
    output += file[2539]
    output += "\n"

    # Display Turn and Grid
    for i in file[2717:2732]:
        output += i
    output += "\n"

    # Display Score
    for i in file[2742:2749]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '16', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '16', file[2770])


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Invalid coordinates

def TC_PB_DS_002():
    output = ""
    # Test ID
    output += file[2771]
    output += "\n"

    # Display Turn and Grid
    for i in file[2858:2872]:
        output += i
    output += "\n"

    # Display Score
    for i in file[2882:2889]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '17', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '17', file[2910])


# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Valid Coordinates

def TC_EOGA_001():
    output = ""
    # Test ID
    output += file[2911]
    output += "\n"

    # Display Turn and Grid
    for i in file[3328:3343]:
        output += i
    output += "\n"

    # Display High Score
    for i in file[3345:3359]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '18', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '18', file[3360])


# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Valid Coordinates

def TC_EOGA_002():
    output = ""
    # Test ID
    output += file[3361]
    output += "\n"

    # Display Turn and Grid
    for i in file[3448:3462]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '19', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '19', file[3470])


# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Valid option for Main Menu - 3

def TC_HS_001():
    output = ""
    # Test ID
    output += file[3471]
    output += "\n"

    # Display High Score
    for i in file[3482:3489]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '20', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '20', file[3499])


# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Valid option for Main Menu - 3

def TC_HS_002():
    output = ""
    # Test ID
    output += file[3500]
    output += "\n"

    # Display High Score
    for i in file[3511:3521]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '21', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '21', file[3522])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Valid Main Menu Option

def TC_Exit_001():
    output = ""
    # Test ID
    output += file[3523]
    output += "\n"

    # Output after user input
    output += file[3557]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[3562:3573]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '22', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '22', file[3574])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Invalid Main Menu Option

def TC_Exit_002():
    output = ""
    # Test ID
    output += file[3575]
    output += "\n"

    # Output after user input
    output += file[1609]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[3624:3634]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '23', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '23', file[3635])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Invalid Game Menu Option

def TC_Exit_003():
    output = ""
    # Test ID
    output += file[3636]
    output += "\n"

    # Display Turn and Game Menu
    for i in file[3670:3691]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '24', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '24', file[3692])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Valid option for Main Menu.
def TC_SG_Exit_001():
    output = ""
    # Test ID
    output += file[3693]
    output += "\n"

    # Output after user input
    output += file[3727]
    output += "\n"

    # Display Main Menu + Game Ended
    for i in file[3732:3743]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '25', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '25', file[3744])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Invalid option for Main Menu.

def TC_SG_Exit_002():
    output = ""
    # Test ID
    output += file[3745]
    output += "\n"

    # Output after user input
    output += file[3779]
    output += "\n"

    # Display Main Menu + Output after user input
    for i in file[3794:3804]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '26', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '26', file[3805])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Invalid option for Game Menu.

def TC_SG_Exit_003():
    output = ""
    # Test ID
    output += file[3806]
    output += "\n"

    # Display Turn and Game Menu
    for i in file[3840:3861]:
        output += i

    # Output after user input
    output += "\n"
    output += file[2884]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '27', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '27', file[3862])


# Description: Verify that user can see main menu
# Test Scenario ID: UAT_TS_MainMenu_001
# Test Data: NA

def UAT_TC_MainMenu_001():
    output = ""
    # Test ID
    output += file[3863]
    output += "\n"

    # Display Main Menu
    for i in file[3866:3875]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '2', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '2', file[3875])


# Description: Verify that user can select city size
# Test Scenario ID: TS_CitySize_001
# Test Data: Valid City Size

def UAT_TC_CitySize_001():
    output = ""
    # Test ID
    output += file[3876]
    output += "\n"

    # Display Main Menu, Options Menu and City Size
    for i in file[3908:3922]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '3', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '3', file[3924])


# Description: Verify that user can select city size
# Test Scenario ID: TS_CitySize_001
# Test Data: Invalid City Size

def UAT_TC_CitySize_002():
    output = ""
    # Test ID
    output += file[3925]
    output += "\n"

    # Display Main Menu, Options Menu and City Size
    for i in file[3957:3969]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '4', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '4', file[3971])


# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Valid Building Pool - 1,2,4,6,7

def UAT_TC_BuildingPool_001():
    output = ""
    # Test ID
    output += file[3972]
    output += "\n"

    # Display Current Building Pool
    for i in file[4004:4019]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '5', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '5', file[4020])


# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Invalid Building Pool - 1,2,8,9,10

def UAT_TC_BuildingPool_002():
    output = ""
    # Test ID
    output += file[4021]
    output += "\n"

    # Display Current Building Pool
    for i in file[4053:4068]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '6', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '6', file[4069])


# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Valid Main Menu Option - 1

def UAT_TC_StartGame_001():
    output = ""
    # Test ID
    output += file[4070]
    output += "\n"

    # Display Main Menu and Selection Output (Including Grid and Game Menu)
    for i in file[4081:4104]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '7', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '7', file[4105])


# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Invalid Main Menu Option - 5

def UAT_TC_StartGame_002():
    output = ""
    # Test ID
    output += file[4106]
    output += "\n"

    # Display Main Menu and Selection Output (Including Grid and Game Menu)
    for i in file[4117:4127]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '8', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '8', file[4128])


# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Valid Coordinate - A1

def UAT_TC_PlaceBuilding_001():
    output = ""
    # Test ID
    output += file[4129]
    output += "\n"

    # Display Turn and Grid
    for i in file[4163:4178]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '9', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '9', file[4186])


# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Invalid Coordinate - A9

def UAT_TC_PlaceBuilding_002():
    output = ""
    # Test ID
    output += file[4187]
    output += "\n"

    # Display Turn and Grid
    for i in file[4221:4235]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '10', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '10', file[4243])


# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Valid Coordinate - A1

def UAT_TC_BuildingCount_001():
    output = ""
    # Test ID
    output += file[4244]
    output += "\n"

    # Display Turn and Grid
    for i in file[4278:4293]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '11', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '11', file[4301])


# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Invalid Coordinate - A9

def UAT_TC_BuildingCount_002():
    output = ""
    # Test ID
    output += file[4302]
    output += "\n"

    # Display Turn and Grid
    for i in file[4336:4349]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '12', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '12', file[4358])


# Description: Verify that user can save game
# Test Scenario ID: UAT_TS_SaveGame_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 4

def UAT_TC_SaveGame_001():
    output = ""
    # Test ID
    output += file[4359]
    output += "\n"

    # Display Turn and Grid
    for i in file[4396:4408]:
        output += i
    output += "\n"

    # Output after user input
    output += file[4418]
    output += "\n"

    # Display Saved File
    for i in file[4441:4454]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '13', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '13', file[4456])


# Description: Verify that game file can be loaded
# Test Scenario ID: UAT_TS_LoadGame_001
# Test Data: Valid Game File

def UAT_TC_LoadGame_001():
    output = ""
    # Test ID
    output += file[4457]
    output += "\n"

    # Display Turn and Grid
    for i in file[4469:4485]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '14', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '14', file[4493])


# Description: Verify that game file can be loaded
# Test Scenario ID: UAT_TS_LoadGame_001
# Test Data: Invalid Game File

def UAT_TC_LoadGame_002():
    output = ""
    # Test ID
    output += file[4494]
    output += "\n"

    # Display Turn and Grid
    for i in file[4505:4522]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '15', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '15', file[4530])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 3

def UAT_TC_GameScore_001():
    output = ""
    # Test ID
    output += file[4531]

    # Display Turn and Grid
    output += "\n"
    for i in file[4565:4580]:
        output += i
    output += "\n"

    # Display Score
    for i in file[4587:4597]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '16', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '16', file[4618])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Invalid Coordinate - A9, Valid Game Menu Option - 3

def UAT_TC_GameScore_002():
    output = ""
    # Test ID
    output += file[4619]

    # Display Turn and Grid
    output += "\n"
    for i in file[4653:4667]:
        output += i
    output += "\n"

    # Display Score
    output += "\n"
    for i in file[4677:4684]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '17', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '17', file[4705])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Valid Coordinates

def UAT_TC_GameScore_003():
    output = ""
    # Test ID
    output += file[4706]

    # Display Grid Size
    output += "\n"
    for i in file[5374:5391]:
        output += i

    # Display EOGA
    output += "\n"
    for i in file[5393:5407]:
        output += i

    # View High Score from Main Menu
    output += "\n"
    for i in file[5408:5423]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '18', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '18', file[5433])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_HighScore_001
# Test Data: Valid Main Menu Option - 3

def UAT_TC_HighScore_001():
    output = ""
    # Test ID
    output += file[5434]

    # View High Score from Main Menu
    output += "\n"
    for i in file[5445:5461]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '19', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '19', file[5462])


TC_CS_BP_SG_001()
TC_CS_BP_SG_002()
TC_CS_BP_SG_003()
TC_CS_BP_SG_004()
TC_Grid_Fill_001()
TC_Grid_Fill_002()
TC_PB_BC_001()
TC_PB_BC_002()
TC_PB_SG_001()
TC_PB_SG_002()
TC_LG_CG_001()
TC_LG_CG_002()
TC_LG_DS_001()
TC_LG_DS_002()
TC_PB_DS_001()
TC_PB_DS_002()
TC_EOGA_001()
TC_EOGA_002()
TC_HS_001()
TC_HS_002()
TC_Exit_001()
TC_Exit_002()
TC_Exit_003()
TC_SG_Exit_001()
TC_SG_Exit_002()
TC_SG_Exit_003()

UAT_TC_MainMenu_001()
UAT_TC_CitySize_001()
UAT_TC_CitySize_002()
UAT_TC_BuildingPool_001()
UAT_TC_BuildingPool_002()
UAT_TC_StartGame_001()
UAT_TC_StartGame_002()
UAT_TC_PlaceBuilding_001()
UAT_TC_PlaceBuilding_002()
UAT_TC_BuildingCount_001()
UAT_TC_BuildingCount_002()
UAT_TC_SaveGame_001()
UAT_TC_LoadGame_001()
UAT_TC_LoadGame_002()
UAT_TC_GameScore_001()
UAT_TC_GameScore_002()
UAT_TC_GameScore_003()
UAT_TC_HighScore_001()