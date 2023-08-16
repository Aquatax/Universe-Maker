import random
from random import randint
import planetmaker
from formulas import planetnumber
import formulas
from planetmaker import makeplanet


def galaxymakerr(minimum_systems, include_moons=True):
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

    systems = {}
    for x in range(1, number_of_systems + 1 + number_of_overflow_systems):
        systemname = f"{random.choice(nouns)} {random.choice(adjectives)} {(random.choice(alphabet))} "
        newSystem = str(f"system{x}")
        systems[newSystem] = {
            "Name": systemname,
            "links": [],
            "SystemScan": False,
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

    for x in systems["system1"]["links"]:
        selectSystem = f"system{x}"
        systems[selectSystem]["links"].append(1)

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

    for x in range(1, number_of_systems + 1 + number_of_overflow_systems):

        SysteminQuestion = f"system{x}"
        number_of_planets = randint(0, 10)
        if SysteminQuestion == "system1":
            number_of_planets = randint(4, 9)
        # At most 8 planets. If planet number is 0, it should skip
        listplanets = ["Gas Giant", "Ice Giant", "Super Earth", "Rocky Planet", "Dwarf Planet"]

        planettypes = {  # This shows the planet types along with the number of points it gets towards star cost
            "Gas Giant": 20,
            "Ice Giant": 15,
            "Super Earth": 9,
            "Rocky Planet": 7,
            "Dwarf Planet": 2,
        }

        newstar = planetmaker.makeplanet()  # This Prepares planet production
        if SysteminQuestion == "system1":  # This section is only run if it is the starting system
            newerstar = newstar.starfactory(wanted_star="G")  # Creates a Yellow Star
        else:
            newerstar = newstar.starfactory(wanted_star="random")  # Creates a random star

        if SysteminQuestion == "system1":  # This section is only run if it is the starting system
            newerstar["Value"] = 100  # This sets the planet points to 100
            TotalPoints = 100  # This sets the planet points to 100
        else:
            TotalPoints = newerstar["Value"]  # This sets TotalPoints to the stars planet points
        for planetnum in range(0, 9):  # This section creates the planets, up to 8 planets
            if planetnum == 0:
                pass
            else:
                if SysteminQuestion == "system1" and planetnum == 3:  # The first few if statements are for spawn
                    newplanet = planetmaker.makeplanet()
                    planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype="Rocky Planet",
                                                         forcelife=True)
                    cont = True
                    TotalPoints -= 98
                elif SysteminQuestion == "system1" and planetnum <= 4:
                    newplanet = planetmaker.makeplanet()
                    planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype="Rocky Planet",
                                                         forcelife=False)
                    cont = True
                elif SysteminQuestion == "system1" and planetnum <= 6:
                    newplanet = planetmaker.makeplanet()
                    planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype="Gas Giant")
                    cont = True
                elif SysteminQuestion == "system1" and planetnum <= 8:
                    newplanet = planetmaker.makeplanet()
                    planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype="Ice Giant")
                    cont = True
                else:
                    planetchosen = random.choice(listplanets)  # This chooses a random planet
                    if planettypes[planetchosen] <= TotalPoints:  # This tests if the planet will fit
                        TotalPoints -= planettypes[planetchosen]  # This subtracts planet points from the system
                        cont = True
                    else:  # Planet production completely stops if one is too large
                        cont = False
                        break
                    if SysteminQuestion != "system1" and random.randint(0, 3) == 3:
                        break
                    if cont:
                        newplanet = planetmaker.makeplanet()
                        planetinfo = newplanet.planetfactory(include_moons=include_moons, forceplanettype=planetchosen)
                #                 Example of what would be returned
                # return [{"Type": typeer}, {"Gravity": gravity}, {"Ringed": hasring}, {"Subtype": subtype},
                # {"Has Life": haslife}, {"Life Subtypes": lifesubtypes}, {"Settled": settled}]

                # Ideal planet dict
                # "Planets": [{"Planet1": [{"Name": "Jupiter"}, {"Type": "Gas Giant"}, {"Ringed: True"}, {"Subtype": "Gaseous"},
                #  {"Has Life": False}, {"Life Subtypes": None}{"Settled": False}, {"Gravity": 5}, ]}]
                if cont:
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
                            "HasBeenScannned": False,
                            "Moons": moons,
                            "Core": core
                        }}

                    systems[SysteminQuestion]["planets"].append(newplaneta)
        StarProperties = newerstar
        systems[SysteminQuestion]["stars"] = {"Star1": StarProperties}

        currentstar = 2
        startingpoints = TotalPoints
        while currentstar < 7:
            goahead = 0
            if TotalPoints >= 200 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="O")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 200
            elif TotalPoints >= 175 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="B")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 175
            elif TotalPoints >= 150 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="A")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 150
            elif TotalPoints >= 100 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="F")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 100
            elif TotalPoints >= 70 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="G")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 70
            elif TotalPoints >= 50 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="K")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 50
            elif TotalPoints >= 30 and random.randint(0, 1) == 1:
                secondstar = newstar.starfactory(wanted_star="M")
                goahead = 1
                # TotalPoints += round(secondstar["Value"] / 1.5)
                TotalPoints -= 30
            if goahead == 1:
                systems[SysteminQuestion]["stars"][f"Star{currentstar}"] = secondstar
                currentstar += 1
            if random.randint(0, 2) == 0:
                break

        if currentstar > 4:
            pass

    return systems


def galaxylinks():
    import json

    with open('systems.json') as json_file:
        galaxy = json.load(json_file)
    system2 = {}

    # print(galaxy["system1"]["links"])
    for code in range(1, len(galaxy) + 1):
        mysystemnumber = code
        mysystem = f"system{mysystemnumber}"
        systemsnumbered = []
        for x in galaxy[mysystem]["links"]:
            systemsnumbered.append([mysystemnumber, x])
        for rangenumber in range(0, 7):
            for x in systemsnumbered:
                mylist = galaxy[f"system{x[-1]}"]["links"]
                for value in mylist:
                    cont = True
                    for value2 in systemsnumbered:
                        if value == value2[-1]:
                            cont = False
                        if len(systemsnumbered) == len(galaxy):
                            break
                    if cont:
                        newlist = []
                        for newvalue in x:
                            newlist.append(newvalue)
                        newlist.append(value)
                        systemsnumbered.append(newlist)
                    if len(systemsnumbered) == len(galaxy):
                        break
                if len(systemsnumbered) == len(galaxy):
                    break
            if len(systemsnumbered) == len(galaxy):
                break
        system2[mysystem] = systemsnumbered

        # print(f"{mysystem} is Done")
    json_object = json.dumps(system2, default=lambda o: o.__dict__, sort_keys=False, indent=4)
    with open('SystemLinks.json', 'w') as fp:
        fp.write(json_object)
    return system2
