from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL


def get_ollama_model():
    client = AsyncOpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key="ollama"  # any string works
    )

    return OpenAIChatCompletionsModel(
        model=OLLAMA_MODEL,
        openai_client=client
    )