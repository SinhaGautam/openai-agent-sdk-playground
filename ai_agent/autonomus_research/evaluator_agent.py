from agents import Agent
from pydantic import BaseModel, Field


class Evaluation(BaseModel):
    score: int = Field(description="1-10")
    feedback: str


def evaluator_agent(model):
    return Agent(
        name="Evaluator",
        instructions="""
You are evaluating a research report.

Input you receive:
- the report markdown (and possibly supporting summary fields)

Evaluate for:
- completeness (did it cover the whole query?)
- clarity (can a reader follow the structure?)
- depth (are claims appropriately detailed?)
- accuracy / internal consistency (does it rely on the provided summaries without inventing facts?)

Output requirements (schema handled by the model tooling):
- `score`: integer 1-10
- `feedback`: actionable notes to improve the report (missing sections, unclear claims, contradictions, weak evidence, structural improvements).

Be specific and avoid vague advice.
""",
        model=model,
        output_type=Evaluation,
    )
    