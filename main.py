# Goal of this file is to be where the input command is and will lead to the other files
from galaxymaker import galaxymakerr  #This is to allow for galaxy generation
import planetmaker   #This is for planet generation
import os   #This is to help with clearing the screen
import player   #This created the player character
from formulas import planetnumber, planetletter   #This is used to convert b to 2 and 2 to b
import random     #Math
from tkinter import *    #For the GUI
from tkinter.ttk import *    #For the GUI


def clearscreen(Windows):
    #This clears the screen. It works with def changeos to work on both linux and windows without crashing
    if Windows.lower() == "yes":
        myvalue = os.system('cls')
    else:
        myvalue = os.system('clear')
    if myvalue != 0 and Windows.lower() == "yes":
        changeos("Windows")
    elif myvalue != 0 and Windows.lower() == "no":
        changeos("Linux")


def changeos(fromwhere):
    #This will change the operating system from windows to linux or visa versa to clear screen correctly
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
    # This will create a planet for fun. Does not affect the game, but may be useful for planet stats
    # When making one from scratch
    # Will be used at start to make the galaxy though
    x = planetmaker.makeplanet()
    try:
        if input1 == "planet":
            # Will generate a planet with or without moons as desired. Also can force the planet type
            answer = x.planetfactory(include_moons=(input3), forceplanettype=input2)
            for x in answer:
                print(f"{x}: {answer[x]}")

            return ()
        elif input1 == "moon":
            #Will return a moon sample that can be used for other purposes
            return (x.moonfactory(moontype=input2)[0])
        elif input1 == "galaxy":
            # Will generate a new galaxy and save it to the game file
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
    global Windows
    # clearscreen(Windows)
    if input1 == "info":
        print(f"Crew={playership.ship.crew}")
        print(f"Ship Type={playership.ship.size} {playership.ship.shiptype}")
        print(f"Health={playership.ship.health}")

        print(f"Inventory={playership.ship.inventory}")
        print(f"Crew={playership.ship.crew}")
        # clearscreen(Windows)


def systemcommand(input1="help", input2="help", input3="help", input4="help"):
    global Windows
    # clearscreen(Windows)
    current_system = playership.system
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
canvas = Canvas(width=1000, height=1000, highlightthickness=0)
# Upper Buttons
btn1 = Button(window, text="Travel", command=lambda: totravel(), width=15)
btn1.grid(column=0, row=0)
btn2 = Button(text="System", command=systembutton, width=15)
btn2.grid(column=1, row=0)
btn3 = Button(text="Planet", command=planetbutton, width=15)
btn3.grid(column=2, row=0)
btn4 = Button(text="Ship", command=ignorethis, width=15)
btn4.grid(column=3, row=0)
btn5 = Button(text="Crew", command=ignorethis, width=15)
btn5.grid(column=4, row=0)
btn6 = Button(text="Starbase", command=ignorethis, width=15)
btn6.grid(column=5, row=0)
btn7 = Button(text="Settings", command=ignorethis, width=15)
btn7.grid(column=6, row=0)
btn8 = Button(text="Console", command=console, width=15)
btn8.grid(column=7, row=0)
# Lower Buttons
btn9 = Button(text="Spare1", command=lambda: ignorethis(), width=15)
btn9.grid(column=0, row=1)
btn10 = Button(text="Spare2", command=ignorethis, width=15)
btn10.grid(column=1, row=1)
btn11 = Button(text="Spare3", command=ignorethis, width=15)
btn11.grid(column=2, row=1)
btn12 = Button(text="Spare4", command=ignorethis, width=15)
btn12.grid(column=3, row=1)
btn13 = Button(text="Spare5", command=ignorethis, width=15)
btn13.grid(column=4, row=1)
btn14 = Button(text="Spare6", command=ignorethis, width=15)
btn14.grid(column=5, row=1)
btn15 = Button(text="Spare7", command=ignorethis, width=15)
btn15.grid(column=6, row=1)
btn16 = Button(text="Spare8", command=ignorethis, width=15)
btn16.grid(column=7, row=1)
window.mainloop()



