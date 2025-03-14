import random

class Grid:
    def __init__(self, width, height):
        """Create a 2D grid with empty cells."""
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.food_marker = '.'

    def place_animal(self, animal, x, y):
        """Place an animal in the specified position."""
        self.grid[y][x] = animal

    def is_within_bounds(self, x, y):
        """Make sure the animal is placed within the grid."""
        return 0 <= x < self.width and 0 <= y < self.height

    def move_animal(self, animal, old_x, old_y, new_x, new_y):
        """Move an animal from one position to another on the grid."""
        if self.is_within_bounds(new_x, new_y):
            self.grid[old_y][old_x] = None
            self.grid[new_y][new_x] = animal
            print(f"{animal.name} moved to ({new_x}, {new_y})")
        else:
            print(f"Invalid move for {animal.name} to ({new_x}, {new_y})")

    def get_cell(self, x, y):
        """Get the content of a grid cell."""
        return self.grid[y][x]

    def place_food(self, x, y):
        """Place food in the grid cell (x, y)."""
        self.grid[y][x] = self.food_marker

    def remove_food(self, x, y):
        """Remove food from the grid cell (x, y)."""
        self.grid[y][x] = None

    def remove_animal(self, x, y):
        """Remove an animal from the grid (used when a herbivore is eaten)."""
        self.grid[y][x] = None


    def populate_food(self):
        """Place food in 1/3 of the grid cells randomly."""
        # Calculate the number of cells to place food in (1/3 of the grid cells)
        total_cells = self.width * self.height
        food_cells_count = total_cells // 3

        food_cells_placed = 0
        while food_cells_placed < food_cells_count:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            # Only place food if the cell is empty (no animal in it)
            if self.grid[y][x] is None:
                self.place_food(x, y)
                food_cells_placed += 1


    def __str__(self):
        """Returns a string representation of the grid."""
        grid_str = ""
        for row in self.grid:
            row_str = ""
            for cell in row:
                if isinstance(cell, object) and hasattr(cell, 'name'):
                    # If the cell contains an animal, display the first letter of the animal's name
                    row_str += f"[{cell.name[0].upper()}]"  # Use the first letter of animal's name
                elif cell == self.food_marker:
                    # If the cell contains food, display a food marker ('.')
                    row_str += f"[{cell}]"
                else:
                    # If the cell is empty, display a space
                    row_str += "[ ]"
            grid_str += row_str + "\n"
        return grid_str


