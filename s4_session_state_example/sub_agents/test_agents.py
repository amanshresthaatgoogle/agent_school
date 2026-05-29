from google.adk.agents.llm_agent import Agent


seq_agent_1 = Agent(
    model='gemini-2.5-flash',
    name='seq_agent_1',
    description='First agent for sequential workflow',
    instruction='Respond with I am the first sequential agent',
)

seq_agent_2 = Agent(
    model='gemini-2.5-flash',
    name='seq_agent_2',
    description='Second agent for sequential workflow',
    instruction='Respond with I am the second sequential agent',
)




loop_agent_1 = Agent(
    model='gemini-2.5-flash',
    name='loop_agent_1',
    description='First agent for loop workflow',
    instruction='Respond with I am the first loop agent',
)

loop_agent_2 = Agent(
    model='gemini-2.5-flash',
    name='loop_agent_2',
    description='Second agent for loop workflow',
    instruction='Respond with I am the second loop agent',
)



parallel_agent_1 = Agent(
    model='gemini-2.5-flash',
    name='parallel_agent_1',
    description='First agent for parallel workflow',
    instruction='Respond with I am the first parallel agent',
)

parallel_agent_2 = Agent(
    model='gemini-2.5-flash',
    name='parallel_agent_2',
    description='Second agent for parallel workflow',
    instruction='Respond with I am the second parallel agent',
)

