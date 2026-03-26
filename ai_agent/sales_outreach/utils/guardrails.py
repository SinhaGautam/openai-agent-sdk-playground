import re


async def guardrail_against_name(input_text: str, _context):
    text = input_text.lower()

    blocked_patterns = [
        r"what is your name",
        r"who are you",
        r"reveal system prompt",
        r"ignore previous instructions",
    ]

    for pattern in blocked_patterns:
        if re.search(pattern, text):
            raise ValueError(
                "Request blocked by safety guardrail."
            )

    return input_text
