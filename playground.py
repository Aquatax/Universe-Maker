from random import randint
import planetmaker
from shipbuilder import maksship
from governments import GovernmentMaker
import moonmaker
import math
import formulas
# y = []
x = planetmaker.makeplanet()
newx = x.planetfactory(include_moons=True, forceplanettype="Dwarf Planet")
# print(newx)
GConstant = 6.6743 * 10**(-11)
# Make sure that you are using kilograms and meters for G

# Mass is in kilograms
mass = 3.130440771794056 * 10 ** 25


# density is in g/cm^3
density = 3.577


# Density is now kg/m^3
density *= 1000


# volume is kg/m^3
volume = mass / density


radius = (3 * mass / (4 * math.pi * density)) ** (1/3)
# radius is in centimeters
gravity = GConstant * (mass / ((radius) ** 2))

# print(f"Mass={mass}, Density={density}, Volume={volume}, Radius={radius}, Gravity={gravity}")
# radius = math.cbrt((3 * volume) / (4 * math.pi))
# radius = math.cbrt((3*mass)/(4*math.pi*density))

