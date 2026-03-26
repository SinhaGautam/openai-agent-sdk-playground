from ai_agent.autonomus_research.autonomous_planner_agent import planner_agent
from ai_agent.autonomus_research.search_agent import search_agent
from ai_agent.autonomus_research.report_agent import report_agent
from ai_agent.autonomus_research.evaluator_agent import evaluator_agent
from ai_agent.autonomus_research.optimizer_agent import optimizer_agent
from ai_agent.autonomus_research.email_agent import email_agent

from ai_agent.autonomus_research.tools.research_tools import create_research_tools
from ai_agent.autonomus_research.autonomous_research_manager import autonomous_research_agent


def build_autonomous_research_agent(model):

    # Specialist agents
    planner = planner_agent(model)
    search = search_agent(model)
    evaluator = evaluator_agent(model)
    optimizer = optimizer_agent(model)

    writer = report_agent(model)
    email = email_agent(model)

    tools = create_research_tools(
        planner,
        search,
        writer,
        evaluator,
        optimizer,
    )

    handoffs = [email]

    # Top-level agent
    return autonomous_research_agent(
        model,
        tools,
        handoffs,
    )