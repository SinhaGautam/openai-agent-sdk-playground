import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool
from config.settings import SENDGRID_FROM_EMAIL, SENDGRID_TO_EMAIL


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email(SENDGRID_FROM_EMAIL) 
    to_email = To(SENDGRID_TO_EMAIL) 
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response", response.status_code)
    return "success"


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report in markdown format.

Your job:
1. Generate a clear, compelling email subject line based on the report topic.
2. Convert the provided markdown report into clean, well-presented HTML (basic semantic tags only).
3. Call `send_email(subject, html_body)` exactly once to send the email via SendGrid.

HTML rules:
- Use a simple layout with a top title, headings, paragraphs, and lists.
- Keep HTML safe and minimal (no scripts).
- If the markdown contains URLs, preserve them as clickable links.

Final output rules:
- After sending, return the input markdown report verbatim and unchanged.
"""

def email_agent(model):
    return Agent(
        name="Email agent",
        instructions=INSTRUCTIONS,
        tools=[send_email],
        model=model,
    )
