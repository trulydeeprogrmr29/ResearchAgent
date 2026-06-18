"""Search Agent - Executes web searches and summarizes results."""

from dotenv import load_dotenv

load_dotenv()

try:
    from agents import Agent, WebSearchTool
    from agents.model_settings import ModelSettings
except ImportError:
    # Stubs for development
    class Agent:
        def __init__(self, name, instructions, tools=None, model_settings=None):
            self.name = name
            self.instructions = instructions
            self.tools = tools or []
            self.model_settings = model_settings
    
    class WebSearchTool:
        pass
    
    class ModelSettings:
        def __init__(self, tool_choice=None):
            self.tool_choice = tool_choice

search_agent = Agent(
    name="SearchAgent",
    instructions=(
        "You are an internet researcher. Use the WebSearch tool to gather the "
        "most relevant information for the given query. Summarize your findings "
        "in clear, markdown bullets (≤300 words)."
    ),
    tools=[WebSearchTool()],
    # force the model to choose the tool; no stray text-only answers
    model_settings=ModelSettings(tool_choice="required"),
)