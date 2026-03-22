# OpenAI Agents SDK playground

Experiments with the [OpenAI Agents Python SDK](https://github.com/openai/openai-agents-python): small runnable demos that use `agents.Agent`, `Runner`, tracing, handoffs, tools, and optional guardrails.

## Requirements

- Python **3.12+**
- [uv](https://docs.astral.sh/uv/) (recommended) or another PEP 517 installer

## Setup

```bash
cd openai-agent-sdk-playground
uv sync
```

Copy `.env` from your secrets manager or create one with the variables below. The app loads it via `python-dotenv` in `config/settings.py`.

## Environment variables

| Variable | Role | Default |
|----------|------|---------|
| `MODEL_PROVIDER` | `ollama` or `openai` | `ollama` |
| `OLLAMA_BASE_URL` | OpenAI-compatible base URL for Ollama | `http://localhost:11434/v1` |
| `OLLAMA_MODEL` | Model name when using Ollama | `mistral` |
| `OPENAI_MODEL` | Model name when using OpenAI | `gpt-4.1-mini` |
| `OPENAI_API_KEY` | Required when `MODEL_PROVIDER=openai` | — |
| `SENDGRID_API_KEY` | Required for the **sales** demo to send email | — |
| `SENDGRID_FROM_EMAIL` | Verified SendGrid sender | `ed@edwarddonner.com` |
| `SENDGRID_TO_EMAIL` | Recipient for the demo | `ed.donner@gmail.com` |

Override the SendGrid defaults in `.env` for your verified sender and inbox.

## Run

```bash
uv run python main.py joke    # single joke agent, traced run
uv run python main.py sales   # sales manager → draft tools → email handoff
```

Or: `python main.py joke` / `python main.py sales` with the project venv activated.

## Project layout

| Path | Purpose |
|------|---------|
| `main.py` | CLI entry: dispatches to runners |
| `runners/run_joke.py` | Minimal `Runner.run` + `trace` using the joke agent |
| `runners/run_sales.py` | Runs the sales outreach demo (uses `builder`) |
| `ai_agent/basic/joke_agent.py` | Simple `Agent` factory |
| `ai_agent/sales_outreach/` | Sales agents, tools, manager, `builder`, email + SendGrid |
| `ai_agent/sales_outreach/builder.py` | Wires model → draft tools → manager → email handoff |
| `ai_agent/agent.py` | Standalone joke script (same model factory as `main.py`; run with `python -m ai_agent.agent`) |
| `models/` | `get_model()` switches Ollama vs OpenAI chat-completions models |
| `config/settings.py` | Loads `.env` and model / SendGrid settings |
| `utils/guardrails.py` | Input guardrail on the sales manager |

## Sales demo (high level)

1. Three stylistically different sales agents are exposed as tools (`b2b_sales_email`, `startup_sales_email`, `enterprise_sales_email`).
2. The **Sales Manager** agent is instructed to call those tools, pick one draft, and hand off once to the **Email Manager**.
3. The **Email Manager** uses nested tools for subject and HTML conversion, then `send_html_email` via SendGrid.

## Dependencies

See `pyproject.toml`: `openai`, `openai-agents`, `python-dotenv`, `sendgrid`.
