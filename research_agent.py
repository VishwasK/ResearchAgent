import os

from agents import Agent, Runner, WebSearchTool

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

research_agent = Agent(
    name="ResearchAgent",
    model=MODEL_NAME,
    instructions=(
        "You are a rigorous research assistant. "
        "Provide concise, structured findings with key points, assumptions, and caveats. "
        "When using web search, synthesize and avoid speculation."
    ),
    tools=[WebSearchTool()],
)


async def run_research(query: str) -> str:
    result = await Runner.run(research_agent, query)
    return result.final_output
