import random


class Hat:

    houses = ["Corrino", "Harkonnen", "Atreides"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
