import os
from typing import Dict

import sendgrid
from agents import Agent, function_tool
from sendgrid.helpers.mail import Content, Email, Mail, To

from config.settings import SENDGRID_FROM_EMAIL, SENDGRID_TO_EMAIL

subject_instructions = (
    "You can write a subject for a cold sales email. "
    "You are given a message and you need to write a subject for an email that is likely to get a response."
)

html_instructions = (
    "You can convert a text email body to an HTML email body. "
    "You are given a text email body which might have some markdown "
    "and you need to convert it to an HTML email body with simple, clear, compelling layout and design."
)

instructions = (
    "You are an email formatter and sender. You receive the body of an email to be sent. "
    "You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. "
    "Finally, you use the send_html_email tool to send the email with the subject and HTML body."
)


@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body."""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email(SENDGRID_FROM_EMAIL)
    to_email = To(SENDGRID_TO_EMAIL)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


def get_email_agent(model):
    subject_writer = Agent(
        name="Email subject writer",
        instructions=subject_instructions,
        model=model,
    )
    subject_tool = subject_writer.as_tool(
        tool_name="subject_writer",
        tool_description="Write a subject for a cold sales email",
    )

    html_converter = Agent(
        name="HTML email body converter",
        instructions=html_instructions,
        model=model,
    )
    html_tool = html_converter.as_tool(
        tool_name="html_converter",
        tool_description="Convert a text email body to an HTML email body",
    )

    email_tools = [subject_tool, html_tool, send_html_email]

    return Agent(
        name="Email Manager",
        instructions=instructions,
        tools=email_tools,
        model=model,
        handoff_description="Convert an email to HTML and send it",
    )
