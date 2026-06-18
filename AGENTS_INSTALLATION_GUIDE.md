# Installing the 'agents' Module

## Current Status

Your Research Agent is now **working** with stub implementations. The warning message you see is expected:
```
WARNING:root:'agents' module not found. Using stub implementation.
```

This allows the application to run without the actual agents library, but it won't perform real research.

## To Enable Real Research

You need to install the `agents` module. This appears to be a custom agents framework. Here are options:

### Option 1: If it's a private package

If you have a private agents package, install it from:

```bash
# From local directory
pip install /path/to/agents

# From git repository
pip install git+https://github.com/your-org/agents.git

# From PyPI (if available)
pip install agents
```

### Option 2: If you need to install a specific version

Check if there's a specific agents library you should use:

```bash
# Search PyPI
pip search agents

# Install from PyPI if found
pip install agents==<version>
```

### Option 3: Add to requirements.txt

If you find the correct package, update `requirements.txt`:

```
agents>=1.0.0
# or
agents @ git+https://github.com/your-org/agents.git
```

Then install:
```bash
pip install -r requirements.txt
```

## What the agents Module Provides

Based on your code, the agents module should provide:

1. **Agent class** - For creating AI agents
   ```python
   from agents import Agent
   
   agent = Agent(
       name="MyAgent",
       instructions="Do something",
       model="gpt-4o"
   )
   ```

2. **Runner class** - For executing agents
   ```python
   from agents import Runner
   
   result = await Runner.run(agent, prompt)
   ```

3. **WebSearchTool** - For web search capability
   ```python
   from agents import WebSearchTool
   
   search_tool = WebSearchTool()
   ```

4. **ModelSettings** - For configuring model behavior
   ```python
   from agents.model_settings import ModelSettings
   
   settings = ModelSettings(tool_choice="required")
   ```

## Checking if agents is Installed

```bash
# Try importing
python -c "from agents import Agent, Runner; print('agents module found!')"

# If not found, you'll see:
# ModuleNotFoundError: No module named 'agents'
```

## Once You Install agents

1. The warning will disappear automatically
2. Your agents will use real AI models
3. Web searches will execute properly
4. Reports will be generated with actual research data

## Troubleshooting

**Still getting ModuleNotFoundError?**
1. Ensure you're using the correct virtual environment: `which python` or `where python`
2. Verify installation: `pip list | grep agents`
3. Reinstall: `pip uninstall agents && pip install agents`

**Not sure what agents package to use?**
- Check your project documentation
- Look for setup.md or INSTALL.md files
- Check with your team/project maintainer
- Look at git history for clues: `git log --all --oneline | grep -i agent`

## Testing Installation

Once installed, test with:
```bash
python main.py "What is artificial intelligence?" --verbose
```

You should see actual research results instead of the stub message.
