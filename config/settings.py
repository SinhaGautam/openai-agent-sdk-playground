import os
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama")

# Ollama settings
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434/v1"
)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

# OpenAI settings
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# SendGrid (sales email demo)
SENDGRID_FROM_EMAIL = os.getenv("SENDGRID_FROM_EMAIL")
SENDGRID_TO_EMAIL = os.getenv("SENDGRID_TO_EMAIL")