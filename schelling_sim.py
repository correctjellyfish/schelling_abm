"""
Run the Schelling Model
"""

from typing import cast

from mesa.visualization import SolaraViz, SpaceRenderer  # type: ignore
from mesa.visualization.components import AgentPortrayalStyle  # type: ignore

from schelling_model import SchellingModel, SchellingAgent, SchellingAgentType

AGENT_SIZE = 20
GRID_SIZE = (50, 50)
AGENT_START_COUNT = int(0.75 * (GRID_SIZE[0] * GRID_SIZE[1]))


def agent_portrayal(agent: SchellingAgent) -> AgentPortrayalStyle:
    match agent.type:
        case SchellingAgentType.BLUE:
            return AgentPortrayalStyle(color="tab:blue", size=AGENT_SIZE)
        case SchellingAgentType.RED:
            return AgentPortrayalStyle(color="tab:red", size=AGENT_SIZE)
        case _:
            return AgentPortrayalStyle(color="tab:green", size=AGENT_SIZE)


model_parameters = {
    "agent_count": {
        "type": "SliderInt",
        "value": AGENT_START_COUNT,
        "label": "Number of agents:",
        "min": 2,
        "max": (GRID_SIZE[0] * GRID_SIZE[1] - 1),
        "step": 1,
    },
    "desired_simmilar_proportion": {
        "type": "SliderFloat",
        "value": 0.2,
        "label": "Simmilar Proportion:",
        "min": 0.01,
        "max": 1.0,
        "step": 0.01,
    },
    "width": GRID_SIZE[0],
    "height": GRID_SIZE[1],
}


if __name__ == "__main__":
    schelling_model = SchellingModel(
        width=cast(int, model_parameters["width"]),
        height=cast(int, model_parameters["height"]),
        agent_count=cast(
            int, cast(dict, model_parameters["agent_count"])["value"]
        ),
        desired_simmilar_proportion=cast(
            float,
            cast(dict, model_parameters["desired_simmilar_proportion"])[
                "value"
            ],
        ),
    )

    renderer = SpaceRenderer(
        model=schelling_model, backend="matplotlib"
    ).render(agent_portrayal=agent_portrayal)

    page = SolaraViz(
        model=schelling_model,
        renderer=renderer,
        components=[],
        model_params=model_parameters,
        name="Schelling's Segregation Model",
    )

    page
