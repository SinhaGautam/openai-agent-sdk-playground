from typing import List
from agents import function_tool
from ddgs import DDGS

# =========================
# Core Search Logic
# =========================

def _duckduckgo_search(
    query: str,
    max_results: int = 5,
) -> List[dict]:
    """
    Perform DuckDuckGo search and return raw results.
    """
    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results,
        )

        for r in search_results:
            results.append(
                {
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "href": r.get("href", ""),
                }
            )

    return results


# =========================
# Formatting for LLM
# =========================

def _format_results(results: List[dict]) -> str:
    """
    Convert search results into LLM-friendly text.
    """
    if not results:
        return "No relevant results found."

    formatted = []

    for i, r in enumerate(results, start=1):
        formatted.append(
            f"""
Result {i}
Title: {r['title']}
Summary: {r['body']}
URL: {r['href']}
""".strip()
        )

    return "\n\n".join(formatted)


# =========================
# Agent Tool (Public)
# =========================

@function_tool
def web_search(
    query: str,
    max_results: int = 5,
) -> str:
    """
    Search the web using DuckDuckGo.

    Use this tool when you need up-to-date information
    from the internet.

    Args:
        query: Search query
        max_results: Number of results (default 5)

    Returns:
        LLM-friendly formatted search results
    """

    if not query or not query.strip():
        return "Error: Empty search query."

    try:
        raw_results = _duckduckgo_search(
            query=query,
            max_results=max_results,
        )

        return _format_results(raw_results)

    except Exception as e:
        return f"Web search failed: {str(e)}"