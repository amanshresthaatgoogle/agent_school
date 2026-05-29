from google.adk.agents.llm_agent import Agent

from .sub_agents import gce_agent, gcs_agent, sequential_agent, loop_agent, parallel_agent



root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A root agent that tests different agents',
    instruction="""
    - When you get a question about about compute engine, send it to gce_agent
    - When you get a question about clou dstorage, send it to gcs_agent
    """,

    # - When you are asked to test a sequential agent, send it to sequential_agent
    # - When you are asked to test a loop agent, send it to loop_agent
    # - When you are asked to test a parallel agent, send it to parallel_agent
    
    sub_agents=[
        gce_agent,
        gcs_agent,
        # sequential_agent,
        # loop_agent,
        # parallel_agent
    ]
)
