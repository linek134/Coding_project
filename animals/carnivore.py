from animals.animal import Animal

# animales that are carnivores (lion, eagle, fox)
class Carnivore(Animal):
    def __init__(self, name, size, speed, energy_requirement, mutation_rate, mating_rate):
        super().__init__(name, size, speed, energy_requirement, mutation_rate, mating_rate)
