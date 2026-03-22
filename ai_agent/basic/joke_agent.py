from agents import Agent


def create_joke_agent(model):
    return Agent(
        name="Jokester",
        instructions="You are a professional comedian AI.",
        model=model
    )