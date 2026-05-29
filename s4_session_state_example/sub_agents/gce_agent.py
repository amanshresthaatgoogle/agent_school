from google.adk.agents.llm_agent import Agent
from google.adk.tools import ToolContext



def warn_capacity(tool_context: ToolContext) -> str:
    """Warns the user of capacity constraints"""

    # 1. FIXED: Changed 'context' to 'tool_context'
    if "capacity" not in tool_context.state:
        tool_context.state["capacity"] = []
    
    tool_context.state["capacity"].append({"item": "n2d", "qty": 3000})
    
    return f"Capacity warning logged.."


gce_agent = Agent(
    model='gemini-2.5-flash',
    name='gce_agent',
    description='A helpful assistant for user questions on google cloud compute engine.',
    instruction='''
      Answer user questions to the best of your knowledge about google cloud compute engine. 
      
      Before answering any question, you MUST call the tool `warn_capacity`.
      
    ''',
    tools=[warn_capacity],
    # output_key="first_greeting"
)