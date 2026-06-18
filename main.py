#!/usr/bin/env python3
"""
Main entry point for the Research Agent application.
"""

import argparse
import asyncio
import logging
import sys

from research_bot.groq_manager import GroqResearchManager
from research_bot.config import config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def run_research(query: str, verbose: bool = False) -> None:
    """Run research on a given query."""
    try:
        logger.info(f"Starting research for query: {query}")
        manager = GroqResearchManager()
        await manager.run(query)
        logger.info("Research completed successfully")
    except Exception as e:
        logger.error(f"Research failed: {e}", exc_info=verbose)
        raise


def main():
    """Main entry point for the Research Agent."""
    parser = argparse.ArgumentParser(
        description='Research Agent - AI-powered research automation (Groq-powered)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --query "Machine Learning trends"
  python main.py --query "Climate change solutions" --verbose
        """
    )
    
    parser.add_argument(
        'query',
        nargs='?',
        help='Research query to process'
    )
    
    parser.add_argument(
        '--query', '-q',
        dest='query_arg',
        help='Research query (alternative syntax)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Determine the query
    query = args.query or args.query_arg
    
    # Set logging level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled")
    
    logger.info("Research Agent started (Groq-powered)")
    
    try:
        # Validate configuration
        config.validate()
        
        if not query:
            print("Welcome to Research Agent (Powered by Groq)!")
            print("Usage: python main.py '<your research query>'")
            print("Example: python main.py 'What are the latest AI breakthroughs?'")
            sys.exit(0)
        
        # Run research asynchronously
        asyncio.run(run_research(query, args.verbose))
        logger.info("Research Agent completed successfully")
        
    except KeyboardInterrupt:
        logger.warning("Research interrupted by user")
        sys.exit(0)
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=args.verbose)
        sys.exit(1)


if __name__ == "__main__":
    main()
