import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Try to import Groq, provide stub if not available
try:
    from groq import Groq
except ImportError:
    logging.warning("'groq' module not found. Using stub implementation.")
    class Groq:
        def __init__(self, api_key=None):
            self.api_key = api_key

# Try to import agents, provide stub if not available
try:
    from agents import Runner
except ImportError:
    logging.warning("'agents' module not found. Using stub implementation.")
    class Runner:
        @staticmethod
        async def run(agent, prompt):
            """Stub implementation for development."""
            return StubResult()
    
    class StubResult:
        def __init__(self):
            self.final_output = StubOutput()
    
    class StubOutput:
        def __init__(self):
            self.searches = []
            self.markdown_report = "# Research Report\n\nNo real searches performed - agents module not installed."

try:
    from tracing import trace, gen_trace_id
except ImportError:
    # Fallback if tracing module not available
    def trace(name, trace_id=None):
        return TraceContext()
    
    def gen_trace_id():
        import uuid
        return str(uuid.uuid4())
    
    class TraceContext:
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

from .agents import planner_agent, search_agent, writer_agent
from .config import config

logger = logging.getLogger(__name__)

class ResearchManager:
    def __init__(self):
        self.groq_client = Groq(api_key=config.groq_api_key)
    
    async def run(self, query: str) -> None:
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            plan    = await self._plan_searches(query)
            results = await self._perform_searches(plan)
            report  = await self._write_report(query, results)
            print(report.markdown_report)

    async def _plan_searches(self, query: str):
        result = await Runner.run(planner_agent, f"Query: {query}")
        return result.final_output.searches

    async def _perform_searches(self, searches):
        tasks = [asyncio.create_task(self._search(item)) for item in searches]
        return [await t for t in asyncio.as_completed(tasks)]

    async def _search(self, item):
        res = await Runner.run(search_agent, item.query)
        return res.final_output

    async def _write_report(self, query: str, summaries):
        joined = "\n".join(summaries)
        output = await Runner.run(writer_agent,
            f"Original query: {query}\nResearch:\n{joined}"
        )
        return output.final_output