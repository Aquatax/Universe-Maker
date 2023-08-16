import random

import shipbuilder


class Computer:

    def __init__(self, reloading=False):
        govtypes = ["Republic", "Solar Empire", "Coalition", "Pirates"]
        if not reloading:
            self.newsave = None
            self.system = 1
            self.ship = shipbuilder.maksship(reload="ignore")
            self.planet = "None"
            self.government = random.choice(govtypes)
            self.goal = []
            self.path = []
            self.debugfail = 0
            self.code = random.randint(100000000000, 999999999999)
            self.oldpath = []
        else:
            self.system = reloading["system"]
            self.planet = reloading["planet"]
            self.ship = shipbuilder.maksship(reload=reloading["myship"])


    def saveship(self):
        newsave = {
            "system": self.system,
            "planet": self.planet,
            "goal": self.goal,
            "gov": self.government,
            "path": self.path,
            "code": self.code,
            "oldpath": self.oldpath,
            "spotinpath": 0,
            "fullpath": [],
            "debugfail": self.debugfail,
            "myship": {
                "ammo": self.ship.ammo,
                "crew capacity": self.ship.crewcapacity,
                "crew": self.ship.crew,
                "health": self.ship.health,
                "maxammo": self.ship.maxammo,
                "maxhealth": self.ship.maxhealth,
                "fueluse": self.ship.fueluse,
                "hold": self.ship.hold,
                "shiptype": self.ship.shiptype,
                "stubborness": self.ship.stubborness,
                "size": self.ship.size,
                "inventory": self.ship.inventory
            }
        }

        return newsave
