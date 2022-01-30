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
    for i in file[1589:1603]:
        output += i
    output += "\n"

    # Output after user input
    output += file[1614]
    output += "\n"

    # Display Game File
    for i in file[1637:1648]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '10', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '10', file[1650])


# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Invalid coordinates

def TC_PB_SG_002():
    output = ""
    # Test ID
    output += file[1651]
    output += "\n"

    # Display Turn and Grid
    for i in file[1685:1698]:
        output += i
    output += "\n"

    # Output after user input
    output += file[1709]
    output += "\n"

    # Display Game File
    for i in file[1732:1743]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '11', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '11', file[1745])


# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_CG_001
# Test Data: Valid Game File

def TC_LG_CG_001():
    output = ""
    # Test ID
    output += file[1746]
    output += "\n"

    # Display Load Game and Grid
    for i in file[1758:1773]:
        output += i
    output += "\n"

    # Display Grid
    for i in file[2333:2350]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '12', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '12', file[2358])


# Description: Verifying the interaction between loading the game file and continuing the game.
# Test Scenario ID: TS_LG_CG_001
# Test Data: Valid Game File

def TC_LG_CG_002():
    output = ""
    # Test ID
    output += file[2359]
    output += "\n"

    # Display Turn and Grid
    for i in file[2372:1698]:
        output += i
    output += "\n"

    # Output after user input
    output += file[1709]
    output += "\n"

    # Display Game File
    for i in file[1732:1743]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '13', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '13', file[1745])


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Valid coordinates

def TC_PB_DS_001():
    output = ""
    # Test ID
    output += file[1632]
    output += "\n"

    # Display Turn and Grid
    for i in file[1810:1824]:
        output += i

    # Output after user input
    output += "\n"
    output += file[1832]
    output += "\n"

    # Display Score
    for i in file[1835:1842]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '16', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '16', file[1863])


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Invalid coordinates

def TC_PB_DS_002():
    output = ""
    # Test ID
    output += file[1864]
    output += "\n"

    # Display Turn and Grid
    for i in file[1951:1964]:
        output += i

    # Output after user input
    output += "\n"
    output += file[1972]
    output += "\n"

    # Display Score
    for i in file[1975:1982]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '17', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '17', file[2003])


# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Valid Coordinates

def TC_EOGA_001():
    output = ""
    # Test ID
    output += file[2004]
    output += "\n"

    # Display Turn and Grid
    for i in file[2358:2383]:
        output += i
    output += "\n"

    # Display High Score
    for i in file[2383:2388]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '18', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '18', file[2389])


# Description: Verifying the interaction between placing the final building, calculation of game score, adding to leaderboard and displaying of high score
# Test Scenario ID: TS_EOGA_001
# Test Data: Valid Coordinates

def TC_EOGA_002():
    output = ""
    # Test ID
    output += file[2390]
    output += "\n"

    # Display Turn and Grid
    for i in file[2477:2491]:
        output += i
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '19', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '19', file[2499])


# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Valid option for Main Menu - 3

def TC_HS_001():
    output = ""
    # Test ID
    output += file[2500]
    output += "\n"

    # Display High Score
    for i in file[2512:2518]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '20', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '20', file[2529])


# Description: Verify High Score (leaderboard) can be shown from Main Menu
# Test Scenario ID: TS_HS_001
# Test Data: Valid option for Main Menu - 3

def TC_HS_002():
    output = ""
    # Test ID
    output += file[2530]
    output += "\n"

    # Display High Score
    for i in file[2542:2552]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '21', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '21', file[2554])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Valid Main Menu Option

def TC_Exit_001():
    output = ""
    # Test ID
    output += file[2555]
    output += "\n"

    # Output after user input
    output += file[2590]
    output += "\n"
    output += file[2593]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[2597:2607]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '22', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '22', file[2608])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Invalid Main Menu Option

def TC_Exit_002():
    output = ""
    # Test ID
    output += file[2609]
    output += "\n"

    # Output after user input
    output += file[2644]
    output += "\n"
    output += file[2647]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[2660:2670]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '23', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '23', file[2672])


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Invalid Game Menu Option

def TC_Exit_003():
    output = ""
    # Test ID
    output += file[2673]
    output += "\n"

    # Display Turn and Game Menu
    for i in file[2708:2722]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '24', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '24', file[2730])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Valid option for Main Menu.
def TC_SG_Exit_001():
    output = ""
    # Test ID
    output += file[2731]
    output += "\n"

    # Output after user input
    output += file[2666]
    output += "\n"
    output += file[2769]
    output += "\n"

    # Display Main Menu + Game Ended
    for i in file[2773:2783]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '25', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '25', file[2784])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Invalid option for Main Menu.

def TC_SG_Exit_002():
    output = ""
    # Test ID
    output += file[2785]
    output += "\n"

    # Display Grid
    for i in file[2797:2813]:
        output += i

    # Output after user input
    output += "\n"
    output += file[2820]
    output += "\n"

    # Display Main Menu + Output after user input
    for i in file[2836:2837]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '26', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '26', file[2838])


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Invalid option for Game Menu.

def TC_SG_Exit_003():
    output = ""
    # Test ID
    output += file[2849]
    output += "\n"

    # Display Turn and Game Menu
    for i in file[2865:2884]:
        output += i

    # Output after user input
    output += "\n"
    output += file[2884]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '27', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '27', file[2906])


# Description: Verify that user can see main menu
# Test Scenario ID: UAT_TS_MainMenu_001
# Test Data: NA

def UAT_TC_MainMenu_001():
    output = ""
    # Test ID
    output += file[2907]
    output += "\n"

    # Display Main Menu
    for i in file[2910:2920]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '2', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '2', file[2920])


# Description: Verify that user can select city size
# Test Scenario ID: TS_CitySize_001
# Test Data: Valid City Size

def UAT_TC_CitySize_001():
    output = ""
    # Test ID
    output += file[2921]
    output += "\n"

    # Display Main Menu, Options Menu and City Size
    for i in file[2924:2944]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '3', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '3', file[2955])


# Description: Verify that user can select city size
# Test Scenario ID: TS_CitySize_001
# Test Data: Invalid City Size

def UAT_TC_CitySize_002():
    output = ""
    # Test ID
    output += file[2956]
    output += "\n"

    # Display Main Menu, Options Menu and City Size
    for i in file[2970:2979]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '4', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '4', file[2990])


# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Valid Building Pool - 1,2,4,6,7

def UAT_TC_BuildingPool_001():
    output = ""
    # Test ID
    output += file[2991]
    output += "\n"

    # Display Current Building Pool
    for i in file[3014:3027]:
        output += i

    # Update Building Pool
    output += "\n"
    output += file[3027]
    output += "\n"

    # Display Updated Building Pool
    output += file[3043]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '5', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '5', file[3045])


# Description: Verify that user can select building pool
# Test Scenario ID: UAT_TS_BuildingPool_001
# Test Data: Invalid Building Pool - 1,2,8,9,10

def UAT_TC_BuildingPool_002():
    output = ""
    # Test ID
    output += file[3046]
    output += "\n"

    # Display Current Building Pool
    for i in file[3069:3082]:
        output += i

    # Update Building Pool
    output += "\n"
    output += file[3082]
    output += "\n"

    # Display Updated Building Pool
    output += file[3096]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '6', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '6', file[3098])


# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Valid Main Menu Option - 1

def UAT_TC_StartGame_001():
    output = ""
    # Test ID
    output += file[3099]
    output += "\n"

    # Display Main Menu and Selection Output (Including Grid and Game Menu)
    for i in file[3115:3134]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '7', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '7', file[3135])


# Description: Verify that user can a start a game
# Test Scenario ID: UAT_TS_StartGame_001
# Test Data: Invalid Main Menu Option - 5

def UAT_TC_StartGame_002():
    output = ""
    # Test ID
    output += file[3136]
    output += "\n"

    # Display Main Menu and Selection Output (Including Grid and Game Menu)
    for i in file[3148:3158]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '8', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '8', file[3160])


# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Valid Coordinate - A1

def UAT_TC_PlaceBuilding_001():
    output = ""
    # Test ID
    output += file[3161]
    output += "\n"

    # Display Turn and Grid
    for i in file[3196:3211]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '9', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '9', file[3219])


# Description: Verify that user can place building on desired coordinate
# Test Scenario ID: UAT_TS_PlaceBuilding_001
# Test Data: Invalid Coordinate - A9

def UAT_TC_PlaceBuilding_002():
    output = ""
    # Test ID
    output += file[3220]
    output += "\n"

    # Display Turn and Grid
    for i in file[3255:3269]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '10', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '10', file[3277])


# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Valid Coordinate - A1

def UAT_TC_BuildingCount_001():
    output = ""
    # Test ID
    output += file[3278]
    output += "\n"

    # Display Turn and Grid
    for i in file[3313:3328]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '11', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '11', file[3336])


# Description: Verify that user can see remaining building its count
# Test Scenario ID: UAT_TS_BuildingCount_001
# Test Data: Invalid Coordinate - A9

def UAT_TC_BuildingCount_002():
    output = ""
    # Test ID
    output += file[3337]
    output += "\n"

    # Display Turn and Grid
    for i in file[3372:3386]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '12', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '12', file[3394])


# Description: Verify that user can save game
# Test Scenario ID: UAT_TS_SaveGame_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 4

def UAT_TC_SaveGame_001():
    output = ""
    # Test ID
    output += file[3395]
    output += "\n"

    # Display Turn and Grid
    for i in file[3430:3444]:
        output += i

    # Output after user input
    output += "\n"
    output += file[3455]

    # Display Saved File
    output += "\n"
    for i in file[3478:3485]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '13', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '13', file[3487])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Valid Coordinate - A1, Valid Game Menu Option - 3

def UAT_TC_GameScore_001():
    output = ""
    # Test ID
    output += file[3488]
    output += "\n"

    # Display Turn and Grid
    for i in file[3523:3538]:
        output += i

    # Output after user input
    output += "\n"
    output += file[3545]

    # Display Score
    output += "\n"
    for i in file[3548:3555]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '16', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '16', file[3576])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Invalid Coordinate - A9, Valid Game Menu Option - 3

def UAT_TC_GameScore_002():
    output = ""
    # Test ID
    output += file[3577]

    # Display Turn and Grid
    output += "\n"
    for i in file[3612:3626]:
        output += i

    # Output after user input
    output += "\n"
    output += file[3633]

    # Display Score
    output += "\n"
    for i in file[3636:3642]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '17', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '17', file[3664])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_GameScore_001
# Test Data: Valid Coordinates

def UAT_TC_GameScore_003():
    output = ""
    # Test ID
    output += file[3665]

    # Display Grid Size
    output += "\n"
    for i in file[3679:3688]:
        output += i

    # Display EOGA
    output += "\n"
    for i in file[4311:4344]:
        output += i

    # View High Score from Main Menu
    output += "\n"
    for i in file[4345:4361]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '18', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '18', file[4372])


# Description: Verify that game score can be shown
# Test Scenario ID: UAT_TS_HighScore_001
# Test Data: Valid Main Menu Option - 3

def UAT_TC_HighScore_001():
    output = ""
    # Test ID
    output += file[4373]

    # View High Score from Main Menu
    output += "\n"
    for i in file[4376:4392]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[1]
    wks.update_value(uatFunctionalCol + '19', output)

    # Time Taken
    wks.update_value(uatFunctionalTime + '19', file[4401])


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
UAT_TC_GameScore_001()
UAT_TC_GameScore_002()
UAT_TC_GameScore_003()
UAT_TC_HighScore_001()