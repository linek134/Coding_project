from animals.animal import Animal

class Herbivore(Animal):
    def __init__(self, name, size, speed, energy_requirement, mutation_rate, mating_rate):
        super().__init__(name=name, size=size, speed=speed, energy_requirement=energy_requirement,
                         mutation_rate=mutation_rate, mating_rate=mating_rate)

