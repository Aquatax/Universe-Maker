# Goal of this file is to be where the input command is and will lead to the other files
from galaxymaker import galaxymakerr
import planetmaker
import os
import json

# print(galaxymakerr(minimum_systems=64, include_moons=True))
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


            galaxydict = galaxymakerr(include_moons=(input3), minimum_systems=float(input2))
            # Serializing json
            json_object = json.dumps(galaxydict, indent=4)
            print(json_object)
            return


        else:
            print('''
            /make (planet/galaxy/moon/help) (input1) (input2) (input3)
            -allows you to make a galaxy, planet, or moon
            /make galaxy (minimum systems) (include moons: True/False)
            /make planet (forceplanettype: random) (include moons: True/False)
            /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5)
            
            ''')
    except(KeyError):
        print('''
                    /make (planet/galaxy/moon/help) (input1) (input2) (input3)
            -allows you to make a galaxy, planet, or moon
            /make galaxy (minimum systems) (include moons: True/False)
            /make planet (forceplanettype: random) (include moons: True/False)
            /make moon (forcemoontype: moon1, moon2, moon3, moon4, moon5)

                    ''')
        return






print("Welcome to Galaxy Creator")
print("Use / to start a command. Try /help")
while True:
    command = input("Input Command:")
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
            os.system('cls')
        elif command[0] == "/make":

            command.append("vacantslot")
            command.append("vacantslot")
            command.append("vacantslot")
            answer = makecommand(command[1], command[2], command[3])
            print(answer)

