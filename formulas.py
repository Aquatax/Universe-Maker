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
