from agents import Agent


def optimizer_agent(model):
    return Agent(
        name="Optimizer",
        instructions="""
Improve the report using evaluator feedback.

Input you receive:
- the original report markdown
- evaluator feedback (score and notes)

Output requirements:
- Return ONLY the improved markdown report (no JSON, no preamble, no commentary).
- Preserve the overall structure and headings.
- Do NOT introduce new factual claims that are not supported by the provided summaries.
- Keep length roughly the same (>= 1000 words).
""",
        model=model,
    )