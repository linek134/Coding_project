# main.py
from animals.ecosystem import Ecosystem

def main():
    # Prompt the user for input on the number of each type of animal
    print("Welcome to the Ecosystem Simulation!")
    
    # Getting user input for the grid dimensions and number of each animal
    grid_width = int(input("Enter the grid width: "))
    grid_height = int(input("Enter the grid height: "))
    
    num_rabbits = int(input("Enter the number of rabbits: "))
    num_foxes = int(input("Enter the number of foxes: "))
    num_lions = int(input("Enter the number of lions: "))
    num_zebras = int(input("Enter the number of zebras: "))
    num_gazelles = int(input("Enter the number of gazelles: "))
    num_eagles = int(input("Enter the number of eagles: "))

    # Initialize the ecosystem with the user's inputs
    print("\nInitializing Ecosystem...")
    ecosystem = Ecosystem(grid_width=grid_width, grid_height=grid_height, 
                          num_rabbits=num_rabbits, num_foxes=num_foxes, 
                          num_lions=num_lions, num_zebras=num_zebras, 
                          num_gazelles=num_gazelles, num_eagles=num_eagles)
    print(ecosystem.grid)
    print("\nStarting Simulation...")

    # Simulate for a certain number of rounds
    rounds = int(input("\nEnter the number of simulation rounds: "))
    
    for round_number in range(1, rounds + 1):
        print(f"\n----- Round {round_number} -----")
        ecosystem.simulate_round()

        # After each round, display the grid
        print("\nGrid after round", round_number)
        print(ecosystem.grid)  # Print the grid to display it

if __name__ == "__main__":
    main()
