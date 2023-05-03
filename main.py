# Goal of this file is to be where the input command is and will lead to the other files
from galaxymaker import galaxymakerr
import planetmaker
import os
import player
from tkinter import Tk  # in Python 2, use "Tkinter" instead




# print(galaxymakerr(minimum_systems=64, include_moons=True))


def clearscreen():
    # input("Any button to continue")
    try:
        os.system('cls')
    except:
        os.system('clear')


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
            /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5)
    
    
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
        current_system = playership.system
        links = "links"
        name = "Name"
        print(f"System Name: {galaxy[current_system][name]}")
        print(f"Nearby Systems: {galaxy[current_system][links]}")
        current_planet = 1
        if len(galaxy[current_system]["planets"]) == 0:
            print("No Planets in this system")
        for x in galaxy[current_system]["planets"]:
            print(x["planet" + str(current_planet)]["Name"] + "; " + x["planet" + str(current_planet)]["Type"])
            current_planet += 1


            # type = galaxy[current_system][x]["Type"]
            # print(f"Name: {galaxy[current_system][x][name]}; {type}")
    elif input1.lower == "help":
        print("Guide for the `System` command")
        print("Format: /system info")
        print("This will provide some information about the current system")

def gotocommand(input1="help", input2="help"):

    if input1.lower() == "system":

        current_system = playership.system
        for x in galaxy[current_system]["links"]:
            # print(f"x={x}, input2={input2}")
            if x == int(input2):

                playership.system = "system" + str(x)
                name = "Name"
                print(f"Player is now in System {x}: {galaxy[playership.system][name]}")
                return

        print("System not connected!")
    elif input1.lower == "help":
        print("Guide for the `Goto` command")
        print("Format: /goto system [system number]")
        print("You can only go to the Nearby Systems")






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
while True:
    command = input("Input Command:")
    clearscreen()
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
            clearscreen()
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



