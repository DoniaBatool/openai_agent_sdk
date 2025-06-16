# Basics

The **Basics** folder contains foundational examples to get started with the OpenAI Agents SDK. These scripts showcase simple agent usage, dynamic prompting, and model configuration, serving as “hello world” style introductions to core concepts.

-   **code_gemini.py** – A basic example involving code generation or dual-prompt interaction. This script likely has the agent perform a coding task or handle two related prompts (hence “gemini”). For instance, it might prompt the agent to generate code and then explain it, demonstrating how the agent can handle multi-step instructions or provide reasoning alongside answers.
    
-   **default_model.py** – Demonstrates using the default model settings of the SDK or switching the agent’s model. It might simply run an agent with the default configuration (usually GPT-3.5) to show baseline behavior. Additionally, it could illustrate how to explicitly specify a model (like upgrading to GPT-4) and what effect that has on the agent’s responses or capabilities.
    
-   **mycode.py** – A simple custom script (possibly a scratchpad example) where the agent is given a straightforward task. This could be an introductory “Hello, world” agent that greets the user or a minimal workflow demonstrating how to initialize an agent and get a response. It’s likely used for quick experiments or as a template for writing new agent scripts.
    
-   **with_model.py** – An example of running an agent with a specified model or context manager. It might use a context (perhaps using a `with` statement or a specific SDK call) to temporarily switch the agent’s model or settings. For example, this script could show how to run the same prompt on two different models for comparison, or how to configure an agent to use a non-OpenAI model/provider if supported.
    

Each of these scripts can be executed to observe basic agent behaviors. They are a good starting point for understanding how to set up an agent, provide instructions, and retrieve outputs. New users of the SDK can modify these examples to experiment with prompts, models, and other parameters in a simple environment.