# Agent_ModelSettings
This folder contains examples focused on configuring agent models and runtime settings, including switching model configurations, tracking usage, parallel tool execution, and decision reasoning. These scripts demonstrate how different model settings and context management can affect agent behavior.
## Model_Settings1.py 
Demonstrates setting up an agent with a specific model configuration. For example, it may initialize an agent with certain parameters (like using GPT-3.5 vs. GPT-4 or custom tokens) to show how model choice affects responses.
## Model_Settings2.py 
Similar to ModelSettings1, but with an alternate configuration or model. This script could use a different model or altered settings (such as temperature or context length) to compare outcomes with the first configuration.
## include_usage.py 
Shows how to include and retrieve token usage information from agent runs. This example runs an agent task and prints/logs the API usage metrics (prompt tokens, completion tokens, etc.), illustrating how to monitor and limit costs.
## meta_data.py
Demonstrates attaching and using metadata in an agent’s context. For instance, it might add custom metadata or tags to the agent’s RunContext or requests, showing how to pass additional information (like user IDs or session info) through the agent workflow.
## parallel_tool_call1.py 
An experiment with having an agent invoke multiple tools in parallel or in rapid succession. It likely sets up an agent that needs to use more than one tool and showcases a pattern for either concurrent execution or handling multiple tool outputs.
## parallel_tool_call2.py
A companion to parallel_tool_call1, providing a variation on parallel tool usage. This script might implement a different method for running tools (e.g., sequential vs. parallel) or demonstrate the performance difference and result handling when an agent calls tools simultaneously.
## reasoning_process.py 
Illustrates capturing an agent’s reasoning process. It may prompt the agent to output its thought process or use the SDK’s tracing/logging to display intermediate reasoning steps. This helps users understand how the agent arrives at a conclusion or chooses a tool.
## tool_choice.py
Shows an agent deciding between multiple available tools. This example likely registers several tools and then uses the agent’s prompt or logic to pick the appropriate tool based on the user’s query. It demonstrates dynamic tool selection (e.g., math tool vs. search tool depending on question).

# Note:
Each script can be run independently to observe how different settings and configurations impact the agent’s behavior. These examples are useful for learning how to tweak model parameters and utilize the SDK’s features for usage tracking and decision transparency.
