import math
from random import randint
import random
from math import *

GConstant = 6.6743 * 10 ** (-11)


class makeplanet():

    def __init__(self):
        pass

    def planetfactory(self, include_moons=False, forceplanettype="random", forcelife=False):
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

        # This is in Meters
        radii = {
            "Dwarf Planet": [100000, 1699000],
            "Rocky Planet": [1700000, 7599000],
            "Super Earth": [7600000, 14099000],
            "Ice Giant": [14100000, 29999000],
            "Gas Giant": [30000000, 90000000]

        }

        if forceplanettype == "random":
            given = randint(0, 100)
            if given <= chances["Dwarf Planet"]:
                typeer = "Dwarf Planet"
                ptype = "Rocky Planet"
                points = 1

            elif chances["Dwarf Planet"] < given <= chances["Rocky Planet"]:
                typeer = "Rocky Planet"
                ptype = "Rocky Planet"
                points = 5

            elif chances["Rocky Planet"] < given <= chances["Super Earth"]:
                typeer = "Super Earth"
                ptype = "Rocky Planet"
                points = 7


            elif chances["Super Earth"] < given <= chances["Ice Giant"]:
                typeer = "Ice Giant"
                ptype = "Gas Planet"
                points = 15




            else:
                typeer = "Gas Giant"
                ptype = "Gas Planet"
                points = 20






        else:
            typeer = forceplanettype
            if typeer == "Ice Giant" or typeer == "Gas Giant":
                ptype = "Gas Planet"
            else:
                ptype = "Rocky Planet"

        # Radius unit is in meters
        radius = randint(radii[typeer][0], radii[typeer][1])

        if forcelife == True and forceplanettype == "Rocky Planet":
            radius = 6371000
            typeer = forceplanettype
            settled = True

        # volume is in meters^3
        volume = (4 / 3) * pi * (radius ** 3)

        core = self.coremaker(ptype)


        # density is g/cm^3
        density = core["density"]

        # ndensity is kg/m^3
        ndensity = density * 1000

        newmass = (ndensity) * volume
        gravity = GConstant * (newmass / (radius ** 2))
        ignorethis = "density"
        stats = {
            "gravity": gravity,
            "mass": newmass,
            "volume": volume,
            "density": core["density"],
            "radius": radius,
            "corestats": core

        }
        #       f"Volume={volume}")

        if randint(0, 1) == 1:
            hasring = True
        else:
            hasring = False

        if typeer == "Ice Giant" or typeer == "Gas Giant":
            subtype = "Gaseous"

        elif typeer == "Dwarf Planet":
            subtype = "Barrenworld"
            hasring = False

        elif typeer == "Super Earth":
            value = randint(0, 3)
            if value == 0:
                subtype = "Waterworld"
            elif value == 1:
                subtype = "Lavaworld"
            else:
                subtype = "Barrenworld"

        elif typeer == "Rocky Planet":
            value = randint(0, 3)
            if value == 0:
                subtype = "Waterworld"
            elif value == 1:
                subtype = "Lavaworld"
            elif value == 2:
                subtype = "Barrenworld"
            if value == 3 or forcelife == True:
                subtype = "Habitableworld"
                if randint(0, 1) == 1:
                    haslife = True
                    if randint(0, 1) == 1:
                        lifesubtypes = "Intelligent"
                        settled = True
                    else:
                        lifesubtypes = "Unintelligent"
            if forcelife:
                settled = True
                lifesubtypes = "Intelligent"

        if include_moons == True:
            moons = self.moonfactory(moontype="random", totalmass=newmass, planet_type=typeer)

        return {
            "Type": typeer,
            "Gravity": gravity,
            "Mass": newmass,
            "Ringed": hasring,
            "Subtype": subtype,
            "Has Life": haslife,
            "Life Subtypes": lifesubtypes,
            "Settled": settled,
            # "stats": stats,
            "core": core,
            "Moons": moons,

        }

    def moonfactory(self, totalmass=1000000000000000000000000000000, planet_type="Gas Giant", moontype="random",
                    moonversion=1):
        # moonversion 1 will use the while loop to repeat the selection process where the number of moons is decided here
        # moonversion 2 will only return a single moon and is added later on using a different process

        moons = []
        remainingmass = totalmass * 0.15
        moonsizes = ["moon1", "moon2", "moon3", "moon4", "moon5"]
        # Radius is in meters
        mooninfo = {
            # Mass is in Teragrams
            "moon1": {
                "Radius": [1000, 10000],
                "Shape": ["Irregular", "Spherical"],
                "Points": 1},
            "moon2": {
                "Radius": [10000, 100000],
                "Shape": ["Irregular", "Spherical"],
                "Points": 2},
            "moon3": {
                "Radius": [100000, 1000000],
                "Shape": ["Irregular", "Spherical"],
                "Points": 4},
            "moon4": {
                "Radius": [1000000, 2000000],
                "Shape": ["Spherical"],
                "Points": 7},
            "moon5": {
                "Radius": [2000000, 5000000],
                "Shape": ["Spherical"],
                "Points": 10}}

        slots = 0
        if planet_type == "Dwarf Planet":
            slots = 5
            moonitem = random.randint(0, 1)
        elif planet_type == "Rocky Planet":
            slots = 3
            moonitem = random.randint(0, 3)
        elif planet_type == "Super Earth":
            slots = 5
            moonitem = random.randint(0, 3)
        elif planet_type == "Ice Giant":
            slots = 10
            moonitem = random.randint(0, 4)
        else:
            slots = 15
            moonitem = random.randint(0, 4)

        slots = random.randint(0, slots)
        if slots > 0:
            while slots > 0:
                if remainingmass * 1000 > totalmass:
                    currentmoon = {}
                    if moontype == "random":
                        moontype = moonsizes[moonitem]
                        moonradius = randint(mooninfo[moontype]["Radius"][0], mooninfo[moontype]["Radius"][1])

                    elif moontype != "random":
                        moonitem = 0
                        moonsizes[0] = moontype
                        moonradius = randint(mooninfo[moontype]["Radius"][0], mooninfo[moontype]["Radius"][1])

                    moonchoice = mooninfo[moontype]
                    # moonmass /= 1000000000
                    if moontype == "moon1":
                        core1 = self.coremaker(planettype="Moon")
                    elif moontype == "moon2":
                        core1 = self.coremaker(planettype="Moon")
                    elif moontype == "moon3":
                        core1 = self.coremaker(planettype="Rocky Planet")
                    elif moontype == "moon4":
                        core1 = self.coremaker(planettype="Rocky Planet")
                    else:
                        core1 = self.coremaker(planettype="Rocky Planet")

                    # density is g / cm ^ 3
                    mdensity = core1["density"]

                    # ndensity is kg/m^3
                    mndensity = mdensity * 1000

                    mvolume = (4 / 3) * pi * (moonradius ** 3)

                    moonmass = (mndensity) * mvolume

                    # radius is in meters

                    moongrav = GConstant * (moonmass / (moonradius ** 2))
                    moongrav = round(moongrav, 8)
                    moonshape = random.choice(moonchoice["Shape"])

                    remainingmass -= moonmass

                    if remainingmass > 0:
                        currentmoon = {
                            "Type": moonsizes[moonitem],
                            "Mass": moonmass,
                            "Gravity": moongrav,
                            "Radius": moonradius,
                            "Volume": mvolume,
                            "Shape": moonshape,
                            "core": core1
                        }
                        slots -= 1
                        moons.append(currentmoon)
                    else:
                        remainingmass += moonmass
                        slots -= 0.1
                else:
                    slots -= 1
                if planet_type == "Dwarf Planet":
                    moonitem = random.randint(0, 1)
                elif planet_type == "Rocky Planet":
                    moonitem = random.randint(0, 3)
                elif planet_type == "Super Earth":
                    moonitem = random.randint(0, 3)
                elif planet_type == "Ice Giant":
                    moonitem = random.randint(0, 4)
                else:
                    moonitem = random.randint(0, 4)
                moontype = "random"
                if moonversion == 2:
                    break
        if len(moons) == 0:
            moons = self.moonfactory(totalmass=totalmass, planet_type=planet_type, moontype=moontype,
                                     moonversion=moonversion)

        return moons

    def starfactory(self, wanted_star="random"):
        startypes = {
            "O": {
                "Values": (200, 250),
                "Abundance": (1, 1),
                "Radius": 10,
                "Mass": 50,
                "Color": "Blue",
                "Temperature": (30000, 50000),
            },
            "B": {
                "Values": (175, 199),
                "Abundance": (2, 4),
                "Radius": 5,
                "Mass": 10,
                "Color": "White-Blue",
                "Temperature": (10000, 30000),
            },
            "A": {
                "Values": (150, 174),
                "Abundance": (5, 10),
                "Radius": 1.7,
                "Mass": 2,
                "Color": "White",
                "Temperature": (7500, 10000),
            },
            "F": {
                "Values": (100, 149),
                "Abundance": (11, 20),
                "Radius": 1.3,
                "Mass": 1.5,
                "Color": "White-Yellow",
                "Temperature": (6000, 7500),
            },
            "G": {
                "Values": (70, 99),
                "Abundance": (21, 40),
                "Radius": 1,
                "Mass": 1,
                "Color": "Yellow",
                "Temperature": (5200, 6000),
            },
            "K": {
                "Values": (50, 69),
                "Abundance": (41, 60),
                "Radius": 0.7,
                "Mass": 0.7,
                "Color": "Orange",
                "Temperature": (3700, 5200),
            },
            "M": {
                "Values": (30, 49),
                "Abundance": (61, 100),
                "Radius": 0.2,
                "Mass": 0.2,
                "Color": "Red",
                "Temperature": (3000, 3700),
            },

        }
        listtypes = ["O", "B", "A", "F", "G", "K", "M"]
        if wanted_star == "random":
            value = randint(1, 100)
            for starclass in startypes:
                if startypes[starclass]["Abundance"][0] <= value <= startypes[starclass]["Abundance"][1]:
                    wanted_star = starclass

        self.startype = {
            "Value": random.randint(startypes[wanted_star]["Values"][0], (startypes[wanted_star]["Values"][1])),
            "Class": wanted_star,
            "Color": startypes[wanted_star]["Color"],
            "Mass": random.randint(
                int(round(startypes[wanted_star]["Mass"] * 100 - startypes[wanted_star]["Mass"] * 100 / 8)),
                int(round(startypes[wanted_star]["Mass"] * 100 + startypes[wanted_star]["Mass"] * 100 / 8))) / 100,
            "Radius": random.randint(
                int(round(startypes[wanted_star]["Radius"] * 100 - startypes[wanted_star]["Radius"] * 100 / 8)),
                int(round(startypes[wanted_star]["Radius"] * 100 + startypes[wanted_star]["Radius"] * 100 / 8))) / 100,
            "Temperature": random.randint(startypes[wanted_star]["Temperature"][0],
                                          (startypes[wanted_star]["Temperature"][1])),

        }
        return self.startype

    # Source for Star Stuff is http://www.atlasoftheuniverse.com/startype.html
    def coremaker(self, planettype):
        '''
        Accepted Value for planettype are "Gas Planet" and "Dwarf Planet".

        Use "Dwarf Planet" for solid bodies, and "Gas Planet" for gasseous


        :param planettype:
        :return:
        '''

        def getcoreterra(whatarewetesting):
            coresplit = randint(1, len(whatarewetesting) - 1)
            coresplitss = []
            corev = []
            minsplit = 0
            for x in range(0, coresplit):
                newsplit = randint(minsplit, 100)
                if newsplit != minsplit:
                    coresplitss.append(newsplit)
                    minsplit = newsplit

            total = 0
            for x in range(len(coresplitss)):

                if x == 0:
                    corev.append(coresplitss[x])
                    total += coresplitss[x]
                else:
                    corev.append(coresplitss[x] - coresplitss[x - 1])
                    total += coresplitss[x] - coresplitss[x - 1]

            corev.append(100 - total)
            ccorev = corev

            corecontents = []
            # corecontents.append(choice(whatarewetesting))
            # place = randint(0, len(whatarewetesting) - 1)
            # corecontents.append(whatarewetesting[place])
            # del(whatarewetesting[place])
            #
            while len(corecontents) < len(corev):
                place = randint(0, len(whatarewetesting) - 1)
                corecontents.append(whatarewetesting[place])
                del (whatarewetesting[place])
            count = 0
            newcore = {}
            for value in corecontents:
                if corev[count] != 0:
                    newcore[corecontents[count]] = corev[count]
                    count += 1

            return newcore

        # Function Ends

        elements = {
            "Ice": 0.9,
            "Iron": 7.8,
            "Nickel": 8.9,
            "Rock": 2.6,
            "Sulfur": 2.1,
            "Silicon": 2.3,
            "Oxygen": 1.2,
            "Magnesium": 1.7,
            "Aluminum": 2.7,
            "Potassium": 0.8,
            "Hydrogen": 0.007,
            "Helium": 0.002
        }
        core = ["Iron", "Nickel"]
        mantle = ["Sulfur", "Oxygen", "Silicon", "Magnesium"]
        crust = ["Ice", "Rock", "Sulfur", "Silicon", "Oxygen", "Magnesium", "Aluminum", "Potassium", "Iron", "Nickel"]
        atmos = ["Hydrogen", "Helium"]

        if planettype == "Moon":
            density = {}
            corevalue = randint(10, 99)
            crustvalue = 100 - corevalue
            mycore = getcoreterra(core)
            mycrust = getcoreterra(crust)
            totalcore = {
                "core": mycore,
                "core%": corevalue,
                "crust": mycrust,
                "crust%": crustvalue

            }
            coredenity = 0
            for x in mycore:
                weight = mycore[x] / 100
                dens = elements[x]
                coredenity += (dens * weight)
            density["core"] = round(coredenity, 3)

            crudenity = 0
            for x in mycrust:
                weight = mycrust[x] / 100
                dens = elements[x]
                crudenity += (dens * weight)
            density["crust"] = round(crudenity, 3)
            finaldensity = 0
            finaldensity += (corevalue / 100) * density["core"]
            finaldensity += (crustvalue / 100) * density["crust"]
            totalcore["density"] = round(finaldensity, 3)

        if planettype == "Rocky Planet":
            density = {}
            corevalue = randint(10, 30)
            crustvalue = randint(0, 20)
            mantlevalue = 100 - (corevalue + crustvalue)
            mycore = getcoreterra(core)
            mymantle = getcoreterra(mantle)
            mycrust = getcoreterra(crust)
            totalcore = {
                "core": mycore,
                "core%": corevalue,
                "mantle": mymantle,
                "mantle%": mantlevalue,
                "crust": mycrust,
                "crust%": crustvalue

            }
            coredenity = 0
            for x in mycore:
                weight = mycore[x] / 100
                dens = elements[x]
                coredenity += (dens * weight)
            density["core"] = round(coredenity, 3)

            mandenity = 0
            for x in mymantle:
                weight = mymantle[x] / 100
                dens = elements[x]
                mandenity += (dens * weight)
            density["mantle"] = round(mandenity, 3)

            crudenity = 0
            for x in mycrust:
                weight = mycrust[x] / 100
                dens = elements[x]
                crudenity += (dens * weight)
            density["crust"] = round(crudenity, 3)
            finaldensity = 0
            finaldensity += (corevalue / 100) * density["core"]
            finaldensity += (mantlevalue / 100) * density["mantle"]
            finaldensity += (crustvalue / 100) * density["crust"]
            totalcore["density"] = round(finaldensity, 3)

        if planettype == "Gas Planet":

            density = {}
            corevalue = randint(10, 30)
            atmovalue = 100 - corevalue
            mycore = getcoreterra(core)
            myatmo = getcoreterra(atmos)
            totalcore = {
                "core": mycore,
                "core%": corevalue,
                "atmo": myatmo,
                "atmo%": atmovalue
            }
            coredenity = 0
            for x in mycore:
                weight = mycore[x] / 100
                dens = elements[x]
                coredenity += (dens * weight)
            density["core"] = round(coredenity, 3)
            atmodenity = 0
            for x in myatmo:
                weight = myatmo[x] / 100
                dens = elements[x]
                atmodenity += (dens * weight)
            density["atmosphere"] = round(atmodenity, 3)
            finaldensity = 0
            finaldensity += (corevalue / 100) * density["core"]
            finaldensity += (atmovalue / 100) * density["atmosphere"]

            totalcore["density"] = round(finaldensity, 3)
        totalcore["Core Density"] = density["core"]

        return totalcore

#     Type represents what class of planet it is
# Gravity is the strength of gravity at sea level
# Mass is the number of Earth Masses
# Ringed is whether or not the planet has rings
# subtype chooses from a basic list of features (Gasseous, Waterworld, Lavaworld, Barrenworld, Habitableworld)
# Has Life will apply if the world has life
# Life subtype will specift if there is intelligent life. This is only active on worlds with Has Life
# Settled will be given to all worlds with intelligent life
