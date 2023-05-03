from random import randint


class GovernmentMaker:

    def __init__(self):
        pass

    def bicameral_factory(self):
        odds = [1, 2, 2, 3, 3, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.06, 5.12, 5.18, 5.25, 5.31, 5.37, 5.43, 5.5, 5.56, 5.62,
                5.68, 5.75, 5.81, 5.87, 5.93, 6, 6.2, 6.4, 6.6, 6.8, 7, 7, 8, 8, 9]
        preference_in_division = odds[randint(0, len(odds) - 1)]
        lower_house = []

        members_in_upper = randint(30, 100)
        members_in_lower = randint(80, 200)
        preference_in_globalists_in_lower = int(preference_in_division * 10)
        preference_in_globalists_in_upper = preference_in_globalists_in_lower + randint(-5, 5)
        print(preference_in_globalists_in_upper)
        print(preference_in_globalists_in_lower)

        global_in_upper = int(preference_in_globalists_in_upper / 100 * members_in_upper)
        isolationists_in_upper = members_in_upper - global_in_upper
        global_in_lower = int(preference_in_globalists_in_lower / 100 * members_in_lower)
        isolationists_in_lower = members_in_lower - global_in_lower

        type_of_government = 0
        print(preference_in_division)
        return [{
            "Members In Upper": members_in_upper,
            "Members In Lower": members_in_lower,
            "Islt In Upper": isolationists_in_upper,
            "Islt In Lower": isolationists_in_lower,
            "Glob In Upper": global_in_upper,
            "Glob In Lower": global_in_lower
        }]

    def parlimentary_factory(self):
        pass



