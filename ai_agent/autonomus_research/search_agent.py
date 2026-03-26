from agents import Agent, ModelSettings
from ai_agent.autonomus_research.tools.websearch_tool import web_search

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise, report-ready summary of the results.\n"
    "\n"
    "Input handling:\n"
    "- The input may include prefixes like 'Search term:' and/or 'Reason for searching:'. Extract only the actual search term.\n"
    "\n"
    "Output rules:\n"
    "- Output 200-250 words total.\n"
    "- No extra commentary beyond the summary.\n"
    "- Use plain text labeled sections to help the writer:\n"
    "  - `MainFindings:` (what the best sources agree on)\n"
    "  - `KeyFacts:` (important details, definitions, or qualitative conclusions)\n"
    "  - `KeyNumbers:` (any stats/figures; if none, write 'N/A')\n"
    "  - `DisagreementsOrCaveats:` (uncertainties, disagreements, limitations)\n"
    "\n"
    "Write succinctly with minimal grammar; capture the essence."
)

def search_agent(model):
    return Agent(
        name="Search agent",
        instructions=INSTRUCTIONS,
        tools=[web_search],
        model=model,
        model_settings=ModelSettings(tool_choice="required"),
    )