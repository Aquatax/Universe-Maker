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

            elif chances["Dwarf Planet"] < given <= chances["Rocky Planet"]:
                typeer = "Rocky Planet"
                ptype = "Rocky Planet"

            elif chances["Rocky Planet"] < given <= chances["Super Earth"]:
                typeer = "Super Earth"
                ptype = "Rocky Planet"


            elif chances["Super Earth"] < given <= chances["Ice Giant"]:
                typeer = "Ice Giant"
                ptype = "Gas Planet"




            else:
                typeer = "Gas Giant"
                ptype = "Gas Planet"






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
        # print(f"Ptype = {ptype}")
        core = self.coremaker(ptype)
        # print(f"Ptype = {ptype}")

        # density is g/cm^3
        density = core["density"]

        # ndensity is kg/m^3
        ndensity = density * 1000

        newmass = (ndensity) * volume
        # Mass is in
        # print(newmass)
        gravity = GConstant * (newmass / (radius ** 2))
        ignorethis = "density"
        # print(f"Core Info is {core}")
        stats = {
            "gravity": gravity,
            "mass": newmass,
            "volume": volume,
            "density": core["density"],
            "radius": radius,
            "corestats": core

        }
        # print(f"gravity should be {gravity}. Radius={radius}, Mass={newmass}, Density={ndensity}, "
        #       f"Volume={volume}")

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
            # print("HI")
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

    def moonfactory(self, totalmass=1000000000000000000000000000000, planet_type="Gas Giant", moontype="random"):

        moons = []
        remainingmass = totalmass * 0.15
        moonsizes = ["moon1", "moon2", "moon3", "moon4", "moon5"]
        # Radius is in meters
        mooninfo = {
            # Mass is in Teragrams
            "moon1": {
                "Radius": [1000, 10000],
                "Shape": ["Irregular", "Spherical"]},
            "moon2": {
                "Radius": [10000, 100000],
                "Shape": ["Irregular", "Spherical"]},
            "moon3": {
                "Radius": [100000, 1000000],
                "Shape": ["Irregular", "Spherical"]},
            "moon4": {
                "Radius": [1000000, 2000000],
                "Shape": ["Spherical"]},
            "moon5": {
                "Radius": [2000000, 5000000],
                "Shape": ["Spherical"]}}

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
        # print(slots)
        if slots > 0:
            while slots > 0:
                if remainingmass * 1000 > totalmass:
                    currentmoon = {}
                    if moontype == "random":
                        moontype = moonsizes[moonitem]
                        moonradius = randint(mooninfo[moontype]["Radius"][0], mooninfo[moontype]["Radius"][1])

                        # print(f"Moontype = {moontype}, radius = {moonradius}")
                    elif moontype != "random":
                        moonitem = 0
                        moonsizes[0] = moontype
                        moonradius = randint(mooninfo[moontype]["Radius"][0], mooninfo[moontype]["Radius"][1])

                        # print("HI")
                    moonchoice = mooninfo[moontype]
                    # moonmass /= 1000000000
                    # print(f"Moonmass = {moonmass}")
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
                    # mass = mooninfo[moonchoice["Mass"]]
                    # print(remainingmass)
                    # print(f"remaining_mass = {remainingmass}")
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
        if len(moons) == 0:
            # print("Error making moon, restarting")
            moons = self.moonfactory(totalmass=totalmass, planet_type=planet_type)

        return moons

    def starfactory(self):
        startypes = {

        }

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

            # print(coresplitss)
            total = 0
            for x in range(len(coresplitss)):

                # print(coresplitss[x])
                if x == 0:
                    corev.append(coresplitss[x])
                    total += coresplitss[x]
                else:
                    corev.append(coresplitss[x] - coresplitss[x - 1])
                    total += coresplitss[x] - coresplitss[x - 1]

            # print(total)
            corev.append(100 - total)
            # print(corev)
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
            # print(f"{corecontents}, {corev}")
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
            # print(finaldensity)
            totalcore["density"] = round(finaldensity, 3)

        if planettype == "Rocky Planet":
            density = {}
            corevalue = randint(10, 30)
            crustvalue = randint(0, 20)
            mantlevalue = 100 - (corevalue + crustvalue)
            mycore = getcoreterra(core)
            # print(mycore)
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
            # print(finaldensity)
            totalcore["density"] = round(finaldensity, 3)

        if planettype == "Gas Planet":

            density = {}
            corevalue = randint(10, 30)
            atmovalue = 100 - corevalue
            mycore = getcoreterra(core)
            # print(f"mycore = {mycore}")
            myatmo = getcoreterra(atmos)
            # print(mycore)
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
            # print(finaldensity)

            totalcore["density"] = round(finaldensity, 3)
        totalcore["Core Density"] = density["core"]

        return totalcore

        # print(getcore(mantle))
#     Type represents what class of planet it is
# Gravity is the strength of gravity at sea level
# Mass is the number of Earth Masses
# Ringed is whether or not the planet has rings
# subtype chooses from a basic list of features (Gasseous, Waterworld, Lavaworld, Barrenworld, Habitableworld)
# Has Life will apply if the world has life
# Life subtype will specift if there is intelligent life. This is only active on worlds with Has Life
# Settled will be given to all worlds with intelligent life
