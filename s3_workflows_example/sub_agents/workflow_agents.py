from google.adk.agents import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent
from google.adk.agents.parallel_agent import ParallelAgent

from .test_agents import  seq_agent_1, seq_agent_2, loop_agent_1, loop_agent_2, parallel_agent_1, parallel_agent_2


sequential_agent = SequentialAgent(
    name='sequential_parent_agent',
    description='Executes agents sequentially',
    sub_agents=[seq_agent_1, seq_agent_2]
)
loop_agent = LoopAgent(
    name='loop_parent_agent',
    description='Executes agents in a loop',
    max_iterations=3,
    sub_agents=[loop_agent_1, loop_agent_2]
)

parallel_agent = ParallelAgent(
    name='parallel_parent_agent',
    description='Executes agents in parallel',
    sub_agents=[parallel_agent_1, parallel_agent_2]
)