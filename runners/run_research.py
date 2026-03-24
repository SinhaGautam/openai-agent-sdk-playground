import gradio as gr
from dotenv import load_dotenv
from models.factory import get_model
from ai_agent.deep_research.research_manager import ResearchManager

load_dotenv(override=True)

# Create model once


# =========================
# Research Runner (Streaming)
# =========================

async def run_research(query: str):
    model = get_model()
    async for chunk in ResearchManager(model).run( query):
        yield chunk


# =========================
# UI Builder
# =========================

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


# =========================
# Launch App
# =========================

def run():
    ui = create_ui()
    ui.launch(inbrowser=True)