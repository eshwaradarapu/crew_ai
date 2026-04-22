# CrewAI Multi-Agent Report Generator

A simple CrewAI project that takes a topic as input and runs a 3-agent workflow:

1. Researcher Agent
2. Writer Agent
3. Reviewer Agent

The output is a research-driven article/report plus a structured review containing:
- score (1-10)
- strengths
- weaknesses
- final_verdict

## Project Structure

- `main.py` - Creates and runs the crew in sequential mode.
- `agents.py` - Defines agents, shared LLM config (Groq), and search tool integration.
- `tasks.py` - Defines research, writing, and review tasks.
- `models.py` - Pydantic schema for reviewer output.
- `requirements.txt` - Python dependencies.

## Prerequisites

- Python 3.10+
- A Groq API key
- A Serper API key

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If activation is blocked on Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Environment Variables (Temporary Session)

Set keys in the same terminal session where you run the app:

```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
$env:SERPER_API_KEY="your_serper_api_key_here"
```

## Run

```powershell
python main.py
```

Then enter a topic when prompted.

## How It Works

1. `research_task` gathers facts and context on `{topic}`.
2. `write_task` uses the research output to write the article/report.
3. `review_task` evaluates quality and returns structured output validated by `ReviewerOutput`.

## LLM + Tool Configuration

- LLM model is configured in `agents.py` using CrewAI `LLM(...)`.
- Current model: `groq/llama-3.3-70b-versatile`
- Research agent has `SerperDevTool()` attached.

## Troubleshooting

- `OPENAI_API_KEY is required`:
  - This means your run is still using OpenAI defaults somewhere. Ensure Groq LLM is configured in `agents.py` and `GROQ_API_KEY` is set in the active terminal.

- `tool_use_failed` or function-call formatting errors:
  - Some model/tool combinations may produce invalid tool-call formatting.
  - Try running again, simplify prompts, or switch to a model with stronger tool-calling reliability.

- `Import "crewai" could not be resolved` in VS Code:
  - Usually an interpreter selection issue. Select the `.venv` Python interpreter in VS Code.

## Notes

- API keys set with `$env:...` are temporary and apply only to the current terminal.
- Reviewer output is typed with Pydantic in `models.py`.
