# Coding project
Repository for the coding project in the Advanced scientific programming with Python course 2025.

# Project Description
The idea of my project is to create a simulation of an ecosystem, in which different species (classes of objects) live and compete for resources.
First, the user has to specify the number of objects to be created for each species. Each species will be associated with numerical values for different traits, such as: size, speed, energy(food) requirements, mutation rate and mating rate. 
The values for the traits sums up to an energy value. The initial energy value is equal for all species. 
The energy value for the objects will be increased or decreased based on how well the object performs in the resource-competition.
If the energy value reaches 0 the object will die (be removed from the ecosystem). 

The resources will be: food and partner availability. 
There will be food available for all species. Some species can also consume other species as food. 

Mutations are modelled by slight changes in the trait values for each new generation.
The simulation runs in cycles (ca. 100 generations) where species interact, reproduce, and evolve. 

The visualization of the simulation will be text-based. Key aspects such as the availability of food and mating resources, population sizes, and energy levels for each species will be represented using ASCII characters. This will allow users to follow the ecosystem’s health and track the evolution of species as the simulation progresses.

A suggested structure for the project is:
ecosystem_simulation/
│
├── main.py                   # entry point for the simulation, runs the simulation loop
├── ecosystem.py              # the ecosystem class with resources and simulation logic
├── species.py                # the species class specifying each species and their traits
├── resources.py              # contains the resource class for food and mating resouurces
├── visualization.py          # functions to generate text-based visualization of the simulation
└── utils.py                  # additional code (e.g., random number generators)
