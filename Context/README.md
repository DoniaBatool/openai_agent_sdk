# Context Module

This folder demonstrates various ways to manage and utilize context objects in agent-based systems. Context allows agents to access user-specific or session-specific information, enabling more personalized and stateful interactions.

## File Descriptions

### 1. `context_dataclass.py`
- **Purpose:** Shows how to use a Python dataclass as a context object for an agent.
- **Details:**
  - Defines a `UserContext` dataclass with fields like `name` and `user_id`.
  - Implements a tool function `greet_user` that accesses the context to greet the user by name and ID.
  - Demonstrates how to pass the context object to the agent and use it within tools.
  - Runs the agent asynchronously and prints the personalized greeting.

### 2. `context_pydantic.py`
- **Purpose:** Demonstrates using a Pydantic model as a context object for an agent.
- **Details:**
  - Defines a `UserContextModel` Pydantic model with fields like `name`, `user_id`, and `is_pro`.
  - Implements a tool function `describe_user` that describes the user based on the context, including whether they are a "Pro user".
  - Shows how to pass the Pydantic context to the agent and use it in tools.
  - Runs the agent asynchronously and prints the user description.

### 3. `dynamic_instructions.py`
- **Purpose:** Demonstrates how to generate agent instructions dynamically based on the context.
- **Details:**
  - Uses a dataclass `UserContext` for context.
  - Defines a function `make_dynamic_instructions` that generates personalized instructions for the agent based on the context (e.g., greeting the user by name and ID).
  - The agent receives these dynamic instructions at runtime, allowing for highly personalized agent behavior.
  - Runs the agent asynchronously and prints the result.

### 4. `input_with_context.py`
- **Purpose:** Shows how to combine user input with context information for the agent.
- **Details:**
  - Uses a dataclass `UserContext` for context.
  - Prepares a user query that includes context information (e.g., user name and ID) in the input string.
  - Passes both the combined input and the context object to the agent.
  - Demonstrates how the agent and its tools can access and use both the input and the context for more informed responses.
  - Runs the agent asynchronously and prints the personalized output.

---

## Summary

The Context folder provides practical examples of:
- Using both dataclasses and Pydantic models as context objects for agents.
- Accessing context within agent tools for personalized responses.
- Generating dynamic agent instructions based on context.
- Combining user input with context for richer interactions.

Use these examples as templates for building agents that can maintain and utilize user/session context for more intelligent and personalized applications. 