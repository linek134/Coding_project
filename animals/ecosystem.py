# ecosystem.py
from .grid import Grid
from .carnivore import Carnivore
from .herbivore import Herbivore
from .rabbit import Rabbit
from .fox import Fox
from .lion import Lion
from .eagle import Eagle
from .zebra import Zebra
from .gazelle import Gazelle
import random

class Ecosystem:
    def __init__(self, grid_width, grid_height, num_rabbits, num_foxes, num_lions, num_zebras, num_gazelles, num_eagles):
        self.grid = Grid(grid_width, grid_height)  # Create an empty grid
        self.animals = []  # List to store all the animals

        """create animals based on user input"""
        for _ in range(num_rabbits):
            rabbit = Rabbit()
            self.animals.append(rabbit)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            rabbit.x, rabbit.y = x, y
            self.grid.place_animal(rabbit, x, y)

        for _ in range(num_foxes):
            fox = Fox()
            self.animals.append(fox)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            fox.x, fox.y = x, y
            self.grid.place_animal(fox, x, y)

        for _ in range(num_lions):
            lion = Lion()
            self.animals.append(lion)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            lion.x, lion.y = x, y
            self.grid.place_animal(lion, x, y)

        for _ in range(num_zebras):
            zebra = Zebra()
            self.animals.append(zebra)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            zebra.x, zebra.y = x, y
            self.grid.place_animal(zebra, x, y)

        for _ in range(num_gazelles):
            gazelle = Gazelle()
            self.animals.append(gazelle)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            gazelle.x, gazelle.y = x, y
            self.grid.place_animal(gazelle, x, y)

        for _ in range(num_eagles):
            eagle = Eagle()
            self.animals.append(eagle)
            x, y = random.randint(0, grid_width-1), random.randint(0, grid_height-1)
            eagle.x, eagle.y = x, y
            self.grid.place_animal(eagle, x, y)

        self.populate_grid()

    def populate_grid(self):
        
        """Populate the grid with animals at random locations."""
        for animal in self.animals:
            placed = False
            while not placed:
                x = random.randint(0, self.grid.width - 1)
                y = random.randint(0, self.grid.height - 1)
                """Only put animals in empty cells in the population step"""
                if self.grid.grid[y][x] is None:
                    self.grid.place_animal(animal, x, y)
                    animal.x, animal.y = x, y
                    placed = True
        """Put food items in the grid"""
        self.grid.populate_food()


    def simulate_round(self):
        """Simulate a round of actions for all animals in the ecosystem."""
        for animal in self.animals:
            if animal.is_alive():
 #               if isinstance(animal, Carnivore):
#                    animal.hunt(self.grid)
                if animal.is_alive():    
                    animal.move(self.grid)  # Move animals on the grid randomly
                    animal.consume_energy()  # all animals lose energy in each move


                #reproduction logic
                for partner in self.animals:
                    if partner is not animal and isinstance(partner, animal.__class__): #if two animals are at the same spot and the same class
                        offspring = animal.reproduce(partner, self.grid)  # Pass the grid as an argument to reproduce method
                        if offspring:
                            print(f"A new {offspring.name} is born!")
                            self.animals.append(offspring)  # Add offspring to ecosystem





