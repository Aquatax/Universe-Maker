# Givens
import math



def mass(formula, volume=0, density=0, weight=0, gravity=0, force=0, acceleration=0):
    '''
    Formula options:

    1: mass = force * acceleration

    2: mass = volume * density

    3: mass = weight / gravity

    :param formula:
    :param volume:
    :param density:
    :param weight:
    :param gravity:
    :param force:
    :param acceleration:
    :return:
    '''
    if formula == 1:
        mass = force * acceleration
    elif formula == 2:
        mass = volume * density
    elif formula == 3:
        mass = weight / gravity
    return mass
def volume(self, formula, density=0, mass=0, radius=0):
    if formula == 1:
        #Volume with Mass and Density
        volume = mass / density
    elif formula == 2:
        #Formula for a sphere
        volume = (4/3) * math.pi * (radius ** 3)

def planetnumber(letter):
    if letter == "b":
        return 1
    elif letter == "c":
        return 2
    elif letter == "d":
        return 3
    elif letter == "e":
        return 4
    elif letter == "f":
        return 5
    elif letter == "g":
        return 6
    elif letter == "h":
        return 7
    elif letter == "i":
        return 8
    elif letter == "j":
        return 9
    elif letter == "k":
        return 10
    elif letter == "l":
        return 11
    elif letter == "m":
        return 12
    elif letter == "n":
        return 13
    elif letter == "o":
        return 14
    elif letter == "p":
        return 15

def planetletter(number):
    if number == 1:
        return "b"
    elif number == 2:
        return "c"
    elif number == 3:
        return "d"
    elif number == 4:
        return "e"
    elif number == 5:
        return "f"
    elif number == 6:
        return "g"
    elif number == 7:
        return "h"
    elif number == 8:
        return "i"
    elif number == 9:
        return "j"
    elif number == 10:
        return "k"

nouns = ["Warriors", "Archers", "Pheonixs", "Lions", "Hares", "Stephens", "Kings", "Queens", "Misty",
         "Mountains", "Burrowed", "Caves", "Homers", "Bureaucrats", "Monsters", "Crabs", "Boils", "Elks",
         "Portions", "Mans", "Creatures", "Lovely", "Stoneworks", "Snowy", "Nebulas", "Planets", "Fairy",
         "Hunters", "Fields", "Bowmans", "Chiefs", "Cardinals", "Eagles", "Fathers", "Mothers", "Brothers",
         "Sisters", "Uncles", "Aunts", "Stories", "Fictions", "Holidays", "Wires",
         "Felicitys", "Susies", "Darwins", "Newtons", "Einsteins", "Curies", "Copernicans", "Faradays",
         "Gallileos", "Hawkings"]
adjectives = ["Clouds", "Love", "Pride", "Fall", "Birth", "Hate", "Lust", "Edge", "String", "Soup", "Pie", "Refinery",
              "Odyssey", "Tale", "Adventure", "Thirst", "Pain", "Deep", "Order", "End", "Start", "Fart", "Shine",
              "Rays", "Rocks", "Debris", "War", "Battle", "Judge", "Mark", "Arrival", "Grave", "Strength", "Armada",
              "Haven", "Sea", "Surprise", "Maneuver", "Folly", "Victory", "Defeat", "Horde", "Tactics", "Run", "Dream",
              "Theatrics", "Cold", "Heat", "Warmth", "Warning", "Tears", "Teeth", "Kiss", "Rift", "Stranger"]
Systemnames = {
    "Warriors": ["Pride", "Fall", "Odyssey", "Remains", "Mark", "End", "Haven", "Folly", "Grave", "Strength", "Run"],
    "Archers": ["Pride", "Fall", "Odyssey", "Remains", "Mark", "End", "Haven", "Folly", "Rift"],
    "Lions": ["Den", "Pride", "Grave"],
    "Mountain": ["Song", "Tear", "Pass", "War", "Rays", "Mist", "Rain"],
    "Poets": ["Fortune", "Grace", "Melody", "Tale", "Grave", "Strength"],
    "Adventurers": ["Love", "Pride", "Fall", "Folly", "Theatrics", "Maneuver", "Suprise", "Run", "Haven", "Mark"],
    "Kings": ["Gambit", "War", "Run", "Armada", "Folly", "Odyssey", "Victory", "Defeat", "Horde"]






}
