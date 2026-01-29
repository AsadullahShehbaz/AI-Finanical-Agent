from phi.agent import Agent
from phi.tools.serpapi_tools import SerpApiTools
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def initialize_agents():
    """Initialize all AI agents with error handling"""
    try:
        logger.info("Initializing Web Agent...")
        web_agent = Agent(
            name="Web Agent",
            role="Search the web for information",
            model=Groq(id="llama-3.3-70b-versatile"),
            tools=[SerpApiTools()],
            instructions=[
                "Always include sources",
                "Provide latest information using search results",
                "Provide URLs when available"
            ],
            show_tool_calls=True,
            markdown=True,
        )
        logger.info("Web Agent initialized successfully")
        
        logger.info("Initializing Finance Agent...")
        finance_agent = Agent(
            name="Finance Agent",
            role="Get financial data and provide analysis",
            model=Groq(id="llama-3.3-70b-versatile"),
            instructions=[
                "Use tables to display data",
                "Provide clear financial analysis",
                "Include relevant metrics and statistics",
                "Format numbers properly with commas"
            ],
            show_tool_calls=True,
            markdown=True,
        )
        logger.info("Finance Agent initialized successfully")
        
        logger.info("Initializing Agent Team...")
        agent_team = Agent(
            model=Groq(id="llama-3.3-70b-versatile"),
            team=[web_agent, finance_agent],
            instructions=[
                "Always include sources", 
                "Use tables to display data",
                "Coordinate between agents to provide comprehensive answers",
                "If one agent fails, use the other agent's information",
                "Provide actionable insights"
            ],
            show_tool_calls=True,
            markdown=True,
        )
        logger.info("Agent Team initialized successfully")
        
        return agent_team
        
    except Exception as e:
        logger.error(f"Error initializing agents: {str(e)}", exc_info=True)
        raise e

def process_agent_query(agent_team, query):
    """Process query with better error handling and retries"""
    try:
        logger.info(f"Attempting to process query: {query}")
        response = agent_team.run(query)
        
        if hasattr(response, 'content'):
            return response.content
        else:
            return str(response)
            
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error in agent query: {error_msg}", exc_info=True)
        
        # Check if it's a tool use error
        if "tool_use_failed" in error_msg:
            logger.info("Tool error detected, retrying with simpler query...")
            try:
                # Retry with a simpler approach
                simplified_query = f"Provide information about {query.split('for')[-1] if 'for' in query else query}"
                logger.info(f"Simplified query: {simplified_query}")
                response = agent_team.run(simplified_query)
                
                if hasattr(response, 'content'):
                    return response.content
                else:
                    return str(response)
            except Exception as retry_error:
                logger.error(f"Retry also failed: {str(retry_error)}", exc_info=True)
                raise retry_error
        else:
            raise e
