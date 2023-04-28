from random import randint
import random
import moonmaker
from math import *

class makeplanet():

    def __init__(self):
        pass

    def planetfactory(self, include_moons=False, forceplanettype="random"):
        haslife = False
        lifesubtypes = "None"
        subtype = "Gaseous"
        settled = False
        moons = []
        mass = 400
        chances = {
            "Dwarf Planet": 30,
            "Rocky Planet": 50,
            "Super Earth": 60,
            "Ice Giant": 80,
            "Gas Giant": 100
        }
        gravityrange = {
            "Dwarf Planet": [0.01, 2],
            "Rocky Planet": [3, 12],
            "Super Earth": [9, 16],
            "Ice Giant": [7, 18],
            "Gas Giant": [10, 40]

        }
        gravitydrop = {
            "Dwarf Planet": 0.02,
            "Rocky Planet": 1,
            "Super Earth": 2,
            "Ice Giant": 3,
            "Gas Giant": 4

        }

        radii = {
            "Dwarf Planet": [100, 1699],
            "Rocky Planet": [1700, 6699],
            "Super Earth": [6700, 14099],
            "Ice Giant": [14100, 29999],
            "Gas Giant": [30000, 90000]



        }

        masses = {
            "Dwarf Planet": [0.005, 0.01],
            "Rocky Planet": [0.01, 2],
            "Super Earth": [2, 10],
            "Ice Giant": [10, 20],
            "Gas Giant": [20, 400]

        }
        if forceplanettype == "random":
            given = randint(0, 100)
            if given <= chances["Dwarf Planet"]:
                typeer = "Dwarf Planet"

                mass = float(
                    randint(int(masses["Dwarf Planet"][0] * 10000), int(masses["Dwarf Planet"][1] * 10000))) / 10000
                gravity = round(mass * 9.8 + gravitydrop["Dwarf Planet"] * (randint(-100, 100) / 100), 3)

            elif chances["Dwarf Planet"] < given <= chances["Rocky Planet"]:
                typeer = "Rocky Planet"
                mass = float(
                    randint(int(masses["Rocky Planet"][0] * 10000), int(masses["Rocky Planet"][1] * 10000))) / 10000
                gravity = round(mass * 9.8 + gravitydrop["Rocky Planet"] * (randint(-100, 100) / 100), 3)

            elif chances["Rocky Planet"] < given <= chances["Super Earth"]:
                typeer = "Super Earth"
                mass = float(
                    randint(int(masses["Super Earth"][0] * 10000), int(masses["Super Earth"][1] * 10000))) / 10000
                gravity = round(mass * 9.8 + gravitydrop["Super Earth"] * (randint(-100, 100) / 100), 3)


            elif chances["Super Earth"] < given <= chances["Ice Giant"]:
                typeer = "Ice Giant"
                mass = float(
                    randint(int(masses["Ice Giant"][0] * 10000), int(masses["Ice Giant"][1] * 10000))) / 10000




            else:
                typeer = "Gas Giant"
                gravity = randint(int(gravityrange["Gas Giant"][0] * 100), int(gravityrange["Gas Giant"][1] * 100))
                gravity = float(gravity / 100)
                mass = float(
                    randint(int(masses["Gas Giant"][0] * 10000), int(masses["Gas Giant"][1] * 10000))) / 10000



            radius = randint(radii[typeer][0], radii[typeer][1])
            gravity = round((mass / (radius ** 2)) * 9.8, 3)
            print(f"gravity should be {gravity}. Radius={radius}, Mass={mass}")


        else:
            typeer = forceplanettype
            mass = float(
                randint(int(masses[forceplanettype][0] * 10000), int(masses[forceplanettype][1] * 10000))) / 10000
            if mass > 120:
                x = (float(randint(-200, 200)) / 10000)
                print(f"xvalue = {x}")
                radius = cbrt(mass)
            else:
                x = (float(randint(100, 200)) / 10000)
                print(f"xvalue = {x}")
                radius = cbrt(mass)
            earthradius = 6371
            # radius = randint(radii[typeer][0], radii[typeer][1])
            gravity = (mass / (radius)**2)
            print(f"gravity should be {gravity}. Radius={radius}, Mass={mass}")

            # if typeer == "Ice Giant":
            #     gravity = randint(int(gravityrange["Ice Giant"][0] * 100), int(gravityrange["Ice Giant"][1] * 100))\
            #               / 100
            # elif typeer == "Gas Giant":
            #     gravity = randint(int(gravityrange["Gas Giant"][0] * 100), int(gravityrange["Gas Giant"][1] * 100))\
            #               / 100
            #     print("Here")
            # else:
            #     gravity = round(mass * 9.8 + gravitydrop[forceplanettype] * (randint(-100, 100) / 100), 3)




        if randint(0, 1) == 1:
            hasring = True
        else:
            hasring = False

        if typeer == "Ice Giant" or typeer == "Gas Giant":
            subtype = "Gaseous"
            # print("Checkherer")

        elif typeer == "Dwarf Planet":
            subtype = "Barrenworld"
            hasring = False

        elif typeer == "Super Earth":
            # print("Check here")
            value = randint(0, 3)
            if value == 0:
                subtype = "Waterworld"
            elif value == 1:
                subtype = "Lavaworld"
            else:
                subtype = "Barrenworld"

        elif typeer == "Rocky Planet":
            # print("Check here")
            value = randint(0, 3)
            if value == 0:
                subtype = "Waterworld"
            elif value == 1:
                subtype = "Lavaworld"
            elif value == 2:
                subtype = "Barrenworld"
            else:
                subtype = "Habitableworld"
                if randint(0, 1) == 1:
                    haslife = True
                    if randint(0, 1) == 1:
                        lifesubtypes = "Intelligent"
                        settled = True
                    else:
                        lifesubtypes = "Unintelligent"

        if include_moons == True:
            moons = self.moonfactory(mass, typeer)

        return {
            "Type": typeer,
            "Gravity": gravity,
            "Mass": mass,
            "Ringed": hasring,
            "Subtype": subtype,
            "Has Life": haslife,
            "Life Subtypes": lifesubtypes,
            "Settled": settled,
            "Moons": moons
        }

    def moonfactory(self, totalmass, planet_type):

        moons = []
        remainingmass = totalmass * 0.15
        moonsizes = ["moon1", "moon2", "moon3", "moon4", "moon5"]
        mooninfo = {
            "moon1": {
                          "Mass": [0.00001, 0.0001],
                          "Gravity": [0.001, 0.01],
                          "Shape": ["Irregular", "Spherical"]},
            "moon2": {
                          "Mass": [0.0001, 0.001],
                          "Gravity": [0.01, 0.1],
                          "Shape": ["Irregular", "Spherical"]},
            "moon3": {
                          "Mass": [0.001, 0.01],
                          "Gravity": [0.1, 0.5],
                          "Shape": ["Irregular", "Spherical"]},
            "moon4": {
                          "Mass": [0.01, 0.1],
                          "Gravity": [0.5, 1],
                          "Shape": ["Spherical"]},
            "moon5": {
                          "Mass": [0.1, 1],
                          "Gravity": [1, 6],
                          "Shape": ["Spherical"]}}
        slots = 0
        if planet_type == "Dwarf Planet":
            slots = 5
        elif planet_type == "Rocky Planet":
            slots = 3
        elif planet_type == "Super Earth":
            slots = 5
        elif planet_type == "Ice Giant":
            slots = 10
        elif planet_type == "Gas Giant":
            slots = 15

        slots = random.randint(0, slots)
        # print(slots)
        if slots > 0:
            while slots > 0:
                if remainingmass * 1000 > totalmass:
                    currentmoon = {}
                    moonitem = random.randint(0, 4)
                    moonchoice = mooninfo[moonsizes[moonitem]]
                    moonmass = float(random.randint(moonchoice["Mass"][0] * 100000, moonchoice["Mass"][1] * 100000)) \
                               / 100000
                    moongrav = float(random.randint(moonchoice["Gravity"][0] * 100000,
                                                    moonchoice["Gravity"][1] * 100000)) / 100000
                    moonshape = random.choice(moonchoice["Shape"])
                    # mass = mooninfo[moonchoice["Mass"]]
                    # print(remainingmass)
                    remainingmass -= moonmass
                    if remainingmass > 0:
                        currentmoon = {
                            "Type": moonsizes[moonitem],
                            "Mass": moonmass,
                            "Gravity": moongrav,
                            "Shape": moonshape
                        }
                        slots -= 1
                        moons.append(currentmoon)
                    else:
                        remainingmass += moonmass
                        slots -= 0.1
                else:
                    slots -= 1

        return moons

    def starfactory(self):
        pass
#     Type represents what class of planet it is
# Gravity is the strength of gravity at sea level
# Mass is the number of Earth Masses
# Ringed is whether or not the planet has rings
# subtype chooses from a basic list of features (Gasseous, Waterworld, Lavaworld, Barrenworld, Habitableworld)
# Has Life will apply if the world has life
# Life subtype will specift if there is intelligent life. This is only active on worlds with Has Life
# Settled will be given to all worlds with intelligent life
