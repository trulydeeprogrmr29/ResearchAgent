"""
Streamlit web interface for Research Agent.
Provides an interactive UI for research queries.
"""

import streamlit as st
import asyncio
import logging
from research_bot.groq_manager import GroqResearchManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Research Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with better typography
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1rem;
        font-weight: bold;
    }
    /* Report styling */
    .report-content {
        font-size: 1.1rem;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔍 AI Research Agent")
st.markdown("*Powered by Groq - Fast AI Research Automation*")

# Main content
st.subheader("📝 Enter Your Research Query")
query = st.text_area(
    "What would you like to research?",
    height=100,
    placeholder="Example: What are the latest advancements in quantum computing?",
    label_visibility="collapsed"
)

st.markdown("---")

# Research button
if st.button("🚀 Start Research", use_container_width=True, type="primary"):
    if not query or not query.strip():
        st.error("❌ Please enter a research query")
    else:
        with st.spinner("🔄 Researching... This may take a minute"):
            try:
                logger.info(f"Streamlit: Starting research for: {query}")
                
                # Create progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Initialize manager
                manager = GroqResearchManager()
                
                # Run research
                status_text.info("📊 Generating search plan...")
                progress_bar.progress(25)
                
                status_text.info("🔎 Performing searches...")
                progress_bar.progress(50)
                
                status_text.info("📝 Writing comprehensive report...")
                progress_bar.progress(75)
                
                # Run async function and get report
                report = asyncio.run(manager.run(query))
                
                progress_bar.progress(100)
                status_text.success("✅ Research completed successfully!")
                
                # Display the report with better formatting
                st.markdown("---")
                st.markdown('<div class="report-content">', unsafe_allow_html=True)
                st.markdown(report.markdown_report)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Display follow-up questions
                if report.follow_up_questions:
                    st.markdown("---")
                    st.markdown("### 🤔 Follow-up Questions")
                    for i, question in enumerate(report.follow_up_questions, 1):
                        st.markdown(f"**{i}. {question}**")
                
                logger.info(f"Streamlit: Research completed for: {query}")
                
            except Exception as e:
                st.error(f"❌ Research failed: {str(e)}")
                logger.error(f"Streamlit: Research failed: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.9rem;">
    <p><strong>Research Agent v0.1.0</strong> | Powered by Groq</p>
</div>
""", unsafe_allow_html=True)
