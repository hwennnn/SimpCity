import pygsheets
gc = pygsheets.authorize(service_file='/Users/yongtenggg/Downloads/modular-sign-296911-116ce6ea3ff9.json')

f = open("output.txt", "r")
file = f.readlines()

# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=2:2

def TC_CS_BP_SG_001():
    # Add City Size Output

    output = ""
    # Test ID
    output += file[9]
    output += "\n"

    # Current Building Pool
    output += file[42]
    output += "\n"

    # Output after user input
    output += file[43]
    output += "\n"

    # Updated Building Pool
    output += file[57]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[80:93]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J2', output)


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Valid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_002():
    # Add City Size Output

    output = ""
    # Test ID
    output += file[112]
    output += "\n"

    # Current Building Pool
    output += file[145]
    output += "\n"
    
    # Output after user input
    output += file[146]
    output += "\n"

    # Updated Building Pool
    output += file[160]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[183:196]:
        output += i
    
    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J3', output)


# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Valid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_003():
    # Add City Size Output

    output = ""
    # Test ID
    output += file[215]
    output += "\n"

    # Current Building Pool
    output += file[248]
    output += "\n"

    # Output after user input
    output += file[249]
    output += "\n"

    # Updated Building Pool
    output += file[263]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[286:299]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J4', output)

# Description: Verifying the interaction between selecting city size, selecting building pool and starting game
# Test Scenario ID: TS_CS_BP_SG_001
# Test Data: Invalid City Size / Invalid Building Pool
# Link to Test: https://docs.google.com/spreadsheets/d/1j9zOtrntEV0F12utHqEf2nbwmaoZZrfxYVwqXxvVVEs/edit?pli=1#gid=768609166&range=3:3

def TC_CS_BP_SG_004():
    # Add City Size Output

    output = ""
    # Test ID
    output += file[306]
    output += "\n"

    # Current Building Pool
    output += file[339]
    output += "\n"

    # Output after user input
    output += file[340]
    output += "\n"

    # Updated Building Pool
    output += file[354]
    output += "\n"

    # Display Grid to check if remaining building is using updated building pool
    for i in file[377:390]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J5', output)


# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Valid Coordinates

def TC_Grid_Fill_001():
    output = ""
    # Test ID
    output += file[397]
    output += "\n"

    # Turns
    output += file[715]
    output += "\n"

    # Display Grid
    for i in file[717:728]:
        output += i

    # Add user input when implemented

    # Turns
    output += file[736]
    output += "\n"

    # Display Grid
    for i in file[738:749]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J6', output)

# Type: Functional
# Description: Verifying the possibility of filling the grid with buildings
# Test Scenario ID: TS_Grid_Fill_001
# Test Data: Inalid Coordinates

def TC_Grid_Fill_002():
    output = ""
    # Test ID
    output += file[756]
    output += "\n"
    # Turns
    output += file[825]
    output += "\n"

    # Display Grid
    for i in file[827:845]:
        output += i

    output += "\n"
    # Output after user input
    output += file[845]
    output += "\n"

    # Turns
    output += file[847]
    output += "\n"

    # Display Grid
    for i in file[849:860]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J7', output)


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Valid coordinates

def TC_PB_BC_001():
    output = ""
    # Test ID
    output += file[867]
    output += "\n"
    
    # Turns
    output += file[870]
    output += "\n"

    # Display Grid
    for i in file[872:883]:
        output += i

    # Add user input when implemented
    output += "\n"

    # Turns
    output += file[891]
    output += "\n"

    # Display Grid
    for i in file[893:904]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J8', output)


# Description: Verifying the interaction between placing buildings and remaining building count
# Test Scenario ID: TS_PB_BC_001
# Test Data: Invalid coordinates

def TC_PB_BC_002():
    output = ""
    # Test ID
    output += file[911]
    output += "\n"
    
    # Turns
    output += file[914]
    output += "\n"

    # Display Grid
    for i in file[916:927]:
        output += i

    # Output after user input
    output += "\n"
    output += file[934]
    output += "\n"

    # Turns
    output += file[936]
    output += "\n"

    # Display Grid
    for i in file[938:949]:
        output += i

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J9', output)


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Valid coordinates
def TC_PB_DS_001():
    output = ""
    # Test ID
    output += file[956]
    output += "\n"

    # Turns
    output += file[1127]
    output += "\n"

    # Display Grid
    for i in file[1129:1140]:
        output += i

    # Output after user input
    output += file[1147]
    output += "\n"

    # Display Score
    for i in file[1148:1155]:
        output += i

    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J16', output)


# Description: Verifying the interaction between placing buildings and the viewing of game score
# Test Scenario ID: TS_PB_DS_001
# Test Data: Invalid coordinates

def TC_PB_DS_002():
    output = ""
    # Test ID
    output += file[1176]
    output += "\n"

    # Turns ID
    output += file[1245]
    output += "\n"

    # Display Grid
    for i in file[1247:1258]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1287]
    output += "\n"

    # Display Score
    for i in file[1288:1295]:
        output += i

    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J17', output)


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Valid Main Menu Option

def TC_Exit_001():
    output = ""
    # Test ID
    output += file[1316]
    output += "\n"

    # Display Game Menu
    for i in file[1343:1348]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1349]
    output += "\n"

    # Output after user input
    output += file[1350]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[1352:1359]:
        output += i

    # Add user input when implemented
    output += "\n"

    # Game Ended
    output += file[1360]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J22', output)


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Valid Game Menu Option / Invalid Main Menu Option

def TC_Exit_002():
    output = ""
    # Test ID
    output += file[1361]
    output += "\n"

    # Display Game Menu
    for i in file[1388:1393]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1394]
    output += "\n"

    # Output after user input
    output += file[1395]
    output += "\n"

    # Display Main Menu + Exit
    for i in file[1397:1403]:
        output += i

    output += file[1405]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J23', output)


# Description: Verifying the interaction between exiting from both Game and Main menu
# Test Scenario ID: TS_Exit_001
# Test Data: Invalid Game Menu Option

def TC_Exit_003():
    output = ""
    # Test ID
    output += file[1415]
    output += "\n"

    # Display Game Menu
    for i in file[1442:1447]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1448]
    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J24', output)


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Valid option for Main Menu.
def TC_SG_Exit_001():
    output = ""
    # Test ID
    output += file[1470]
    output += "\n"

    # Display Game Menu
    for i in file[1497:1502]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1503]
    output += "\n"

    # Output after user input
    output += file[1504]
    output += "\n"

    # Display Main Menu + Game Ended
    for i in file[1506:1515]:
        output += i

    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J25', output)


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Valid option for Game Menu and Invalid option for Main Menu.

def TC_SG_Exit_002():
    output = ""
    # Test ID
    output += file[1515]
    output += "\n"

    # Display Game Menu
    for i in file[1542:1547]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1548]
    output += "\n"

    # Output after user input
    output += file[1549]
    output += "\n"

    # Display Main Menu + Output after user input
    for i in file[1551:1560]:
        output += i

    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J26', output)


# Description: Verifying the interaction between starting a new game and exit immediately
# Test Scenario ID: TS_SG_Exit_001
# Test Data: Valid option for Main Menu, Invalid option for Game Menu.

def TC_SG_Exit_003():
    output = ""
    # Test ID
    output += file[1569]
    output += "\n"

    # Display Game Menu
    for i in file[1596:1601]:
        output += i

    output += "\n"

    # Output after user input
    output += file[1602]
    output += "\n"

    output += "\n"

    sh = gc.open('SimpCity Test Cases')
    wks = sh[2]
    wks.update_value('J27', output)


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
TC_Exit_001()
TC_Exit_002()
TC_Exit_003()
TC_SG_Exit_001()
TC_SG_Exit_002()
TC_SG_Exit_003()





