from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from config.settings import OPENAI_MODEL


def get_openai_model():
    client = AsyncOpenAI()  # uses OPENAI_API_KEY env

    return OpenAIChatCompletionsModel(
        model=OPENAI_MODEL,
        openai_client=client
    )