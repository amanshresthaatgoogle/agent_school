from google.adk.agents.llm_agent import Agent


from .sub_agents import gce_agent, gcs_agent, finance_agent


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A root agent that delegates questiosn to different agents',
    instruction='When you get a question, send it either to the gce_agent or gcs_agent. Never answer yourself unless the question is about neither gce or gcs. Use finance_agent to handle expenses.',
    sub_agents=[
        gce_agent,
        gcs_agent,
        finance_agent
    ]
)
