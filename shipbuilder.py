from random import randint


class maksship():

    def __init__(self, size="random", shiptype="random", fueluse=0):
        # Ship Classes. Each ship comes with a minimum and maximum crew capacity
        # Ship classes each come with minimum and maximum ammo.
        shipsizes = ["small", "medium", "large", "massive"]
        types = ["trader", "warship", "diplomatic", "transport"]
        if size == "random":
            size = shipsizes[randint(0, len(shipsizes) - 1)]

        if size == "small":
            self.crewcapacity = randint(20, 50)
            self.ammo = 3
            self.inventory = randint(20, 30)
            self.fueluse = 2
            self.health = 10

        elif size == "medium":
            self.crewcapacity = randint(50, 80)
            self.ammo = 5
            self.inventory = randint(30, 40)
            self.fueluse = 4
            self.health = 15
        elif size == "large":
            self.crewcapacity = randint(80, 110)
            self.ammo = 8
            self.inventory = randint(40, 50)
            self.fueluse = 6
            self.health = 20

        elif size == "massive":
            self.crewcapacity = randint(110, 140)
            self.ammo = 12
            self.inventory = randint(50, 60)
            self.health = 25
            self.fueluse = 8

        if shiptype == "random":
            shiptype = types[randint(0, len(types) - 1)]

        if shiptype == "trader":
            self.ammo -= 1
            self.inventory += 30
            self.crewcapacity += 5
            self.health += 1
            self.stubborness = randint(3, 7)
            if self.fueluse > 2:
                self.fueluse -= 1

        elif shiptype == "warship":
            self.ammo += 6
            self.inventory -= 5
            self.fueluse += 1
            self.crewcapacity += 7
            self.health += 10
            self.stubborness = randint(7, 10)

        elif shiptype == "diplomatic":
            self.ammo -= 3
            self.inventory -= 7
            self.fueluse -= 1
            self.crewcapacity -= 5
            self.health -= 5
            self.stubborness = randint(1, 4)

        elif shiptype == "transport":
            self.ammo += 2
            self.inventory -= 7
            self.fueluse += 1
            self.crewcapacity += 20
            self.health -= 1
            self.stubborness = randint(3, 7)
        self.hold = {
            "Hydrogen": 0,
            "Ice": 0,
            "Iron": 0,
            "Nickel": 0,
            "Rock": 0,
            "Sulfur": 0,
            "Silicon": 0,
            "Oxygen": 0,
            "Magnesium": 0,
            "Aluminum": 0,
            "Potassium": 0,
            "Helium": 0
        }
        self.shiptype = shiptype
        self.crew = self.crewcapacity
        self.size = size
        self.maxhealth = self.health
        self.maxammo = self.ammo


    # def shipfactory():
    #
    #     return [{"crewcapacity": crewcapacity, "ammo": ammo, "inventory": inventory, "fueluse": fueluse,
    #              "shiptype": shiptype, "shipsize": size}]

