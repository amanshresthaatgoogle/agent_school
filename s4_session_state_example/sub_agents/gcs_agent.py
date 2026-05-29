from google.adk.agents.llm_agent import Agent

gcs_agent = Agent(
    model='gemini-2.5-flash',
    name='gcs_agent',
    description='A helpful assistant for user questions on google cloud storage.',
    instruction='Answer user questions to the best of your knowledge about google cloud storage. show {capacity?} if exists, if not, say no capacity',
)
