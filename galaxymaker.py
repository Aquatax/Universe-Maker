import random
from random import randint
import planetmaker


def galaxymakerr(minimum_systems, include_moons=True):
    # print("HERE")
    # Code by Aquatax
    # Write Below Here \/ \/ \/

    number_of_systems = round(minimum_systems)
    number_of_overflow_systems = round(minimum_systems / 2)

    # Write above here /\ /\ /\

    lifecounter = 0

    def system_checker(systemb, systemc):
        if systemb == systemc:
            return True
        else:
            return False

    movements = 0

    system_names = ["Alpha",
                    "Beta",
                    "Gamma",
                    "Delta",
                    "Epsilon",
                    "Zeta",
                    "Eta",
                    "Theta",
                    "Iota",
                    "Kappa",
                    "Lambda",
                    "Mu",
                    "Nu",
                    "Xi",
                    "Omicron",
                    "Pi",
                    "Rho",
                    "Sigma",
                    "Tau",
                    "Upsilon",
                    "Phi",
                    "Chi",
                    "Psi",
                    "Omega",
                    ]
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P", "Q", 'R', "S",
                'T', "U", "V", "W", "X", "Y", "Z"]
    alphalower = []
    for value in alphabet:
        alphalower.append(value.lower())
    # print(alphalower)

    systems = {}
    for x in range(1, number_of_systems + 1 + number_of_overflow_systems):
        systemname = random.choice(system_names) + random.choice(alphabet) + (random.choice(alphabet)) + str(
            randint(0, 9)) + str(randint(0, 9))
        newSystem = str(f"system{x}")
        systems[newSystem] = {
            "Name": systemname,
            "links": [],
            "planets": []
        }

    systems_broken = 0
    systems["system1"]["links"] = [2, 3, 4, 5, 6, 7, 8, 9]

    # print(systems["system1"][0]["links"])
    for x in systems["system1"]["links"]:
        selectSystem = f"system{x}"
        systems[selectSystem]["links"].append(1)

    # print(systems)
    for x in range(2, number_of_systems + 1):

        SysteminQuestion = f"system{x}"
        startingLength = len(systems[SysteminQuestion]["links"])
        if startingLength < 8:
            while len(systems[SysteminQuestion]["links"]) < 8:
                systema = randint(2, number_of_systems + number_of_overflow_systems)
                while system_checker(systema, x) == True:
                    systema = randint(2, number_of_systems + number_of_overflow_systems)
                newsysteminquestion = f"system{systema}"
                if len(systems[newsysteminquestion]["links"]) < 8:
                    go = 1

                    # checks if the number is repeated in the list. If it does repeat in the list it will move on
                    # and not append the number
                    for z in systems[SysteminQuestion]["links"]:
                        if z == systema:
                            go = 0
                            systems_broken += 1
                            if SysteminQuestion == number_of_systems:
                                go = 1

                            if systems_broken > 3:
                                go = 2
                                systems_broken = 0

                    if go == 1:
                        movements += 1
                        systems[newsysteminquestion]["links"].append(x)
                        systems[SysteminQuestion]["links"].append(systema)
                elif x == newsysteminquestion:
                    pass

    for x in range(2, number_of_systems + 1):

        SysteminQuestion = f"system{x}"
        number_of_planets = randint(0, 10)
        # At most 9 planets. If planet number is 0, it should skip
        # print(systems[SysteminQuestion]["Name"])
        for planetnum in range(0, number_of_planets):
            if planetnum == 0:
                pass
            else:
                newplanet = planetmaker.makeplanet()
                planetinfo = newplanet.planetfactory(include_moons=include_moons)
                #                 Example of what would be returned
                # return [{"Type": typeer}, {"Gravity": gravity}, {"Ringed": hasring}, {"Subtype": subtype},
                # {"Has Life": haslife}, {"Life Subtypes": lifesubtypes}, {"Settled": settled}]

                # Ideal planet dict
                # "Planets": [{"Planet1": [{"Name": "Jupiter"}, {"Type": "Gas Giant"}, {"Ringed: True"}, {"Subtype": "Gaseous"},
                #  {"Has Life": False}, {"Life Subtypes": None}{"Settled": False}, {"Gravity": 5}, ]}]

                typeer = planetinfo["Type"]
                grav = planetinfo["Gravity"]
                ringed = planetinfo["Ringed"]
                subtype = planetinfo["Subtype"]
                haslife = planetinfo["Has Life"]
                lifesubtype = planetinfo["Life Subtypes"]
                settled = planetinfo["Settled"]
                moons = planetinfo["Moons"]
                planetpoint = f"planet{planetnum}"
                name = systems[SysteminQuestion]["Name"] + alphalower[planetnum]
                if settled:
                    lifecounter += 1

                newplaneta = {
                    planetpoint: {
                        "Name": name,
                        "Type": typeer,
                        "Ringed": ringed,
                        "Subtype": subtype,
                        "Has Life": haslife,
                        "Life Subtypes": lifesubtype,
                        "Settled": settled,
                        "Gravity": grav,
                        "Moons": moons}}
                systems[SysteminQuestion]["planets"].append(newplaneta)

    return systems
