

### Implementing a Prey - Predator simulation with Mesa


The objective of this practical work is to implement a simulation of a Prey - Predator model. The Prey - Predator model is a simple ecological model, consisting of three agent types: *wolves*, *sheep*, and *grass*. The wolves and the sheep wander around the grid at random. Wolves and sheep both expend energy moving around, and replenish it by eating. Sheep eat grass, and wolves eat sheep if they end up on the same grid cell.

If wolves and sheep have enough energy, they reproduce, creating a new wolf or sheep (in this simplified model, only one parent is needed for reproduction). The grass on each cell regrows at a constant rate. If any wolves and sheep run out of energy, they die.

The implementation of this model will make you use several Mesa concepts and features:

- MultiGrid.
- Multiple agent types (wolves, sheep, grass).
- Overlay arbitrary text (wolf’s energy) on agent’s shapes while drawing on CanvasGrid.
- Agents inheriting a behavior (random movement) from an abstract parent
- Writing a model composed of multiple files.
- Dynamically adding and removing agents from the schedule.

The goal is to implement a Prey - Predator model closely based on the NetLogo Wolf-Sheep Predation Model: Wilensky, U. (1997). NetLogo Wolf Sheep Predation model. http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation


Download the archive which contains the project from which to start and extract it. The extracted folder contains 6 python files:

- prey_predator/random_walker.py: this defines the RandomWalker agent, which implements the behavior of moving randomly across a grid, one cell at a time. Both the Wolf and Sheep agents will inherit from it.

- prey_predator/agents.py: defines the Wolf, Sheep, and GrassPatch agent classes.

- prey_predator/schedule.py: defines a custom variant on the RandomActivation scheduler, where all agents of one class are activated (in random order) before the next class goes – e.g. all the wolves go, then all the sheep, then all the grass.

- prey_predator/model.py: defines the Prey - Predator model itself.

- prey_predator/server.py: sets up the interactive visualization server
run.py: launches a model visualization server.


So, now it’s up to you to work and implement the Prey - Predator model:

1. Defines the Wolf, Sheep, and GrassPatch agent classes in the prey_predator/agents.py file.
 - A sheep that walks around, reproduces (asexually) and gets eaten.
 - A wolf that walks around, reproduces (asexually) and eats sheep.
 - A patch of grass that grows at a fixed rate and it is eaten by sheep.
2. Defines the Prey - Predator model by completing the prey_predator/model.py file.
3. Sets up the interactive visualization server by completing prey_predator/server.py file.

 - Display the different agents on the grid.
 - Added buttons to control the initial settings.
4. Tune the initial parameters to find a balanced state in the model: none of the species disappears during the simulation. The output graph should be like that:
