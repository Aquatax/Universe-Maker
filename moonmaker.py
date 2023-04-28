import random
from random import randint

class MakeMoon:

    def __init__(self):
        pass


    def moonfactory(self, totalmass, planet_type):

        moons = []
        remainingmass = totalmass * 0.15
        moonsizes = ["moon1", "moon2", "moon3", "moon4", "moon5"]
        mooninfo = {
            "moon1": [{"Mass": [0.00001, 0.0001]}, {"Gravity": [0.001, 0.01]}, {"Shape": ["Irregular", "Spherical"]}],
            "moon2": [{"Mass": [0.0001, 0.001]}, {"Gravity": [0.01, 0.1]}, {"Shape": ["Irregular", "Spherical"]}],
            "moon3": [{"Mass": [0.001, 0.01]}, {"Gravity": [0.1, 0.5]}, {"Shape": ["Irregular", "Spherical"]}],
            "moon4": [{"Mass": [0.01, 0.1]}, {"Gravity": [0.5, 1]}, {"Shape": ["Spherical"]}],
            "moon5": [{"Mass": [0.1, 1]}, {"Gravity": [1, 6]}, {"Shape": ["Spherical"]}]}
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

        for x in range(0, slots):
            if remainingmass * 1000 > totalmass:
                currentmoon = {}
                moonitem = random.randint(0, 4)
                moonchoice = mooninfo[moonsizes[moonitem]]
                moonmass = float(random.randint(moonchoice[0]["Mass"][0] * 100000, moonchoice[0]["Mass"][1] * 100000)) \
                           / 100000
                moongrav = float(random.randint(moonchoice[1]["Gravity"][0] * 100000,
                                                moonchoice[1]["Gravity"][1] * 100000)) / 100000
                moonshape = random.choice(moonchoice[2]["Shape"])
                # mass = mooninfo[moonchoice["Mass"]]
                # print(remainingmass)
                remainingmass -= moonmass

                currentmoon = {
                    "Type": moonsizes[moonitem],
                    "Mass": moonmass,
                    "Gravity": moongrav,
                    "Shape": moonshape
                }

                moons.append(currentmoon)



        return moons
