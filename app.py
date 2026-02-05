import asyncio
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from research_agent import run_research

load_dotenv()

app = Flask(__name__)


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/health")
def health() -> tuple:
    has_key = bool(os.getenv("OPENAI_API_KEY"))
    return jsonify({"status": "ok", "openai_configured": has_key}), 200


@app.post("/research")
def research() -> tuple:
    payload = request.get_json(silent=True) or {}
    query = payload.get("query", "").strip()

    if not query:
        return jsonify({"error": "Missing required field: query"}), 400

    try:
        answer = asyncio.run(run_research(query))
        return jsonify({"query": query, "answer": answer}), 200
    except Exception as exc:
        return jsonify({"error": "Research request failed", "details": str(exc)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
