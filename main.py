# Goal of this file is to be where the input command is and will lead to the other files
from galaxymaker import galaxymakerr
import planetmaker
import os
import player
from formulas import planetnumber
from tkinter import Tk  # in Python 2, use "Tkinter" instead


# print(galaxymakerr(minimum_systems=64, include_moons=True))


def clearscreen(Windows):
    # input("Any button to continue")
    if Windows.lower() == "yes":
        myvalue = os.system('cls')
    else:
        myvalue = os.system('clear')
    if myvalue != 0 and Windows.lower() == "yes":
        changeos("Windows")
    elif myvalue != 0 and Windows.lower() == "no":
        changeos("Linux")


def changeos(fromwhere):
    global Windows
    if fromwhere == "Windows":
        Windows = "no"
    if fromwhere == "Linux":
        Windows = "yes"
    clearscreen(Windows)
def helpcommand():
    print('''
    The Following are usable commands
    Begin commands with a /

    /help
    -provides information on commands

    /make (planet/galaxy/moon/help) (input1) (input2) (input3)
    -allows you to make a galaxy, planet, or moon
    /make galaxy (minimum systems) (include moons: True/False)
    /make planet (forceplanettype: random) (include moons: True/False)
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


def makecommand(input1="help", input2="help", input3="help", input4="help"):
    x = planetmaker.makeplanet()
    try:
        if input1 == "planet":
            answer = x.planetfactory(include_moons=(input3), forceplanettype=input2)
            for x in answer:
                print(f"{x}: {answer[x]}")

            return ()
        elif input1 == "moon":

            return (x.moonfactory(moontype=input2)[0])
        elif input1 == "galaxy":
            playership.system = "system1"
            galaxydict = galaxymakerr(include_moons=input3, minimum_systems=float(input2))
            import json
            global galaxy
            # Serializing json

            # print(json_object)

            json_object = json.dumps(galaxydict, default=lambda o: o.__dict__, sort_keys=True, indent=2)

            try:
                with open('systems.json', 'w') as fp:
                    fp.write(json_object)
            except:
                print("BROKE HERE")
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
    # clearscreen()
    if input1 == "info":
        print(f"Crew={playership.ship.crew}")
        print(f"Ship Type={playership.ship.size} {playership.ship.shiptype}")
        print(f"Health={playership.ship.health}")

        print(f"Inventory={playership.ship.inventory}")
        print(f"Crew={playership.ship.crew}")
        clearscreen()


def systemcommand(input1="help", input2="help", input3="help", input4="help"):
    # clearscreen()
    if input1 == "info":
        links = "links"
        name = "Name"
        print(f"System Name: {galaxy[current_system][name]}")
        print(f"Nearby Systems: {galaxy[current_system][links]}")
        current_planet = 1
        current_spot = 1

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


    elif input1.lower() == "planet":
        playership.planet = "planet" + input2
        current_system = playership.system
        current_planet = playership.planet
        current_spot = planetnumber(current_planet[-1])
        try:
            if len(galaxy[current_system]["planets"]) < current_spot - 1:
                playership.planet = "None"
                print("Planet does not exist")
            else:
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
playership = player.Player()
properties = {
    "CurrentSystem": playership.system,
    "Player_Properties": {
        "size": playership.ship.size,
        "Ship Type": playership.ship.shiptype,
        "Crewcapacity": playership.ship.crewcapacity,
        "Ammo": playership.ship.ammo,
        "inventory": playership.ship.inventory,
        "fueluse": playership.ship.fueluse,
        "health": playership.ship.health,
        "crew": playership.ship.crew
    },
}
galaxy = {}
makecommand("galaxy", "100", "False")


# \/  Whether this is a Windows machine or not doesnt matter, it will adjust istelf after the first command
Windows = "yes"
#


# In order to use the Planet Path, you must first share two things. current_system is provided at the start of the
# for loop. The second is current_spot. current spot is the position of the planet. The first planet has a
# current_spot of 1. You can get the spot of the planet by doing the planetnumber() function
# example use of planetpath: eval(planetpath)["Name"]
planetpath = 'galaxy[current_system]["planets"][current_spot - 1]["planet" + str(str(current_spot))]'
while True:

    # No Touch \/
    current_system = playership.system

    # No Touch /\

    command = input("Input Command:")
    clearscreen(Windows)
    try:
        command[0].lower()
        if command[0] == "/":
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
                command.append("vacantslot")
                command.append("vacantslot")
                command.append("vacantslot")
            elif command[0] == "/changeos":
                changeos()
    except(IndexError):
        pass
