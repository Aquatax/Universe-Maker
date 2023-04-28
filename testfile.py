from random import randint
import planetmaker
from shipbuilder import maksship
from governments import GovernmentMaker
from shipbattle import battle

player_ship = maksship()
# print(player_ship.shiptype)
# print(player_ship.size)
# print(player_ship.crewcapacity)

ai_ship = maksship()

newbattle = battle(player_ship, ai_ship)
