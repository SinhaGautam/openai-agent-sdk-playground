from agents import Agent
from pydantic import BaseModel, Field

class PlanResearchInput(BaseModel):
    query: str
    
class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")


INSTRUCTIONS = """
You are an expert research planner.

Given a user query, generate a high-quality plan of web searches
that would best answer the question.

Output ONLY a structured plan containing a list of searches.

Requirements:

- Provide 3 to 5 search queries
- Each query must explore a different angle of the topic
  (background, key ideas, data/statistics, recent developments, expert views)
- Avoid duplicate or very similar queries
- Write concise, effective search phrases
- Do not include explanations outside the structured output

Focus on producing queries that together would give a complete answer.
"""


def planner_agent(model):
    return Agent(
        name="AutonomousPlanner",
        instructions=INSTRUCTIONS,
        model=model,
        output_type=WebSearchPlan,
    )