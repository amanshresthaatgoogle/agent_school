from google.adk.agents.llm_agent import Agent


def warn_capacity() -> str:
    """Warns the user of capacity contraints"""
    return "Capacity is constrained"


gce_agent = Agent(
    model='gemini-2.5-flash',
    name='gce_agent',
    description='A helpful assistant for user questions on google cloud compute engine.',
    instruction='Answer user questions to the best of your knowledge about google cloud compute engine. Before answering any question, call the tool `warn_capacity` and prepend the result.',
    tools=[warn_capacity]
)
