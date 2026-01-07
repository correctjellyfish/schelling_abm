"""
Model definition for the Schelling's Model of Segregation
"""

from mesa import Model, ABMSimulator  # type: ignore

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
        seed=None,
        simulator: ABMSimulator = None,
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

    pass
