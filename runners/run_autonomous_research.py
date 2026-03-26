from agents import Runner, trace
import gradio as gr
from models.factory import get_model
from ai_agent.autonomus_research.builder import build_autonomous_research_agent


async def run_research(query: str):

    model = get_model()
    agent = build_autonomous_research_agent(model)
    
    yield("Starting research...")

    with trace("Autonomous Research"):
        result = await Runner.run(agent, query)
        yield result.final_output


def create_ui():
    with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
        gr.Markdown("# Deep Research")

        query_textbox = gr.Textbox(
            label="What topic would you like to research?"
        )

        run_button = gr.Button("Run", variant="primary")

        report = gr.Markdown(label="Report")

        # Button click
        run_button.click(
            fn=run_research,
            inputs=query_textbox,
            outputs=report,
        )

        # Enter key submit
        query_textbox.submit(
            fn=run_research,
            inputs=query_textbox,
            outputs=report,
        )

    return ui



def run():
    ui = create_ui()
    ui.launch(inbrowser=True)