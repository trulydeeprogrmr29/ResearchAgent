# Using Groq with Research Agent

## Why Groq?
- ✅ **Free API** - No credit card required
- ✅ **Generous rate limits** - 30 requests/minute
- ✅ **Fast inference** - Optimized LLM performance
- ✅ **Open models** - LLaMA, Mixtral (no proprietary lock-in)

## Setup

### 1. Get Your Groq API Key
1. Go to https://console.groq.com/keys
2. Sign up (free, takes 2 minutes)
3. Create an API key
4. Copy it

### 2. Update .env
Edit `.env` and replace:
```
GROQ_API_KEY=your_actual_key_here
```

### 3. Run the Research Agent
```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Run research
python main.py "What is artificial intelligence?"
```

## Models Available on Groq

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| `mixtral-8x7b-32768` | ⚡⚡⚡ Very Fast | Good | Recommended (default) |
| `llama-3-70b-8192` | ⚡⚡ Fast | Better | Complex tasks |
| `llama-3-8b-8192` | ⚡⚡⚡⚡ Fastest | Fair | Simple queries |

## Configuration

Edit `.env` to customize:

```
# Change model (if desired)
PLANNER_MODEL=mixtral-8x7b-32768
WRITER_MODEL=mixtral-8x7b-32768
SEARCH_MODEL=mixtral-8x7b-32768

# Rate limiting
MAX_SEARCHES=20
MAX_CONCURRENT_SEARCHES=5
SEARCH_TIMEOUT=30

# Report length
REPORT_MAX_LENGTH=10
```

## Rate Limits

Groq free tier: **30 requests/minute** per API key

Your agent may take longer if it hits the rate limit. To speed up:
1. Reduce `MAX_SEARCHES` in `.env`
2. Reduce `MAX_CONCURRENT_SEARCHES` in `.env`

## Testing

Quick test:
```powershell
python -c "from groq import Groq; c = Groq(api_key='YOUR_KEY'); print('✓ Groq working!')"
```

## Troubleshooting

**Error: "Invalid API key"**
- Check you copied the key correctly from https://console.groq.com/keys
- Ensure `.env` doesn't have quotes: `GROQ_API_KEY=sk-...` (not `"sk-..."`)

**Error: "Rate limit exceeded"**
- Reduce concurrent searches in `.env`
- Wait a minute and try again

**Still having issues?**
- Verify Groq key: `groq.console.com/keys`
- Check `.env` format
- Run with `--verbose` flag for debug output
