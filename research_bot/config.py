"""
Configuration module for Research Bot.

Manages environment variables and settings for the research bot framework.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class ResearchBotConfig:
    """Configuration settings for Research Bot."""
    
    # API Keys
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    
    # Model settings
    planner_model: str = os.getenv("PLANNER_MODEL", "llama-3.3-70b-versatile")
    writer_model: str = os.getenv("WRITER_MODEL", "llama-3.3-70b-versatile")
    search_model: str = os.getenv("SEARCH_MODEL", "llama-3.3-70b-versatile")
    
    # Search settings
    max_searches: int = int(os.getenv("MAX_SEARCHES", "20"))
    max_concurrent_searches: int = int(os.getenv("MAX_CONCURRENT_SEARCHES", "5"))
    search_timeout: int = int(os.getenv("SEARCH_TIMEOUT", "30"))
    
    # Report settings
    report_max_length: int = int(os.getenv("REPORT_MAX_LENGTH", "10"))  # pages
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    enable_tracing: bool = os.getenv("ENABLE_TRACING", "true").lower() == "true"
    
    def validate(self) -> bool:
        """Validate required configuration."""
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")
        return True


# Global config instance
config = ResearchBotConfig()
