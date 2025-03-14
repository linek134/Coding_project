import random

class Animal:
    def __init__(self, name=None, size=None, speed=None, energy_requirement=None, mutation_rate=None, mating_rate=None):
        if name is None:
            self.name = self.__class__.__name__  #default name is the class name (e.g., "Rabbit")
        else:
            self.name = name
        self.size = size
        self.speed = speed
        self.energy_requirement = energy_requirement
        self.mutation_rate = mutation_rate
        self.mating_rate = mating_rate
        total_energy_value = 15
        self.traits = {
            "size": size,
            "speed": speed,
            "energy_requirement": energy_requirement,
            "mutation_rate": mutation_rate,
            "mating_rate": mating_rate
        }
        self.total = sum(self.traits.values())
        self.energy = self.total

    def __str__(self):
        return (f"{self.name}: Size={self.size}, Speed={self.speed}, Energy={self.energy_requirement}, "
                f"Mutation Rate={self.mutation_rate}, Mating Rate={self.mating_rate}")

    def print_total(self):
        print(f"Total {self.name}: {self.total}")

    def reproduce(self, partner, grid):
        """Reproduction: If two animals of the same species are on the same spot in the grid and have energy > 10, they can reproduce."""

        # if both animals are at the same location and both have enough energy, they can reproduce
        if self.x == partner.x and self.y == partner.y and self.energy > 10 and partner.energy > 10:
            print(f"{self.name} and {partner.name} are reproducing at ({self.x}, {self.y})!")

            # choose one parent to duplicate and create the offspring
            parent_to_duplicate = random.choice([self, partner])
            offspring = self.__class__()
            # adjust offspring traits based on the mutation_rate
            num_mutations = int(offspring.traits["mutation_rate"])  # number of traits to mutate

            #list of all traits to mutate
            traits_list = list(offspring.traits.items())
            mutated_traits = {}

            #randomly choose traits to mutate
            mutated_indexes = random.sample(range(len(traits_list)), min(num_mutations, len(traits_list)))

            for i, (trait_name, value) in enumerate(traits_list):
                if i in mutated_indexes:
                    # Mutate the trait by +1 or -1
                    mutation = random.choice([-1, 1])
                    new_value = value + mutation
                    if new_value <= 0:
                        print(f"The offspring of {self.name} and {partner.name} died due to mutated traits (trait became 0 or negative).")
                        return None
                    mutated_traits[trait_name] = new_value
                else:
                    mutated_traits[trait_name] = value

            # if the offspring survived, update the mutated traits for the offspring
            offspring.traits = mutated_traits

            #put the offspring at a random empty spot on the grid
            placed = False
            while not placed:
                new_x = random.randint(0, grid.width - 1)
                new_y = random.randint(0, grid.height - 1)

                # Check if the spot is empty
                if grid.get_cell(new_x, new_y) is None:
                    grid.place_animal(offspring, new_x, new_y)  # Place the offspring in the grid
                    offspring.x, offspring.y = new_x, new_y  # Update offspring's position
                    placed = True
                    print(f"Offspring placed at ({new_x}, {new_y})")

            return offspring  # Return the created offspring

        return None

    def consume_energy(self):
        """Animals consume energy in each step"""
        self.energy -= 1
        if self.energy <= 0:
            print(f"{self.name} has run out of energy and died!")
            return False  # Animal dies
        return True


    def is_alive(self):
        return self.energy > 0

    def move(self, grid):
        """Move randomly on the grid (up, down, left, right)."""
        direction = random.choice(["up", "down", "left", "right"])
        current_x, current_y = self.x, self.y
        if direction == "up" and self.y > 0:
            new_x, new_y = current_x, current_y - 1
        elif direction == "down" and self.y < grid.height - 1:
            new_x, new_y = current_x, current_y + 1
        elif direction == "left" and self.x > 0:
            new_x, new_y = current_x - 1, current_y
        elif direction == "right" and self.x < grid.width - 1:
            new_x, new_y = current_x + 1, current_y
        else:
            return

        grid.move_animal(self, current_x, current_y, new_x, new_y)
        self.x, self.y = new_x, new_y
#        if grid.get_cell(new_x, new_y) == grid.food_marker:
 #           self.energy += 1
  #          print(f"{self.name} found food at ({new_x}, {new_y})! Energy requirement increased to {self.energy_requirement}.")
#            grid.remove_food(new_x, new_y)
