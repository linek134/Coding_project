from animals.herbivore import Herbivore

class Zebra(Herbivore):
    def __init__(self, size=None, speed=None, energy_requirement=None, mutation_rate=None, mating_rate=None):
        super().__init__(name="Zebra",
                         size=size if size is not None else 3.0,
                         speed=speed if speed is not None else 3.0,
                         energy_requirement=energy_requirement if energy_requirement is not None else 4.0,
                         mutation_rate=mutation_rate if mutation_rate is not None else 2.0,
                         mating_rate=mating_rate if mating_rate is not None else 3.0)
