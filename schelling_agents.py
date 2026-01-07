"""
Agent definition for the Schelling's model of Segregation
"""

from enum import Enum
from typing import Optional, cast

from mesa import Model  # type: ignore
from mesa.discrete_space import CellAgent, Cell  # type: ignore


class SchellingAgentType(Enum):
    """
    Possible Types of Agents
    """

    RED = 1
    BLUE = 2


class SchellingAgent(CellAgent):
    """
    An agent which moves if a proportion of its neighbors above a threshold are
    of the other agent type
    """

    def __init__(
        self,
        model: Model,
        type: SchellingAgentType,
        desired_proportion: float = 0.2,
        cell: Optional[Cell] = None,
    ):
        """
        Initialize a SchellingAgent

        Parameters
        ----------
        model : Model
            The MESA model which the agent is a part of
        type : SchellingAgentType
            The type of this agent
        desired_proportion : float
            Desired proportion of neighbors to have the same agent type
        cell : Cell
            The MESA cell that the agent is on
        """
        super().__init__(model)  # Pass the model to the CellAgent init
        self.type = type
        self.desired_proportion = desired_proportion
        self.cell = cell

    def neighbor_proportion(self) -> float:
        """
        Get the proportion of neighbors which have the same SchellingAgentType
        as self
        """
        same_count = 0.0
        total_count = 0.0
        if self.cell:  # Make sure we are actually on a cell
            for cell in self.cell.neighborhood:
                assert len(cell.agents) <= 1, (
                    "Error! Cell contains more than single agent!"
                )
                for agent in cell.agents:
                    agent = cast(SchellingAgent, agent)
                    total_count += 1.0
                    if self.type == agent.type:
                        same_count += 1
        return same_count / total_count

    def move(self):
        """
        Move to a random empty cell in the model grid
        """
        # NOTE: The CellAgent class has a Cell property that will
        # handle the cell updating when we set the cell property
        self.cell = self.model.grid.select_random_empty_cell()

    def step(self):
        """
        Check neighborhood proportion, if not enough of same agent type move
        """
        if self.neighbor_proportion() < self.desired_proportion:
            self.move()
