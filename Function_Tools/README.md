# Function Tools

This folder showcases how to use Python functions as tools within an agent – a feature of the Agents SDK that allows direct function calls (similar to OpenAI function calling or the `function_tool` utility). It provides an example of registering a custom function so the agent can invoke it as needed, and includes visual aids to help understand the process.

-   **tool_calling.py** – An example script where an agent is equipped with a custom function as a tool. The script likely defines a Python function (e.g., a simple calculator or a date formatter) and uses the SDK’s tool interface (such as `function_tool(...)`) to make it available to the agent. When run, the agent receives a prompt that triggers the function, demonstrating how the agent decides to call the function and how the function’s result is used in the final answer.
    
-   **tool_calling_1a.png** – An image illustrating the tool-calling process or outcome. This could be a snapshot of the agent’s intermediate steps (like a console log or a Chainlit UI screenshot) showing the agent recognizing when to use the function tool and the output it produces.
    
-   **tool_calling_1b.png** – A second image to complement the first, possibly highlighting another aspect of the example (for instance, the flow of control from agent to function and back, or an alternate run with different input). It helps visualize the concept of function calling within the agent’s reasoning.
    

By studying this example, developers can learn how to integrate custom logic into the agent’s decision-making. It’s a powerful pattern for extending the agent’s capabilities beyond the built-in toolset. To try it out, run `tool_calling.py` and observe how the agent utilizes the provided function to fulfill its instructions.