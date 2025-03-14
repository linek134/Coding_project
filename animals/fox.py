from animals.carnivore import Carnivore

class Fox(Carnivore):
    def __init__(self, size=None, speed=None, energy_requirement=None, mutation_rate=None, mating_rate=None):
        # Use the passed values, or default ones if None
        super().__init__(name="Fox",
                         size=size if size is not None else 2.0,
                         speed=speed if speed is not None else 2.0,
                         energy_requirement=energy_requirement if energy_requirement is not None else 3.0,
                         mutation_rate=mutation_rate if mutation_rate is not None else 4.0,
                         mating_rate=mating_rate if mating_rate is not None else 4.0)

