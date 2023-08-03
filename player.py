import shipbuilder
# strings = "Hello"
# print(strings[-1])
class Player:


    def __init__(self, reloading=False):
        if not reloading:
            self.newsave = None
            self.system = "system1"
            self.ship = shipbuilder.maksship(reload="ignore")
            self.planet = "None"
        else:
            self.system = reloading["system"]
            self.planet = reloading["planet"]
            self.ship = shipbuilder.maksship(reload=reloading["myship"])

    def saveship(self):
        newsave = {
            "system" : self.system,
            "planet" : self.planet,
            "myship" : {
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


