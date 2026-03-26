

def create_research_tools(
    planner_agent,
    search_agent,
    writer_agent,
    evaluator_agent,
    optimizer_agent,
):
    tools = []

    tools.append(
        planner_agent.as_tool(
            tool_name="plan_research",
            tool_description="Create a structured research plan. Input should be a research question. Output: {searches[{reason, query}] }.",

        )
    )

    tools.append(
        search_agent.as_tool(
            tool_name="perform_search",
            tool_description="Search the web for the given query string and return a concise summary for report writing. Input must be ONLY the search query (no prefixes like 'Search term:')."

        )
    )

    tools.append(
        writer_agent.as_tool(
            tool_name="write_report",
            tool_description="Generate ReportData (short_summary, markdown_report, follow_up_questions). Input should be a single string containing 'Original query:' and 'Search summaries:'."
        )
    )

    tools.append(
        evaluator_agent.as_tool(
            tool_name="evaluate_report",
            tool_description="Evaluate the quality of a research report. Input: report markdown (and any accompanying short summary, if provided). Output: {score:int, feedback:str}."
        )
    )

    tools.append(
        optimizer_agent.as_tool(
            tool_name="improve_report",
            tool_description="Improve a report using evaluator feedback. Input: original report markdown + evaluator feedback. Output: improved markdown report only."
        )
    )

    return tools