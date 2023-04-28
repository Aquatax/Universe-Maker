from random import *
import math

def coremaker(planettype):


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
        corev.append(100-total)
        # print(corev)
        ccorev  =corev

        corecontents = []
        # corecontents.append(choice(whatarewetesting))
        # place = randint(0, len(whatarewetesting) - 1)
        # corecontents.append(whatarewetesting[place])
        # del(whatarewetesting[place])
        #
        while len(corecontents) < len(corev):
            place = randint(0, len(whatarewetesting) - 1)
            corecontents.append(whatarewetesting[place])
            del(whatarewetesting[place])
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

    if planettype == "Dwarf Planet":
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
    return totalcore



    # print(getcore(mantle))




values = []
for x in range(1, 100000):
    z = coremaker("Gas Planet")
    # print(z)
    newz = z["density"]

    values.append(round(newz, 3))

print(values)

print(f"Average={round(sum(values) / len(values), 3)}, Max={max(values)}, Min={min(values)} ")

# for x in range(4, 0, -1):
#     print(x)