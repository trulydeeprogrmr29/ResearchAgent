"""Writer Agent - Generates comprehensive research reports."""

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

class ReportData(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: list[str]

writer_agent = Agent(
    name="WriterAgent",
    instructions=(
        "You are a senior analyst. Combine the provided research summaries "
        "into a coherent, well-structured report (5-10 pages of markdown). "
        "Begin with a one-paragraph executive summary, then the full report, "
        "and end with 3-5 thoughtful follow-up questions."
    ),
    model="mixtral-8x7b-32768",
    output_type=ReportData,
)