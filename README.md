# Research Agent

**AI-powered research automation using Groq's fast LLMs** to plan searches, gather information, and generate comprehensive reports. **100% free - no credit card required!**

## Features

- **🚀 Groq-Powered**: Uses Groq API with free tier (30 req/min)
- **💡 Intelligent Planning**: AI strategist proposes comprehensive search queries
- **⚡ Fast Inference**: Groq's optimized LLMs for quick responses
- **📊 Smart Reporting**: Combines research into structured, well-formatted reports
- **🔄 Async Architecture**: Non-blocking concurrent operations for performance
- **⚙️ Configurable**: Environment-based configuration for flexible deployment

## Quick Start

```bash
# 1. Get Groq API key (free): https://console.groq.com/keys
# 2. Clone repo
git clone https://github.com/trulydeeprogrmr29/ResearchAgent.git
cd ResearchAgent

# 3. Setup
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

# 4. Configure
cp .env.example .env
# Edit .env and add your Groq API key

# 5. Run!
python main.py "What are benefits of artificial intelligence?"
```

## Project Structure

```
research_bot/
├── __init__.py              # Package initialization
├── config.py                # Configuration management
├── groq_manager.py          # Groq-based research orchestration
└── agents/
    ├── planner_agent.py     # Search planning agent
    ├── search_agent.py      # Search execution agent
    └── writer_agent.py      # Report writing agent

main.py                       # Application entry point
requirements.txt              # Python dependencies
.env.example                  # Example configuration
README.md                     # This file
GROQ_SETUP.md                 # Detailed Groq setup guide
```

## Configuration

### Environment Variables

**Required:**
- `GROQ_API_KEY`: Your Groq API key from https://console.groq.com/keys

**Optional:**
```env
# LLM Models (default: llama-3.3-70b-versatile)
PLANNER_MODEL=llama-3.3-70b-versatile
WRITER_MODEL=llama-3.3-70b-versatile
SEARCH_MODEL=llama-3.3-70b-versatile

# Search Configuration
MAX_SEARCHES=20
MAX_CONCURRENT_SEARCHES=5
SEARCH_TIMEOUT=30

# Report Configuration
REPORT_MAX_LENGTH=10

# Logging
LOG_LEVEL=INFO
ENABLE_TRACING=false
```

See `.env.example` for complete options.

## Usage

### Basic Usage

```bash
python main.py "Your research question"
```

### Examples

```bash
# Research latest AI trends
python main.py "What are the latest AI breakthroughs?"

# Verbose output for debugging
python main.py "Machine learning trends" --verbose

# Alternative syntax
python main.py --query "Climate change solutions"
```

### Output

The agent will:
1. **Plan**: Generate 5-10 relevant search queries
2. **Research**: Execute searches concurrently
3. **Summarize**: Extract key findings from each search
4. **Report**: Generate comprehensive markdown report with:
   - Executive summary
   - Full structured report
   - Follow-up questions

## How It Works

### Research Pipeline

```
Query
  ↓
[PlannerAgent] → Generate search plan (5-10 queries)
  ↓
[SearchAgent] → Execute searches in parallel
  ↓
[WriterAgent] → Combine findings into comprehensive report
  ↓
Output: Markdown Report
```

### Agents

**PlannerAgent**
- Analyzes your query
- Proposes 5-10 targeted searches
- Returns: List with search terms and rationale

**SearchAgent**
- Executes searches (simulated with LLM knowledge)
- Summarizes findings
- Returns: Markdown bullet points (≤300 words)

**WriterAgent**
- Combines all search summaries
- Creates structured report
- Generates follow-up questions
- Returns: Final markdown report

## Available Groq Models

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| `llama-3.3-70b-versatile` | ⚡⚡ Fast | Excellent | **Recommended** |
| `llama-3.1-8b-instant` | ⚡⚡⚡⚡ Very Fast | Good | Quick queries |
| `qwen/qwen3-32b` | ⚡⚡⚡ Medium | Good | Alternative |

## Troubleshooting

**"Invalid API Key" Error**
- Verify key from https://console.groq.com/keys
- Ensure `.env` file has key without quotes: `GROQ_API_KEY=gsk_...`

**"Rate limit exceeded"**
- Groq free tier: 30 requests/minute
- Reduce `MAX_SEARCHES` in `.env`
- Reduce `MAX_CONCURRENT_SEARCHES` in `.env`

**"Model decommissioned"**
- Update to available models: `llama-3.3-70b-versatile` (recommended)
- Check all available models: https://console.groq.com/docs/models

**Installation Issues**
```bash
# Verify Python 3.8+
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## Why Groq?

✅ **Free** - No credit card required  
✅ **Fast** - 10+ tokens/second inference  
✅ **Generous Rate Limits** - 30 requests/min free tier  
✅ **Open Models** - LLaMA 3.3, Mixtral, Qwen  
✅ **No Lock-in** - Use open-source models  

## Development

### Debug Mode
```bash
python main.py "Your query" --verbose
```

Enables DEBUG logging and full error stack traces.

### Adding Custom Features

Extend `research_bot/` with new agents or managers following the existing pattern.

## License

Specify your license here.

## Contributing

Contributions welcome! Please follow project conventions.
