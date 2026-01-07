"""
Model definition for the Schelling's Model of Segregation
"""

import math
from typing import Optional

from mesa import Model  # type: ignore
from mesa.discrete_space import OrthogonalMooreGrid  # type: ignore

from schelling_agents import SchellingAgent, SchellingAgentType


class SchellingModel(Model):
    """
    Schelling's Segregation Model

    A model simulating segregation over time given relatively small individual
    preferences
    """

    description = (
        "A model simulating segregation over time given relatively "
        "small individual preferences"
    )

    def __init__(
        self,
        width: int = 20,
        height: int = 20,
        agent_count: int = 50,
        desired_simmilar_proportion: float = 0.2,
        seed: Optional[int] = None,
    ):
        """
        Create a new Schelling's Segregation Model

        Parameters
        ----------
        width,heigth : int, default=20
            Width and height of the grid the simulation will occur on
        agent_count : int, default = 50
            Number of agents to simulate
        desired_simmilar_proportion : float, default=0.2
            Desired proportion of simmilar neighbors for the Schelling Agents
        """
        super().__init__(seed=seed)

        # Model Params
        self.height = height
        self.width = width

        # Create a Grid (Moore grid, each cell connected to neighbors
        # including diagonals)
        self.grid = OrthogonalMooreGrid(
            dimensions=[self.width, self.height],
            torus=True,
            capacity=math.inf,
            random=self.random,
        )

        # Create agents
        blue_cells = agent_count // 2
        red_cells = agent_count - blue_cells
        SchellingAgent.create_agents(
            self,
            blue_cells,
            type=SchellingAgentType.BLUE,
            desired_proportion=desired_simmilar_proportion,
            cell=self.random.sample(self.grid.empties.cells, k=blue_cells),
        )
        SchellingAgent.create_agents(
            self,
            red_cells,
            type=SchellingAgentType.RED,
            desired_proportion=desired_simmilar_proportion,
            cell=self.random.sample(self.grid.empties.cells, k=red_cells),
        )

    def step(self):
        """
        Execute a single step of the Model
        """
        # Step each agents in a random order
        self.agents.shuffle_do("step")
