# Coding project
Repository for the coding project in the Advanced scientific programming with Python course 2025.

# Project Description
The idea of my project is to create a simulation of an ecosystem, in which different species (classes of objects) live and compete for resources.
First, the user has to specify the size of the ecosystem (grid), the number of objects to be created for each species and how many simulation rounds the user wants to run. 
Each species is associated with numerical values for different traits; size, speed, energy(food) requirements, mutation rate and mating rate. 

The values for the traits sums up to an energy value. The initial energy value is equal for all species. 
The energy value for the objects will be increased or decreased based on how well the object performs in the resource-competition.
If the energy value reaches 0 the object will die (be removed from the ecosystem). 

The resources will be: food and partner availability. 
(There will be food available for all species. Some species can also consume other species as food.)

Mutations are modelled by slight changes in the trait values for each new generation.
The simulation runs in cycles where species interact, reproduce, and evolve. 

The visualization of the simulation is text-based. This allow the user to follow the ecosystem’s health and track the evolution of species as the simulation progresses.

Files in the simulation include:

main.py                   # entry point for the simulation, runs the simulation loop

ecosystem.py              # the ecosystem class with simulation logic including the movement of objects and reproduction logics
grid.py                   # initiates the grid, the visual representation of the ecosystem. Populates the grid with the user-given number of each animal class at random locations. Adds food items to 1/3 of the empty cells. (Unfortunately I didnt have time to finish the food consumption logics though).
carnivores.py             # animals able to consume herbivores and thereby increase their energy (unfortunately I didnt have time to finish the predator/prey interactions though)
herbivores.py             # animals intended to consume the food added to the grid, can be consumed by the carnivores (unfortunately I didnt have time to finish the predator/prey interactions though)

eagle.py                 #contains the classes for each species
lion.py
fox.py 

zebra.py
gazelle.py
rabbit.py

animals.py              # initiates the animals class and defines functions for movement and reproduction
