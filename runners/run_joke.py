from agents import Runner, trace

from ai_agent.basic.joke_agent import create_joke_agent
from models.factory import get_model


async def run():
    model = get_model()
    agent = create_joke_agent(model)

    with trace("Joke Agent Run"):
        result = await Runner.run(
            agent,
            "Tell a joke about AI agents",
        )

    print(result.final_output)
