"""
Groq-based Research Manager - Pure Groq implementation without OpenAI dependency.
Uses Groq API for all LLM operations.
"""

import asyncio
import json
import logging
from typing import List
from groq import Groq
from pydantic import BaseModel
from .config import config

logger = logging.getLogger(__name__)


class SearchItem(BaseModel):
    reason: str
    query: str


class SearchPlan(BaseModel):
    searches: List[SearchItem]


class ResearchReport(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: List[str]


class GroqResearchManager:
    def __init__(self):
        self.client = Groq(api_key=config.groq_api_key)
        self.model = config.planner_model
        
    async def run(self, query: str) -> None:
        """Run research on a given query."""
        try:
            logger.info(f"Starting Groq-based research for: {query}")
            plan = await self._plan_searches(query)
            logger.info(f"Generated plan with {len(plan.searches)} searches")
            
            results = await self._perform_searches(plan.searches)
            logger.info(f"Completed {len(results)} searches")
            
            report = await self._write_report(query, results)
            print("\n" + "="*80)
            print(report.markdown_report)
            print("="*80 + "\n")
            
        except Exception as e:
            logger.error(f"Research failed: {e}")
            raise

    async def _plan_searches(self, query: str) -> SearchPlan:
        """Generate search plan using Groq."""
        prompt = f"""You are a research strategist. Given a question, propose 5-10 web searches that, 
together, will answer it comprehensively. Return ONLY a valid JSON object with this structure:
{{"searches": [{{"reason": "why search", "query": "search term"}}, ...]}}

Question: {query}

Return only the JSON object, no other text."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        try:
            content = response.choices[0].message.content
            # Try to extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            plan_data = json.loads(content.strip())
            return SearchPlan(**plan_data)
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to parse search plan: {e}")
            # Return default plan if parsing fails
            return SearchPlan(searches=[
                SearchItem(reason="Direct answer", query=query),
                SearchItem(reason="Latest developments", query=f"{query} 2024 2025"),
            ])

    async def _perform_searches(self, searches: List[SearchItem]) -> List[str]:
        """Perform searches sequentially (respecting rate limits)."""
        results = []
        for search in searches[:config.max_searches]:
            result = await self._search_and_summarize(search.query)
            results.append(result)
            # Rate limiting: small delay between requests
            await asyncio.sleep(0.5)
        return results

    async def _search_and_summarize(self, query: str) -> str:
        """Search using Groq and return a summary (simulated)."""
        prompt = f"""You are an internet researcher. Based on your knowledge, provide a brief summary 
(max 300 words) about: {query}

Format your response as markdown bullet points."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        
        return response.choices[0].message.content

    async def _write_report(self, query: str, summaries: List[str]) -> ResearchReport:
        """Write final report using Groq."""
        research_text = "\n\n".join(summaries)
        
        prompt = f"""You are a senior analyst. Combine the following research summaries into a 
coherent, well-structured report. Include:
1. A one-paragraph executive summary
2. The full report with key findings (3-5 pages of markdown)
3. 3-5 thoughtful follow-up questions

Original query: {query}

Research summaries:
{research_text}

Return a JSON object with this structure:
{{"short_summary": "1 paragraph", "markdown_report": "full report in markdown", "follow_up_questions": ["q1", "q2", ...]}}

Return only the JSON object."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        try:
            content = response.choices[0].message.content
            # Try to extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            report_data = json.loads(content.strip())
            return ResearchReport(**report_data)
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to parse report: {e}")
            # Return default report if parsing fails
            return ResearchReport(
                short_summary="Research completed successfully.",
                markdown_report=f"# Research Report\n\n## Query\n{query}\n\n## Findings\n\n" + research_text,
                follow_up_questions=["What are the implications?", "What's next?"]
            )
