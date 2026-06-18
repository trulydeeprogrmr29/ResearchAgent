# Research Agent

AI-powered research automation using intelligent agents to plan searches, gather information, and generate comprehensive reports.

## Features

- **Intelligent Planning**: AI strategist proposes comprehensive search queries
- **Parallel Research**: Concurrent web searches for faster information gathering
- **Smart Reporting**: Combines research into structured, well-formatted reports
- **Async Architecture**: Non-blocking concurrent operations for performance
- **Configurable**: Environment-based configuration for flexible deployment

## Project Structure

```
research_bot/
├── __init__.py           # Package initialization and exports
├── config.py             # Configuration management
├── manager.py            # ResearchManager orchestration
└── agents/
    ├── __init__.py       # Agents package initialization
    ├── planner_agent.py  # Search planning agent
    ├── search_agent.py   # Web search execution agent
    └── writer_agent.py   # Report writing agent

main.py                    # Application entry point
pyproject.toml             # Project metadata and dependencies
requirements.txt           # Python dependencies
.env                       # Environment variables (local)
.env.example               # Example environment configuration
```

## Installation

1. **Clone the repository**
   ```bash
   cd ResearchAgent
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # OR
   pip install -e .
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key and settings
   ```

## Configuration

### Environment Variables

**Required:**
- `OPENAI_API_KEY`: Your OpenAI API key

**Optional:**
- `PLANNER_MODEL`: Model for search planning (default: gpt-4o)
- `WRITER_MODEL`: Model for report writing (default: o3-mini)
- `SEARCH_MODEL`: Model for search summarization (default: gpt-4o)
- `MAX_SEARCHES`: Maximum searches to plan (default: 20)
- `MAX_CONCURRENT_SEARCHES`: Concurrent search limit (default: 5)
- `SEARCH_TIMEOUT`: Search timeout in seconds (default: 30)
- `REPORT_MAX_LENGTH`: Report length in pages (default: 10)
- `LOG_LEVEL`: Logging level (default: INFO)
- `ENABLE_TRACING`: Enable request tracing (default: true)

## Usage

### Basic Usage

```bash
python main.py "Your research question here"
```

### Examples

```bash
# Simple query
python main.py "What are the latest AI breakthroughs?"

# With verbose output
python main.py "Machine learning trends in 2024" --verbose

# Alternative syntax
python main.py --query "Climate change solutions"
```

### Output

The agent will:
1. Plan relevant web searches for your query
2. Execute searches concurrently
3. Summarize findings from each search
4. Generate a comprehensive report with:
   - Executive summary
   - Full markdown report
   - Follow-up questions

## Module Architecture

### ResearchManager
Orchestrates the research workflow:
- Plans searches using planner_agent
- Executes searches concurrently using search_agent
- Writes final report using writer_agent

### Agents

**PlannerAgent**
- Receives: Research query
- Returns: List of search queries with rationale
- Model: gpt-4o

**SearchAgent**
- Receives: Individual search query
- Returns: Markdown-formatted summary (≤300 words)
- Tools: WebSearchTool
- Model: gpt-4o (with required tool choice)

**WriterAgent**
- Receives: Combined research summaries
- Returns: Structured report with summary, body, and follow-up questions
- Model: o3-mini

### Configuration Module
Manages environment-based settings with validation:
- Loads .env variables
- Provides typed configuration dataclass
- Validates required settings

## Development

### Running Tests
```bash
# Note: Test framework to be added
python -m pytest tests/
```

### Debug Mode
```bash
python main.py "Your query" --verbose
```

Verbose mode enables:
- DEBUG level logging
- Full stack traces on errors
- Detailed request tracing

### Adding Custom Agents

Extend `research_bot/agents/` with new agent modules:

```python
from agents import Agent
from pydantic import BaseModel

class MyOutput(BaseModel):
    result: str

my_agent = Agent(
    name="MyAgent",
    instructions="Your instructions here",
    output_type=MyOutput,
    model="gpt-4o",
)
```

## Troubleshooting

**ModuleNotFoundError: No module named 'agents'**
- Install dependencies: `pip install -r requirements.txt`

**OPENAI_API_KEY not found**
- Ensure .env file exists with valid API key
- Or set environment variable: `export OPENAI_API_KEY=your_key`

**Connection timeout during searches**
- Increase `SEARCH_TIMEOUT` environment variable
- Check internet connection

## API Documentation

See module docstrings for detailed API documentation:
```python
from research_bot import ResearchManager
help(ResearchManager)
```

## License

MIT License

## Contributing

Contributions welcome! Please follow project conventions.
