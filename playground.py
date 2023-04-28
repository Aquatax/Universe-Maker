from random import randint
import planetmaker
from shipbuilder import maksship
from governments import GovernmentMaker
import moonmaker
import math
y = []
x = planetmaker.makeplanet()
newx = x.planetfactory(include_moons="False")
print(newx)

