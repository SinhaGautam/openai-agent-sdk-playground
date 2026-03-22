from agents import Agent

_COMPLAI = (
    "working for ComplAI, a company that provides a SaaS tool for ensuring SOC2 "
    "compliance and preparing for audits, powered by AI."
)

instructions1 = f"You are a sales agent {_COMPLAI} You write professional, serious cold emails."

instructions2 = (
    f"You are a humorous, engaging sales agent {_COMPLAI} "
    "You write witty, engaging cold emails that are likely to get a response."
)

instructions3 = (
    f"You are a busy sales agent {_COMPLAI} You write concise, to-the-point cold emails."
)


def create_sales_agents(model):
    return (
        Agent(
            name="Professional Sales Agent",
            instructions=instructions1,
            model=model,
        ),
        Agent(
            name="Engaging Sales Agent",
            instructions=instructions2,
            model=model,
        ),
        Agent(
            name="Busy Sales Agent",
            instructions=instructions3,
            model=model,
        ),
    )
