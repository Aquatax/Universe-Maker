import random
from random import randint
import planetmaker
from formulas import planetnumber
import formulas
def galaxymakerr(minimum_systems, include_moons=True):
    # print("HERE")
    # Code by Aquatax
    # Write Below Here \/ \/ \/

    number_of_systems = round(minimum_systems)
    number_of_overflow_systems = round(minimum_systems / 2)

    # Write above here /\ /\ /\
    nouns = formulas.nouns
    adjectives = formulas.adjectives
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
        systemname = f"{random.choice(nouns)} {random.choice(adjectives)} {(random.choice(alphabet))} "
        newSystem = str(f"system{x}")
        systems[newSystem] = {
            "Name": systemname,
            "links": [],
            "planets": []
        }
    makeplanet = planetmaker.makeplanet()
    planet1 = makeplanet.planetfactory(include_moons=include_moons)
    planet2 = makeplanet.planetfactory(include_moons=include_moons, forceplanettype="Rocky Planet")
    planet3 = makeplanet.planetfactory(include_moons=include_moons)
    planet4 = makeplanet.planetfactory(include_moons=include_moons)
    planet5 = makeplanet.planetfactory(include_moons=include_moons)
    planet6 = makeplanet.planetfactory(include_moons=include_moons)
    planet7 = makeplanet.planetfactory(include_moons=include_moons)
    SysteminQuestion = "system1"
    # for x in range(1, 7):
    #     if x == 1:
    #         planetinfo = planet1
    #         planetnum = 1
    #     elif x == 2:
    #         planetinfo = planet2
    #         planetnum = 2
    #     elif x == 3:
    #         planetinfo = planet3
    #         planetnum = 3
    #     elif x == 4:
    #         planetinfo = planet4
    #         planetnum = 4
    #     elif x == 5:
    #         planetinfo = planet5
    #         planetnum = 5
    #     elif x == 6:
    #         planetinfo = planet6
    #         planetnum = 6
    #     else:
    #         planetinfo = planet7
    #         planetnum = 7
    #     typeer = planetinfo["Type"]
    #     grav = planetinfo["Gravity"]
    #     ringed = planetinfo["Ringed"]
    #     subtype = planetinfo["Subtype"]
    #     haslife = planetinfo["Has Life"]
    #     lifesubtype = planetinfo["Life Subtypes"]
    #     settled = planetinfo["Settled"]
    #     moons = planetinfo["Moons"]
    #     planetpoint = f"planet{planetnum}"
    #     name = systems[SysteminQuestion]["Name"] + alphalower[planetnum]
    #     if settled:
    #         lifecounter += 1
    #
    #     newplaneta = {
    #         planetpoint: {
    #             "Name": name,
    #             "Type": typeer,
    #             "Ringed": ringed,
    #             "Subtype": subtype,
    #             "Has Life": haslife,
    #             "Life Subtypes": lifesubtype,
    #             "Settled": settled,
    #             "Gravity": grav,
    #             "Moons": moons}}
    #     systems[SysteminQuestion]["planets"].append(newplaneta)







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

    for x in range(1, number_of_systems + 1):

        SysteminQuestion = f"system{x}"
        number_of_planets = randint(0, 10)
        if SysteminQuestion == "system1":
            number_of_planets = randint(4, 9)
        # At most 8 planets. If planet number is 0, it should skip
        # print(systems[SysteminQuestion]["Name"])
        for planetnum in range(0, number_of_planets):
            if planetnum == 0:
                pass
            else:
                if SysteminQuestion == "system1" and planetnum == 3:
                    newplanet = planetmaker.makeplanet()
                    planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype="Rocky Planet",
                                                         forcelife=True)
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
                core = planetinfo["core"]
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
                        "Moons": moons,
                        "Core": core
                    }}

                systems[SysteminQuestion]["planets"].append(newplaneta)
    # print(lifecounter)

    return systems
