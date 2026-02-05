# ResearchAgent (OpenAI Agents SDK + Heroku)

A deployable research assistant built with the OpenAI Agents SDK and Flask.

## What this app does

- Exposes a simple HTTP API for research tasks.
- Uses the OpenAI Agents SDK to run a `ResearchAgent` with web search.
- Ready for deployment to Heroku.

## Project structure

- `app.py` – Flask application and API routes.
- `research_agent.py` – OpenAI agent definition and execution helper.
- `requirements.txt` – Python dependencies.
- `Procfile` – Heroku process definition.
- `runtime.txt` – Python runtime pin for Heroku.
- `.env.example` – required environment variables.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set your API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Run locally:

```bash
python app.py
```

Test request:

```bash
curl -X POST http://127.0.0.1:5000/research \
  -H "Content-Type: application/json" \
  -d '{"query":"Summarize the latest progress in reusable rockets"}'
```

## Heroku deployment

1. Create app and set stack/runtime as needed.
2. Set config vars:

```bash
heroku config:set OPENAI_API_KEY="your_api_key_here"
```

3. Deploy:

```bash
git push heroku main
```

The `Procfile` runs Gunicorn with `app:app`.

## API

### `GET /health`
Returns service health.

### `POST /research`

Request body:

```json
{
  "query": "Your research question"
}
```

Response body:

```json
{
  "query": "Your research question",
  "answer": "Agent answer"
}
```
