from animals.herbivore import Herbivore

class Rabbit(Herbivore):
    def __init__(self, size=None, speed=None, energy_requirement=None, mutation_rate=None, mating_rate=None):
        super().__init__(name="Rabbit", 
                         size=size if size is not None else 1.0, 
                         speed=speed if speed is not None else 2.0, 
                         energy_requirement=energy_requirement if energy_requirement is not None else 3.0, 
                         mutation_rate=mutation_rate if mutation_rate is not None else 4.0, 
                         mating_rate=mating_rate if mating_rate is not None else 5.0)
