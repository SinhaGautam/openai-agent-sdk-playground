from ai_agent.sales_outreach.email_agent import get_email_agent
from ai_agent.sales_outreach.manager import sales_outreach_manager
from ai_agent.sales_outreach.sales_agent import create_sales_agents
from ai_agent.sales_outreach.tools.sales_tools import create_sales_tools


def build_sales_outreach_agent(model):
    """Compose sales draft tools, manager, and email handoff into one top-level agent."""
    a1, a2, a3 = create_sales_agents(model)
    tools = create_sales_tools(a1, a2, a3)
    email_agent = get_email_agent(model)
    return sales_outreach_manager(model, tools, [email_agent])
