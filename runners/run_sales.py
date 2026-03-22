from agents import Runner, trace

from ai_agent.sales_outreach.builder import build_sales_outreach_agent
from models.factory import get_model


async def run():
    model = get_model()
    agent = build_sales_outreach_agent(model)

    message = "Send out a cold sales email addressed to Dear CEO from Alice"

    with trace("Automated SDR"):
        result = await Runner.run(agent, message)

    print(result.final_output)
