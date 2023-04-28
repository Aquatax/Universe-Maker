from shipbuilder import maksship
import os
from random import randint


class battle():

    def __init__(self, ship1, ship2):
        self.retreat = 0
        print(ship1.health)
        print(ship2.health)
        toolhelp = input("Do you need help with battle? y/n:")
        if toolhelp == "y":
            print("type a for attack, b for board, r for retreat")
            input("continue")
            os.system('cls')
            print("attacking will expend one ammo. Base hit chance is 50%. Base hit damage is between 5 - 7 hp")
            input("continue")
            os.system('cls')
            print("boarding will set your crew against theirs. Attackers have a bonus. for every attacker killed")
            print("the defender will lose 25-50 more of their crew")
            print("boarding ends when either you outnumber the crew 3:1 or 50% of their crew is lost")
            input("continue")
            os.system('cls')
            print("retreating ends the battle")
            input()
            os.system('cls')
        cont = True
        while cont:
            os.system('cls')
            print(f"Health: Player {ship1.health} = {ship2.health} Enemy")
            print(f"Ammo: Player {ship1.ammo} = {ship2.ammo} Enemy")
            print(f"Crew: Player {ship1.crew} = {ship2.crew} Enemy")
            self.commands(ship1, ship2, cont)
            if (ship2.health <= 0 or ship2.crew <= ship1.crew * 0.25) and cont:
                print("You Won")
                cont = False
            if (ship1.health <= 0 or ship1.crew <= ship2.crew * 0.25) and cont:
                cont = False
                print("You Lost")
            if self.retreat == 1:
                cont = False
            elif self.retreat == 2:
                cont = False
            self.arty(ship1, ship2, cont)
            if (ship1.health <= 0 or ship1.crew <= ship2.crew * 0.25) and cont:
                cont = False
                print("You Lost")
            if (ship2.health <= 0 or ship2.crew <= ship1.crew * 0.25) and cont:
                print("You Won")
                cont = False

        input("Game Over")

    def commands(self, ship1, ship2, cont):
        if cont:
            command = str.lower(input("command:"))
            if command == "a" and ship1.ammo > 0:
                if randint(0, 1) == 1:
                    ship2.health -= randint(1, 7)
                    ship1.ammo -= 1
                    ship2.crew -= randint(0, 3)
                else:
                    print("Player Missed")
                    ship1.ammo -= 1
            elif command == "b":
                temploss = randint(0, 15)
                ship1.crew -= temploss
                ship2.crew -= int(temploss * (randint(0, 15) * 0.1))
            elif command == "r":
                if randint(0, 1) == 1:
                    print("You've Retreated")
                    self.retreat = 1
                else:
                    print("Retreat Failed")
            elif command == "s":
                self.retreat = 2
                print("You've Surrendered")

    def arty(self, ship1, ship2, cont):
        if cont and ship2.ammo > 2:
            if randint(0, 1) == 1:
                ship1.health -= randint(1, 7)
                ship2.ammo -= 1
                ship1.crew -= randint(0, 3)
            else:
                print("Enemy Missed")

