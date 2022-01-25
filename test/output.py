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
    for i in file[23:31]:
        output += i
    output += "\n"

    # Current Building Pool
    for i in file[44:52]:
        output += i

    # Update Building Pool
    output += "\n"
    output += file[56]
    output += "\n"
    output += file[57]

    # Updated Building Pool
    output += "\n"
    output += file[73]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[100:114]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '2', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '2', file[139])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_002():
    output = ""
    # Test ID
    output += file[140]
    output += "\n"

    # Update Grid Size
    for i in file[154:163]:
        output += i
    output += "\n"

    # Display Building Pool
    for i in file[175:188]:
        output += i

    # Output after user input
    output += "\n"
    output += file[204]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[231:243]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '3', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '3', file[268])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_003():
    output = ""
    # Test ID
    output += file[269]
    output += "\n"

    # Update City Size
    for i in file[283:292]:
        output += i
    output += "\n"

    # Current Building Pool
    for i in file[304:318]:
        output += i
    output += "\n"

    # Output after user input
    output += file[331]
    output += "\n"

    # Updated Building Pool
    output += file[267]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[358:372]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '4', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '4', file[380])


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_004():
    output = ""
    # Test ID
    output += file[381]
    output += "\n"

    # Update City Size
    for i in file[395:404]:
        output += i

    # Current Building Pool
    for i in file[416:430]:
        output += i

    # Output after user input
    output += "\n"
    output += file[443]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[470:482]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '5', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '5', file[490])


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Valid Coordinates

def TC_Grid_Fill_001():
    output = ""
    # Test ID
    output += file[491]
    output += "\n"

    # Display Turn and Grid
    for i in file[1116:1130]:
        output += i

    # Add user input when implemented
    output += "\n"
    for i in file[1137:1139]:
        output += i
    output += "\n"

    # Display Turn and Grid
    for i in file[1140:1154]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '6', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '6', file[1165])


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Inalid Coordinates

def TC_Grid_Fill_002():
    output = ""
    # Test ID
    output += file[1166]
    output += "\n"

    # Display Turn and Grid
    for i in file[1305:1321]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '7', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '7', file[1329])


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Valid coordinates

def TC_PB_BC_001():
    output = ""
    # Test ID
    output += file[1330]
    output += "\n"

    # Display Turn and Grid
    for i in file[1482:1497]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '8', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '8', file[1388])


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Invalid coordinates

def TC_PB_BC_002():
    output = ""
    # Test ID
    output += file[1389]
    output += "\n"

    # Display Turn and Grid
    for i in file[1424:1437]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '9', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '9', file[1446])


# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Valid coordinates

def TC_PB_SG_001():
    output = ""
    # Test ID
    output += file[1447]
    output += "\n"

    # Display Turn and Grid
    for i in file[1482:1496]:
        output += i

    # Output after user input
    output += "\n"
    output += file[1507]
    output += "\n"

    # Display Game File
    for i in file[1530:1536]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '10', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '10', file[1539])


# Description: Verifying the interaction between placing buildings and saving the game.
# Test Scenario ID: TS_PB_SG_001
# Test Data: Invalid coordinates

def TC_PB_SG_002():
    output = ""
    # Test ID
    output += file[1540]
    output += "\n"

    # Display Turn and Grid
    for i in file[1575:1588]:
        output += i

    # Output after user input
    output += "\n"
    output += file[1599]
    output += "\n"

    # Display Game File
    for i in file[1622:1628]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '10', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '10', file[1631])


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
    for i in file[1835:1841]:
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
    for i in file[1975:1981]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value(funtionalIntegrationCol + '17', output)

    # Time Taken
    wks.update_value(funtionalIntegrationTime + '17', file[2003])


# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Valid Game Menu Option / Valid Main Menu Option

# def TC_Exit_001():
#     output = ""
#     # Test ID
#     output += file[1336]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1349:1369]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1369]
#     output += "\n"

#     # Display Main Menu + Exit
#     for i in file[1370:1381]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '22', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '22', file[1382])


# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Valid Game Menu Option / Invalid Main Menu Option

# def TC_Exit_002():
#     output = ""
#     # Test ID
#     output += file[1383]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1396:1416]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1416]
#     output += "\n"

#     # Display Main Menu + Exit
#     for i in file[1418:1426]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1427]

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '23', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '23', file[1438])


# # Description: Verifying the interaction between exiting from both Game and Main menu
# # Test Scenario ID: TS_Exit_001
# # Test Data: Invalid Game Menu Option

# def TC_Exit_003():
#     output = ""
#     # Test ID
#     output += file[1439]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1452:1472]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1472]

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '24', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '24', file[1495])


# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Valid option for Game Menu and Valid option for Main Menu.
# def TC_SG_Exit_001():
#     output = ""
#     # Test ID
#     output += file[1496]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1509:1529]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1529]
#     output += "\n"

#     # Display Main Menu + Game Ended
#     for i in file[1530:1541]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '25', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '25', file[1542])


# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Valid option for Game Menu and Invalid option for Main Menu.

# def TC_SG_Exit_002():
#     output = ""
#     # Test ID
#     output += file[1543]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1556:1576]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1576]
#     output += "\n"

#     # Display Main Menu + Output after user input
#     for i in file[1577:1588]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '26', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '26', file[1598])


# # Description: Verifying the interaction between starting a new game and exit immediately
# # Test Scenario ID: TS_SG_Exit_001
# # Test Data: Valid option for Main Menu, Invalid option for Game Menu.

# def TC_SG_Exit_003():
#     output = ""
#     # Test ID
#     output += file[1599]
#     output += "\n"

#     # Display Turn and Game Menu
#     for i in file[1612:1632]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1632]
#     output += "\n"

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[2]
#     wks.update_value(funtionalIntegrationCol + '27', output)

#     # Time Taken
#     wks.update_value(funtionalIntegrationTime + '27', file[1655])


# def UAT_TC_MainMenu_001():
#     output = ""
#     # Test ID
#     output += file[1656]
#     output += "\n"

#     # Display Main Menu
#     for i in file[1659:1668]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '2', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '2', file[1668])


# def UAT_TC_BuildingPool_001():
#     output = ""
#     # Test ID
#     output += file[1669]
#     output += "\n"

#     # Display Current Building Pool
#     for i in file[1690:1703]:
#         output += i

#     # Update Building Pool
#     output += "\n"
#     output += file[1703]
#     output += "\n"

#     # Display Updated Building Pool
#     output += file[1717]
#     output += "\n"

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '4', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '4', file[1719])


# def UAT_TC_BuildingPool_002():
#     output = ""
#     # Test ID
#     output += file[1720]
#     output += "\n"

#     # Display Current Building Pool
#     for i in file[1741:1754]:
#         output += i

#     # Update Building Pool
#     output += "\n"
#     output += file[1754]
#     output += "\n"

#     # Display Updated Building Pool
#     output += file[1768]
#     output += "\n"

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '5', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '5', file[1770])


# def UAT_TC_StartGame_001():
#     output = ""
#     # Test ID
#     output += file[1771]
#     output += "\n"

#     # Display Main Menu and Selection Output (Including Grid and Game Menu)
#     for i in file[1774:1804]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '6', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '6', file[1805])


# def UAT_TC_StartGame_002():
#     output = ""
#     # Test ID
#     output += file[1806]
#     output += "\n"

#     # Display Main Menu and Selection Output (Including Grid and Game Menu)
#     for i in file[1809:1818]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '7', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '7', file[1828])


# def UAT_TC_PlaceBuilding_001():
#     output = ""
#     # Test ID
#     output += file[1829]
#     output += "\n"

#     # Display Turn and Grid
#     for i in file[1842:1855]:
#         output += i

#     # Add output of user input

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[1863:1876]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '8', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '8', file[1884])


# def UAT_TC_PlaceBuilding_002():
#     output = ""
#     # Test ID
#     output += file[1885]
#     output += "\n"

#     # Display Turn and Grid
#     for i in file[1898:1910]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[1918]

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[1920:1932]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '9', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '9', file[1941])


# def UAT_TC_BuildingCount_001():
#     output = ""
#     # Test ID
#     output += file[1942]
#     output += "\n"

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[1955:1968]:
#         output += i

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[1976:1989]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '10', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '10', file[1997])


# def UAT_TC_BuildingCount_002():
#     output = ""
#     # Test ID
#     output += file[1998]
#     output += "\n"

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2011:2023]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[2031]

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2033:2046]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '11', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '11', file[2054])


# def UAT_TC_SaveGame_001():
#     output = ""
#     # Test ID
#     output += file[2055]
#     output += "\n"

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2111:2124]:
#         output += i

#     # Display Saved File
#     output += "\n"
#     for i in file[2131:2138]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '12', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '12', file[2140])


# def UAT_TC_GameScore_001():
#     output = ""
#     # Test ID
#     output += file[2141]
#     output += "\n"

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2176:2188]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[2195]

#     # Display Score
#     output += "\n"
#     for i in file[2196:2203]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '15', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '15', file[2225])


# def UAT_TC_GameScore_002():
#     output = ""
#     # Test ID
#     output += file[2226]
#     output += "\n"

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2239:2252]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[2259]

#     # Display Turn and Grid
#     output += "\n"
#     for i in file[2261:2274]:
#         output += i

#     # Output after user input
#     output += "\n"
#     output += file[2281]

#     # Display Score
#     output += "\n"
#     for i in file[2282:2289]:
#         output += i

#     sh = gc.open('SimpCity Test Cases')
#     wks = sh[1]
#     wks.update_value(uatFunctionalCol + '16', output)

#     # Time Taken
#     wks.update_value(uatFunctionalTime + '16', file[2311])


TC_CS_BP_SG_001()
TC_CS_BP_SG_002()
TC_CS_BP_SG_003()
TC_CS_BP_SG_004()
TC_Grid_Fill_001()
TC_Grid_Fill_002()
TC_PB_BC_001()
TC_PB_BC_002()
TC_PB_DS_001()
TC_PB_DS_002()
# TC_Exit_001()
# TC_Exit_002()
# TC_Exit_003()
# TC_SG_Exit_001()
# TC_SG_Exit_002()
# TC_SG_Exit_003()

# UAT_TC_MainMenu_001()
# UAT_TC_BuildingPool_001()
# UAT_TC_BuildingPool_002()
# UAT_TC_StartGame_001()
# UAT_TC_StartGame_002()
# UAT_TC_PlaceBuilding_001()
# UAT_TC_PlaceBuilding_002()
# UAT_TC_BuildingCount_001()
# UAT_TC_BuildingCount_002()
# UAT_TC_SaveGame_001()
# UAT_TC_GameScore_001()
# UAT_TC_GameScore_002()
