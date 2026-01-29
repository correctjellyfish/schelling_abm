# Schelling's Segregation Model

## Background

A microeconomic agent based model showing that even with "mild" in group preferences
significant segregation can still occur. Developed by Thomas Schelling in
[Dynamic models of segregation](https://doi.org/10.1080/0022250X.1971.9989794),
the model consists of two types of agents (in this implementation red and blue)
which are able to move on a grid of cells.

## Rules

1. Only one agent can occupy a cell at a time
1. If the proportion of neighbors of the same agent type is below an
   agents similarity threshold, the agent will move to a random empty cell
   (anywhere on the grid)

## Usage

Clone this repository, and then use pixi to set up a virtual environment
to run the simulation.

You can install pixi following the directions on their [install page](https://pixi.prefix.dev/dev/installation/),
then in the directory the repository was cloned into run

```{bash}
pixi run simulation
```

which should serve the simulation at [http://localhost:8765/](http://localhost:8765/).

## References

- [Wikipedia page about Schelling's Model of Segregation](https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation)
- [Dynamic models of segregation by Thomas Schelling](https://doi.org/10.1080/0022250X.1971.9989794)
