from animals.herbivore import Herbivore

class Gazelle(Herbivore):
    def __init__(self, size=None, speed=None, energy_requirement=None, mutation_rate=None, mating_rate=None):
        # Use the passed values, or default ones if None
        super().__init__(name="Gazelle",
                         size=size if size is not None else 3.0,
                         speed=speed if speed is not None else 5.0,
                         energy_requirement=energy_requirement if energy_requirement is not None else 5.0,
                         mutation_rate=mutation_rate if mutation_rate is not None else 1.0,
                         mating_rate=mating_rate if mating_rate is not None else 1.0)
