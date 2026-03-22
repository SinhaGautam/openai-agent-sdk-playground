from config.settings import MODEL_PROVIDER
from models.ollama_model import get_ollama_model
from models.openai_model import get_openai_model


def get_model():
    if MODEL_PROVIDER == "ollama":
        return get_ollama_model()

    if MODEL_PROVIDER == "openai":
        return get_openai_model()

    raise ValueError(f"Unsupported MODEL_PROVIDER: {MODEL_PROVIDER}")