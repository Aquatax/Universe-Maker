# Goal of this file is to be where the input command is and will lead to the other files
from galaxymaker import galaxymakerr  # This is to allow for galaxy generation
import planetmaker  # This is for planet generation
import os  # This is to help with clearing the screen
import player  # This created the player character
from formulas import planetnumber, planetletter  # This is used to convert b to 2 and 2 to b
import random  # Math
from tkinter import *  # For the GUI
from tkinter.ttk import *  # For the GUI
from shipbattle import battle  # For the ship battle
from shipbuilder import maksship  # to Generalte the ship for battle


def clearscreen(Windows):
    # This clears the screen. It works with def changeos to work on both linux and windows without crashing
    if Windows.lower() == "yes":
        myvalue = os.system('cls')
    else:
        myvalue = os.system('clear')
    if myvalue != 0 and Windows.lower() == "yes":
        changeos("Windows")
    elif myvalue != 0 and Windows.lower() == "no":
        changeos("Linux")


def changeos(fromwhere):
    # This will change the operating system from windows to linux or visa versa to clear screen correctly
    global Windows
    if fromwhere == "Windows":
        Windows = "no"
    if fromwhere == "Linux":
        Windows = "yes"
    clearscreen(Windows)


def helpcommand():
    # This is the help command and activated with /help in the console
    print('''
    The Following are usable commands
    Begin commands with a /

    /help
    -provides information on commands

    /make (planet/galaxy/moon/help) (input1) (input2) (input3)
    -allows you to make a galaxy, planet, or moon
    /make galaxy (minimum systems) (include moons: True/False)
    /make planet (forceplanettype: random, 1, 2, 3, 4, 5) (include moons: True/False)
    /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5
    /system info
    --Lets you see the planets in a system along with nearby system
    
    /planet info
    --lets you see a summary of the planet. use /goto to first go to the plane
    
    /goto [system/planet] [number/letter]
    --Lets you go to that system or planet. 
    
    /changeos
    --important to clear the screen properly. Use "Yes" or "No. use this if you chose the wrong one
    ''')


def makecommand(input1="help", input2="help", input3="help", input4=True):
    # This will create a planet for fun. Does not affect the game, but may be useful for planet stats
    # When making one from scratch
    # Will be used at start to make the galaxy though
    x = planetmaker.makeplanet()
    try:
        if input1 == "planet":
            if input2 != "random" and input2 != "1" and input2 != "2" and input2 != "3" and input2 != "4" and \
                    input2 != "5" and input2 == "help" and input2 != "0":
                print('''
                Accepted Planet Values:
                random: Will Generate a Random Planet
                0:      Will Generate a Random Planet
                1:      Will Generate a Dwarf Planet
                2:      Will Generate a Rocky Planet
                3:      Will Generate a Super Earth
                4:      Will Generate a Ice Giant
                5:      Will Generate a Gas Giant
                example for a rocky planet with moons:
                /make planet 2 True
                
                ''')
            else:
                if input2 == "0":
                    input2 = "random"
                elif input2 == "1":
                    input2 = "Dwarf Planet"
                elif input2 == "2":
                    input2 = "Rocky Planet"
                elif input2 == "3":
                    input2 = "Super Earth"
                elif input2 == "4":
                    input2 = "Ice Giant"
                elif input2 == "5":
                    input2 = "Gas Giant"
                # Will generate a planet with or without moons as desired. Also can force the planet type
                answer = x.planetfactory(include_moons=input3, forceplanettype=input2)
                for x in answer:
                    print(f"{x}: {answer[x]}")
                saveplanet = input("Should this be saved to a file? t/f: ").lower()
                if saveplanet == "t":
                    json_object = json.dumps(answer, default=lambda o: o.__dict__, sort_keys=False, indent=4)

                    try:
                        with open('myplanet.json', 'w') as fp:
                            fp.write(json_object)
                    except:
                        # print("BROKE HERE")
                        pass
                else:
                    pass

            return ()
        elif input1 == "moon":
            # Will return a moon sample that can be used for other purposes
            newmoon = x.moonfactory(moontype=input2, moonversion=2)
            print(newmoon)
            contmoon = input("Should the moon be saved to a file? y/n:")
            if contmoon.lower() == "y":
                json_object = json.dumps(newmoon, default=lambda o: o.__dict__, sort_keys=False, indent=2)

                try:
                    with open('myMoon.json', 'w') as fp:
                        fp.write(json_object)
                except:
                    print("BROKE HERE")
                    pass

        elif input1 == "galaxy":
            # print("GOT HERE")
            # Will generate a new galaxy and save it to the game file
            playership.system = "system1"
            galaxydict = galaxymakerr(include_moons=input3, minimum_systems=float(input2))
            # import json
            global galaxy
            # Serializing json

            # print(json_object)
            if not input4:
                json_object = json.dumps(galaxydict, default=lambda o: o.__dict__, sort_keys=False, indent=2)

                try:
                    with open('systems.json', 'w') as fp:
                        fp.write(json_object)
                except:
                    print("BROKE HERE")
                    pass
            galaxy = galaxydict
            return

        else:
            print('''
            /make (planet/galaxy/moon/help) (input1) (input2) (input3)
            -allows you to make a galaxy, planet, or moon
            /make galaxy (minimum systems) (include moons: True/False)
            /make planet (forceplanettype: random) (include moons: True/False)
            /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5)

            ''')
    except(KeyError, ValueError):
        print('''
            /make (planet/galaxy/moon/help) (input1) (input2) (input3)
               -allows you to make a galaxy, planet, or moon
            /make galaxy (minimum systems) (include moons: True/False)
            /make planet (forceplanettype: random) (include moons: True/False)
            /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5)

                    ''')
        return


def shipcommand(input1="help", input2="help", input3="help", input4="help"):
    global Windows
    # clearscreen(Windows)
    if input1 == "info":
        print(f"Crew={playership.ship.crew}/{playership.ship.crewcapacity}")
        print(f"Ship Type={playership.ship.size} {playership.ship.shiptype}")
        print(f"Health={playership.ship.health}/{playership.ship.maxhealth}")
        print(f"Ammo={playership.ship.ammo}/{playership.ship.maxammo}")
        print(f"Inventory={playership.ship.inventory}")
        # clearscreen(Windows)
    elif input1 == "battle":
        cpromptbattle()
    elif input1 == "refill":
        shiprefill()
    elif input1 == "generate":
        if input2 == "trader" or input2 == "warship" or input2 == "diplomat" or input2 == "transport":
            if input3 == "small" or input3 == "medium" or input3 == "large" or input3 == "massive":
                playership.ship = maksship(size=input3, shiptype=input2)
            else:
                playership.ship = maksship(size="random", shiptype=input2)
        else:
            if input3 == "small" or input3 == "medium" or input3 == "large" or input3 == "massive":
                playership.ship = maksship(size=input3, shiptype="random")
            else:
                playership.ship = maksship(size="random", shiptype="random")
        clearscreen(Windows)
        shipcommand(input1="info")
    else:
        print('''
        /ship info -----------------------------------  Displays player ship stats
        /ship battle  --------------------------------  Begins a battle
        /ship refill  --------------------------------  Resets crew, health, and ammo
        /ship generate [ship class] [ship size] ------  Will change player ship to new ship
           Classes: trader, transport, warship, diplomat, random
           Sizes: small, medium, large, massive, random
        ''')


def systemcommand(input1="help", input2="help", input3="help", input4="help"):
    global Windows
    clearscreen(Windows)
    current_system = playership.system
    if input1 == "info":
        links = "links"
        name = "Name"
        print(f"System Name: {galaxy[current_system][name]}")
        print(f"Nearby Systems: {galaxy[current_system][links]}")
        current_planet = 1
        current_spot = 1
        numberofstars = 0
        for x in galaxy[current_system]["stars"]:
            numberofstars += 1
        print(f"Number of Stars: {numberofstars}")
        print(f"Number of Planets: {len(galaxy[current_system]['planets'])}")

        if len(galaxy[current_system]["planets"]) == 0:
            print("No Planets in this system")
        # this goes through the list that holds the planets. each version of X holds the entire planet data
        for x in galaxy[current_system]["planets"]:
            print(eval(planetpath)[name] + "; " + eval(planetpath)["Type"])
            current_spot += 1

    elif input1.lower == "help":
        print("Guide for the `System` command")
        print("Format: /system info")
        print("This will provide some information about the current system")


def gotocommand(input1="help", input2="help"):
    if input1.lower() == "system":

        current_system = playership.system
        for x in galaxy[current_system]["links"]:
            if x == int(input2):
                playership.system = "system" + str(x)
                name = "Name"
                print(f"Player is now in System {x}: {galaxy[playership.system][name]}")
                playership.planet = "None"
                return

        print("System not connected!")

        changesystem()
    elif input1.lower() == "planet":
        # print("HERE")
        playership.planet = "planet" + input2
        current_system = playership.system
        current_planet = playership.planet
        current_spot = planetnumber(current_planet[-1])
        try:
            if len(galaxy[current_system]["planets"]) < current_spot - 1:
                playership.planet = "None"
                print("Planet does not exist")
            else:
                print(f"Now at {playership.planet}")
                pass

        except(TypeError):
            pass
    else:
        print('''
        /goto Help Page
        usage: /goto [system/planet] [system number/planet letter]

        /goto system [system number]
        You can go to any system connected to the current one. This can be found doing /system info
        example: /goto system 9

        /goto planet [planet letter]
        You can go to any planet within the current system. take the letter at the end of the planet name
        e.g. planet name is PiHN60b
        example: /goto planet b


        ''')


def cpromptbattle():
    beginbattle()
    global ship1
    global ship2
    global newbattle
    global cont
    while cont:
        print('''
        Commands:
        a = Attack
        b = Board
        r = Retreat
        s = Surrender
        ''')
        command = input("=")
        command = command.lower()
        cont = battlecommand(command, fromscreen=0)


def beginbattle():
    global ship1
    global ship2
    global newbattle
    global cont

    ship2 = maksship()
    ship1 = playership.ship
    shiprefill()
    clearscreen(Windows)
    print(f"Health: Player {ship1.health} = {ship2.health} Enemy")
    print(f"Ammo: Player {ship1.ammo} = {ship2.ammo} Enemy")
    print(f"Crew: Player {ship1.crew} = {ship2.crew} Enemy")
    newbattle = battle(ship1, ship2)
    newbattle.retreat = 0
    cont = True


def battlecommand(command, fromscreen=1):
    global ship1
    global ship2
    global newbattle
    global cont

    os.system('cls')
    print(f"Health: Player {ship1.health} = {ship2.health} Enemy")
    print(f"Ammo: Player {ship1.ammo} = {ship2.ammo} Enemy")
    print(f"Crew: Player {ship1.crew} = {ship2.crew} Enemy")
    # command = input("=")
    commandreturn = newbattle.commands(ship1, ship2, cont, command)
    ship1 = commandreturn[0]
    ship2 = commandreturn[1]
    if (ship2.health <= 0 or ship2.crew <= ship1.crew * 0.25) and cont:
        print("You Won")
        cont = False
    if (ship1.health <= 0 or ship1.crew <= ship2.crew * 0.25) and cont:
        cont = False
        print("You Lost")
    if newbattle.retreat == 1:
        cont = False
    elif newbattle.retreat == 2:
        cont = False
    artyreturn = newbattle.arty(ship1, ship2, cont)
    try:
        ship1 = artyreturn[0]
        ship2 = artyreturn[1]

    except TypeError:
        if fromscreen == 1:
            resetlowerbuttons()
            # clearscreen(Windows)
            return
        else:
            cont = False
            return cont

    if (ship1.health <= 0 or ship1.crew <= ship2.crew * 0.25) and cont:
        cont = False
        print("You Lost")
    if (ship2.health <= 0 or ship2.crew <= ship1.crew * 0.25) and cont:
        print("You Won")
        cont = False
    if fromscreen == 0:
        return cont
    elif fromscreen == 1 and cont == False:
        resetlowerbuttons()
        print("Game Over")


def planetcommand(input1="help", input2="help"):
    if input1 == "info":
        current_planet = playership.planet
        current_system = playership.system
        # Current_planet example is planetb
        if current_planet == "None":
            print("No Planet Selected. First use /goto planet [planet letter]")
        else:
            current_spot = planetnumber(current_planet[-1])
            # Current_spot example is a integer, eg. b == 1, d == 3
            try:
                planet = eval(planetpath)
                print(f"""Name: {planet["Name"]}""")
                print(f"""Gravity: {planet["Gravity"]}""")
                print(f"""Classification: {planet["Type"]}""")
                print(f"""Subtype: {planet["Subtype"]}""")
                print(f"""Settled: {planet["Settled"]}""")
            except(TypeError):
                print("Planet Does Not Exist")
    elif input1 == "scan":
        current_planet = playership.planet
        current_system = playership.system
        # Current_planet example is planetb
        if current_planet == "None":
            print("No Planet Selected. First use /goto planet [planet letter]")
        else:
            current_spot = planetnumber(current_planet[-1])
            # Current_spot example is a integer, eg. b == 1, d == 3
            try:
                planet = eval(planetpath)
                # print(f"""Name: {planet["Core"]}""")
                for value in planet["Core"]:
                    if value == "crust":
                        highestvalue = ""
                        for element in planet["Core"]["crust"]:
                            if highestvalue == "":
                                highestvalue = element
                            if planet["Core"]["crust"][element] > planet["Core"]["crust"][highestvalue]:
                                highestvalue = element
                        print(f'''Most abundant resource is {highestvalue} at {planet["Core"]["crust"][highestvalue]
                        }%''')
                    elif value == "atmo":
                        highestvalue = ""
                        for element in planet["Core"]["atmo"]:
                            if highestvalue == "":
                                highestvalue = element
                            if planet["Core"]["atmo"][element] > planet["Core"]["atmo"][highestvalue]:
                                highestvalue = element
                        print(f'''Most abundant resource is {highestvalue} at {planet["Core"]["atmo"][highestvalue
                        ]}%''')
            except(TypeError):
                print("Planet Does Not Exist")
    elif input1.lower() == "mine":
        current_planet = playership.planet
        current_system = playership.system
        # Current_planet example is planetb
        if current_planet == "None":
            print("No Planet Selected. First use /goto planet [planet letter]")
        else:
            current_spot = planetnumber(current_planet[-1])
            # Current_spot example is a integer, eg. b == 1, d == 3
            try:
                planet = eval(planetpath)
                # print(f"""Name: {planet["Core"]}""")
                for value in planet["Core"]:
                    if value == "crust":
                        highestvalue = ""
                        for element in planet["Core"]["crust"]:
                            if highestvalue == "":
                                highestvalue = element
                            if planet["Core"]["crust"][element] > planet["Core"]["crust"][highestvalue]:
                                highestvalue = element
                            elementrating = planet["Core"]["crust"][highestvalue]
                    elif value == "atmo":
                        highestvalue = ""
                        for element in planet["Core"]["atmo"]:
                            if highestvalue == "":
                                highestvalue = element
                            if planet["Core"]["atmo"][element] > planet["Core"]["atmo"][highestvalue]:
                                highestvalue = element
                            elementrating = planet["Core"]["atmo"][highestvalue]

                print(f"{playership.ship.inventory}")
                total_used_space = 0
                for x in playership.ship.hold:
                    total_used_space += playership.ship.hold[x]

                randomvalue = random.randint(0, 100)
                if randomvalue <= elementrating:
                    if (total_used_space + round(randomvalue / 10, 2)) <= playership.ship.inventory:
                        playership.ship.hold[highestvalue] += round(randomvalue / 10, 2)
                        playership.ship.hold[highestvalue] = round(playership.ship.hold[highestvalue], 2)
                    elif total_used_space < playership.ship.inventory:
                        additionalspace = playership.ship.inventory - total_used_space
                        playership.ship.hold[highestvalue] += round(additionalspace, 2)
                        playership.ship.hold[highestvalue] = round(playership.ship.hold[highestvalue], 2)
                    else:
                        print(f"Not Enough Space. Max Storage: {playership.ship.inventory}")
                else:
                    if total_used_space == playership.ship.inventory:
                        print(f"Not Enough Space. Max Storage: {playership.ship.inventory}")
                    else:
                        print("Mining Failed")
                for x in playership.ship.hold:
                    if playership.ship.hold[x] > 0:
                        print(f"{x}: {playership.ship.hold[x]}")
            except(TypeError):
                print("Planet Does Not Exist")
    else:
        print('''
        /planet Help Page
        usage: /planet [info]

        /planet info 
        -Will show you a summary of the planet


        ''')


print("Welcome to Galaxy Creator")
print("Use / to start a command. Try /help")
answer = "Hi"



# makecommand("galaxy", "100", "False")
import json

with open('systems.json') as json_file:
    galaxy = json.load(json_file)

with open('player.json') as playerfile:
    loadingplayer = json.load(playerfile)

playership = player.Player(reloading=loadingplayer)
# print(playership.ship.crew)
def ignorethis():
    pass


# \/  Whether this is a Windows machine or not doesnt matter, it will adjust istelf after the first command
Windows = "yes"


def resetlowerbuttons():
    # clearscreen(Windows)
    for x in range(9, 17):
        newstring = f'''btn{x}.configure(text=f" ", command=ignorethis)'''
        exec(newstring)



#
def changesystem():
    # resetlowerbuttons()
    current_system = playership.system
    a = 9
    for a in range(0, 8):
        a += 9
        try:
            code = a - 9
            x = galaxy[current_system]["links"][code]

            newstring = f'''btn{a}.configure(text=f"System {x}", command=lambda: changesystemupdate(input2={x}))'''
            exec(newstring)
        except:

            newstring = f'''btn{a}.configure(text=f" ", command=ignorethis)'''
            exec(newstring)


def changeplanets():
    # clearscreen(Windows)
    resetlowerbuttons()
    current_system = playership.system
    planetlist = galaxy[current_system]["planets"]
    # print(planetlist)
    planetcode = 1
    for x in range(0, len(planetlist)):
        myplanet = "planet" + str(planetcode)
        planetvalue = planetletter(planetcode)
        # print(planetvalue)
        planetcode += 1
        # print(myplanet)
        newstring = f'''btn{x + 9}.configure(text=f"{myplanet.upper()}", command=lambda: gotocommand(input1="planet", 
        input2="{planetvalue}"))'''
        exec(newstring)
    # for a in range(1, 9):
    #     a += 8
    #     try:
    #         code = a - 8
    #         x = planetlist[code]
    #
    #         newstring = f'''btn{a}.configure(text=f"Planet {x}", command=ignorethis)'''
    #         exec(newstring)
    #     except:
    #
    #         newstring = f'''btn{a}.configure(text=f" ", command=ignorethis)'''
    #         exec(newstring)


def changesystemupdate(input2):
    gotocommand(input1="system", input2=input2)
    changesystem()


def totravel():
    resetlowerbuttons()
    btn9.configure(text="Change System", command=changesystem)
    btn10.configure(text="Change Planet", command=changeplanets)


# In order to use the Planet Path, you must first share two things. current_system is provided at the start of the
# for loop. The second is current_spot. current spot is the position of the planet. The first planet has a
# current_spot of 1. You can get the spot of the planet by doing the planetnumber() function
# example use of planetpath: eval(planetpath)["Name"]
planetpath = 'galaxy[current_system]["planets"][current_spot - 1]["planet" + str(str(current_spot))]'


def systembutton():
    resetlowerbuttons()
    btn9.configure(text="Help", command=lambda: systemcommand(input1="help"))
    btn10.configure(text="System Stats", command=lambda: systemcommand(input1="info"))
    pass


def planetbutton():
    resetlowerbuttons()
    btn9.configure(text="Planet Information", command=lambda: planetcommand(input1="info"))
    btn10.configure(text="Scan Planet", command=lambda: planetcommand(input1="scan"))
    btn11.configure(text="Mine Crust", command=lambda: planetcommand(input1="mine"))
    pass


def shipbutton():
    resetlowerbuttons()
    btn9.configure(text="Simulate Battle", command=lambda: shipbattlebutton())
    btn10.configure(text="Refill Stats", command=lambda: shiprefill())
    btn11.configure(text="Generate Ship", command=lambda: shipgeneratebutton())
    btn12.configure(text="Player Info", command=lambda: shipcommand(input1="info"))


def shipbattlebutton():
    beginbattle()
    resetlowerbuttons()
    btn9.configure(text="Attack", command=lambda: battlecommand(command="a"))
    btn10.configure(text="Board", command=lambda: battlecommand(command="b"))
    btn11.configure(text="Retreat", command=lambda: battlecommand(command="r"))
    btn12.configure(text="Surrender", command=lambda: battlecommand(command="s"))


def shiprefill():
    playership.ship.health = playership.ship.maxhealth
    playership.ship.ammo = playership.ship.maxammo
    playership.ship.crew = playership.ship.crewcapacity
    clearscreen(Windows)
    print("Player Ship Stats Reset")
    print(f'''
    Health = {playership.ship.health}
    Ammo = {playership.ship.ammo}
    Crew = {playership.ship.crew}
    
    
    ''')


def shipgeneratebutton():
    resetlowerbuttons()
    btn9.configure(text="Random", command=lambda: shipgeneratebutton2(shipclass="random"))
    btn10.configure(text="Trader", command=lambda: shipgeneratebutton2(shipclass="trader"))
    btn11.configure(text="Warship", command=lambda: shipgeneratebutton2(shipclass="warship"))
    btn12.configure(text="Diplomat", command=lambda: shipgeneratebutton2(shipclass="diplomat"))
    btn13.configure(text="Transport", command=lambda: shipgeneratebutton2(shipclass="transport"))


def shipgeneratebutton2(shipclass):
    resetlowerbuttons()
    btn9.configure(text="Random", command=lambda: shipgeneratebutton3(shipclass=shipclass, shipsize="random"))
    btn10.configure(text="Small", command=lambda: shipgeneratebutton3(shipclass=shipclass, shipsize="small"))
    btn11.configure(text="Medium", command=lambda: shipgeneratebutton3(shipclass=shipclass, shipsize="medium"))
    btn12.configure(text="Large", command=lambda: shipgeneratebutton3(shipclass=shipclass, shipsize="large"))
    btn13.configure(text="Massive", command=lambda: shipgeneratebutton3(shipclass=shipclass, shipsize="massive"))


def shipgeneratebutton3(shipclass, shipsize):
    resetlowerbuttons()
    shipcommand(input1="generate", input2=shipclass, input3=shipsize)
    resetlowerbuttons()

def settingsbutton():
    resetlowerbuttons()
    btn9.configure(text="Save Game", command=lambda: savegame())
    btn10.configure(text="Load Game", command=lambda: loadgame())
    btn11.configure(text="New Galaxy", command=lambda: regenerategalaxyv2())

def regenerategalaxy(starcount):
    global playership

    makecommand(input1="galaxy", input2=str(starcount), input3="True", input4=False)
    playership = player.Player()
    print("New Galaxy Generated. Remember to Save the galaxy to keep changes")

def regenerategalaxyv2():
    btn9.configure(text="Small", command=lambda: regenerategalaxy(50))
    btn10.configure(text="Medium", command=lambda: regenerategalaxy(100))
    btn11.configure(text="Large", command=lambda: regenerategalaxy(200))

def loadgame():
    global galaxy
    global playership
    with open('systems.json') as json_file:
        galaxy = json.load(json_file)

    with open('player.json') as playerfile:
        loadingplayer = json.load(playerfile)

    playership = player.Player(reloading=loadingplayer)
def savegame():
    newsave = playership.saveship()
    json_object = json.dumps(newsave, default=lambda o: o.__dict__, sort_keys=False, indent=4)

    try:
        with open('player.json', 'w') as fp:
            fp.write(json_object)
            print("Playerdata Saved")
    except:
        # print("BROKE HERE")
        print("Playerdata Failed to Save. Please submit save file")
        pass

    json_object = json.dumps(galaxy, default=lambda o: o.__dict__, sort_keys=False, indent=2)

    try:
        with open('systems.json', 'w') as fp:
            fp.write(json_object)
            print("Galaxy Saved")
    except:
        print("Galaxy Failed to Save. Please Submit Save File")
        pass

def console():
    while True:
        # No Touch \/
        current_system = playership.system

        # No Touch /\

        command = input("Input Command:")
        clearscreen(Windows)
        try:
            command[0].lower()
            if command[0] == "/" or command.lower() == "exit":
                command = command.split()
                spot = 0
                for value in command:
                    if value == "True":
                        command[spot] = True
                    elif value.lower() == "false":
                        command[spot] = False
                    spot += 1

                if command[0].lower() == "/help":
                    helpcommand()
                    input("Any button to continue")
                elif command[0] == "/make":

                    command.append("vacantslot")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    answer = makecommand(command[1], command[2], command[3])
                elif command[0] == "/ship":
                    command.append("vacantslot")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    shipcommand(command[1], command[2], command[3])
                elif command[0] == "/system":
                    command.append("vacantslot")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    systemcommand(command[1], command[2], command[3])
                elif command[0] == "/goto":
                    command.append("vacantslot")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    gotocommand(command[1], command[2])
                elif command[0] == "/planet":
                    # print("HERE")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    command.append("vacantslot")
                    planetcommand(command[1], command[2])


                elif command[0].lower() == "/exit" or command[0].lower() == "exit":
                    break

        except(IndexError):
            pass


window = Tk()
window.title("Galactic Explorer")
window.config(padx=100, pady=50)

window2 = Tk()
window2.title("Galactic Explorer")
window2.config(padx=100, pady=50)


canvas = Canvas(window, width=1000, height=1000, highlightthickness=0)

newcanvas = Canvas(window2, width=2000, height=1000, highlightthickness=0)
Label(newcanvas, text="You can modify this text", font='Helvetica 18 bold').pack()

# Upper Buttons
btn1 = Button(canvas, text="Travel", command=lambda: totravel(), width=15)
btn1.grid(column=0, row=0)
btn2 = Button(canvas, text="System", command=systembutton, width=15)
btn2.grid(column=1, row=0)
btn3 = Button(canvas, text="Planet", command=planetbutton, width=15)
btn3.grid(column=2, row=0)
btn4 = Button(canvas, text="Ship", command=shipbutton, width=15)
btn4.grid(column=3, row=0)
btn5 = Button(canvas, text="Crew", command=ignorethis, width=15)
btn5.grid(column=4, row=0)
btn6 = Button(canvas, text="Starbase", command=ignorethis, width=15)
btn6.grid(column=5, row=0)
btn7 = Button(canvas, text="Settings", command=settingsbutton, width=15)
btn7.grid(column=6, row=0)
btn8 = Button(canvas, text="Console", command=console, width=15)
btn8.grid(column=7, row=0)
# Lower Buttons
btn9 = Button(canvas, text="", command=lambda: ignorethis(), width=15)
btn9.grid(column=0, row=1)
btn10 = Button(canvas, text="", command=ignorethis, width=15)
btn10.grid(column=1, row=1)
btn11 = Button(canvas, text="", command=ignorethis, width=15)
btn11.grid(column=2, row=1)
btn12 = Button(canvas, text="", command=ignorethis, width=15)
btn12.grid(column=3, row=1)
btn13 = Button(canvas, text="", command=ignorethis, width=15)
btn13.grid(column=4, row=1)
btn14 = Button(canvas, text="", command=ignorethis, width=15)
btn14.grid(column=5, row=1)
btn15 = Button(canvas, text="", command=ignorethis, width=15)
btn15.grid(column=6, row=1)
btn16 = Button(canvas, text="", command=ignorethis, width=15)
btn16.grid(column=7, row=1)
canvas.pack()
newcanvas.pack()
window.mainloop()
