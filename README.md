# ADK Agent School

This repository contains a series of examples demonstrating how to build and deploy AI agents using the ADK (Agent Development Kit). The examples progress from a simple single agent to complex multi-agent systems with tools, workflows, and session management.

## Project Structure

- **[s0_my_agent](./s0_my_agent)**: A basic single-agent setup using `Agent` and `to_a2a`.
- **[s1_sub_agent_example](./s1_sub_agent_example)**: Demonstrates how to delegate tasks to sub-agents.
- **[s2_tools_example](./s2_tools_example)**: Shows how to integrate tools, including MCP (Model Context Protocol).
- **[s3_workflows_example](./s3_workflows_example)**: Introduces complex workflows including sequential, loop, and parallel execution.
- **[s4_session_state_example](./s4_session_state_example)**: Demonstrates managing state across multiple turns in a session.

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the necessary packages:
   ```bash
   pip install mcp
   pip install google-adk
   pip install google-adk[a2a]
   ```

## Running the Agents Locally

You can run and test your agents locally using the ADK web interface:

```bash
adk web --allow_origins "regex:https://.*\.cloudshell\.dev"
```

*Note: The `--allow_origins` flag is specifically configured for Google Cloud Shell users to allow the browser to connect to the local development server.*

## Deployment

To deploy an agent to the Agent Engine on Google Cloud, use the following command:

```bash
adk deploy agent_engine \
    --project=$PROJECT_ID \
    --region=$LOCATION_ID \
    --display_name="My First Agent" \
    s0_my_agent
```

## Useful Links

- **Deploy:** [ADK Deployment Documentation](https://adk.dev/deploy/agent-runtime/deploy/)
- **MCP:** [MCP Tools in ADK](https://adk.dev/tools-custom/mcp-tools/)
- **Long running task:** [Long-running Task Tools](https://adk.dev/tools-custom/function-tools/#long-run-tool)
