from google.adk.agents.llm_agent import Agent

gce_agent = Agent(
    model='gemini-2.5-flash',
    name='gce_agent',
    description='A helpful assistant for user questions on google cloud compute engine.',
    instruction='Answer user questions to the best of your knowledge about google cloud compute engine',
)
