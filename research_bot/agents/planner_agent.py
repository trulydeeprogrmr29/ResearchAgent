"""Planner Agent - Plans web searches for research queries."""

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

try:
    from agents import Agent
except ImportError:
    # Stub for development
    class Agent:
        def __init__(self, name, instructions, output_type=None, model=None):
            self.name = name
            self.instructions = instructions
            self.output_type = output_type
            self.model = model


class WebSearchItem(BaseModel):
    reason: str            # why we’re running this search
    query: str             # the exact search term

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]

planner_agent = Agent(
    name="PlannerAgent",
    instructions=(
        "You are a research strategist. Given a question, propose 5-20 web "
        "searches that, together, will answer it comprehensively. "
        "Return them as JSON in the schema provided."
    ),
    model="mixtral-8x7b-32768",
    output_type=WebSearchPlan,
)