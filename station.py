from random import randint
from random import choice
class mkstation():
    govtypes = ["Republic", "Solar Empire", "Coalition", "Pirates"]
    def __init__(self, faction = choice(govtypes)):
        
        self.prices = {
            "fuel": {"price": randint(3, 7), "amount": 20},
            "hydrogen": {"price": randint(3, 7), "amount": 20},
            "iron": {"price": randint(3, 7), "amount": 20}
        }
        self.weapons = {
            "ammo": {"price": randint(3, 7), "amount": 20}
            }
        self.crew = {
            "max_crew": randint(25, 70),
            "current": randint(5, 25),
            "last_turn_checked": 0
        }
        self.faction = faction
