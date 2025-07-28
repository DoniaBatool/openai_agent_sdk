# HANDOFF Module

This folder demonstrates various agent handoff patterns using the `Agent` and `Runner` abstractions. Each file explores a different aspect of agent-to-agent handoff, callbacks, and customization in multi-agent systems.

## File Descriptions

### 1. `handoff1.py`
- **Purpose:** Demonstrates a two-step agent handoff for generating programming tutorials.
- **Details:**
  - Defines a `Tutorial` Pydantic model with `outline` and `tutorial` fields.
  - The `Outline Builder` agent creates an outline for a programming topic.
  - The outline is handed off to the `Tutorial Generator` agent, which generates a detailed tutorial in Markdown, including code snippets and explanations.
  - The process is run synchronously with `Runner.run_sync`, and the final output is printed.
  - This file shows how to chain agents for multi-step content generation, using structured data as the handoff payload.

### 2. `handoff2.py`
- **Purpose:** Shows agent handoff based on the type of user query (triage).
- **Details:**
  - Defines two specialist agents: `History Tutor` and `Math Tutor`, each with their own instructions and handoff descriptions.
  - A `Triage Agent` receives a user question and decides which specialist agent should handle it, based on the content of the question.
  - The triage agent can hand off to either the history or math agent, or provide a general response if neither is relevant.
  - Demonstrates dynamic routing and delegation in multi-agent systems.

### 3. `on_handoff.py`
- **Purpose:** Illustrates the use of `on_handoff` callbacks for custom logic during handoff.
- **Details:**
  - Similar to `handoff2.py`, but adds custom callback functions (`on_math_handoff`, `on_history_handoff`) that are executed when a handoff occurs.
  - These callbacks print messages to indicate which agent is being handed off to, but could be extended for logging, analytics, or other side effects.
  - The triage agent uses the `handoff` function to attach these callbacks to each specialist agent.
  - Shows how to add hooks for custom behavior during agent transitions.

### 4. `on_handoff_input_type.py`
- **Purpose:** Demonstrates handoff with custom input types and escalation logic.
- **Details:**
  - Defines a `ManagerEscalation` Pydantic model to structure escalation data (issue and reason).
  - Implements a `create_ticket` function tool for the manager agent to simulate ticket creation.
  - The `Customer Service` agent handles general inquiries and can escalate unresolved issues to the `Manager` agent, passing along the structured escalation data.
  - The `on_manager_handoff` callback logs escalation details and could be extended to store them in a database.
  - This file demonstrates how to pass structured, context-rich data between agents and trigger side effects during escalation.

### 5. `tool_name_override.py`
- **Purpose:** Shows how to override tool names in handoff scenarios.
- **Details:**
  - Defines specialist agents and attaches custom `on_handoff` callbacks.
  - Uses the `tool_name_override` parameter in the `handoff` function to assign custom tool names (e.g., `ask_history_expert`, `ask_math_expert`) for each handoff.
  - The triage agent is configured with these custom-named handoff tools, making the agent interface more descriptive and API-friendly.
  - Demonstrates how to customize both the behavior and the interface of agent handoff tools.

### 6. `tool_description_override.py`
- **Purpose:** Demonstrates how to override tool descriptions in handoff tools for better clarity in agent interfaces.
- **Details:**
  - Defines specialist agents (`History Tutor`, `Math Tutor`) and attaches custom `on_handoff` callbacks.
  - Uses the `tool_description_override` parameter in the `handoff` function to provide custom descriptions for each handoff tool (e.g., "Transfer this question to the History Tutor for detailed context and timelines.").
  - The triage agent is configured with these handoff tools, each having a clear, user-friendly description that appears in the agent interface or API documentation.
  - Demonstrates how to make agent handoff flows more transparent and understandable for users and developers.

### 7. `input_filter.py`
- **Purpose:** Demonstrates how to filter or preprocess input before handoff to child agents.
- **Details:**
  - Defines specialist agents and attaches custom `on_handoff` callbacks.
  - Implements an `input_filter` function (`filter_user_only`) that processes the input data before it is handed off to the child agent. In this example, it keeps only the latest user message from the chat history.
  - The `input_filter` is passed as a parameter to the `handoff` function for both history and math tutor agents.
  - The triage agent uses these filtered handoff tools, ensuring that only relevant input is passed to the specialist agent.
  - Demonstrates how to control and sanitize the data flow between agents, which is useful for privacy, context reduction, or custom preprocessing needs.

---

## Summary

This folder is a practical guide to implementing agent handoff patterns, including:
- Multi-step agent workflows
- Dynamic agent selection (triage)
- Custom handoff callbacks
- Structured input passing between agents
- Customizing tool names and descriptions
- Filtering and preprocessing input before handoff

Use these examples as templates for building robust, modular, and extensible agentic systems.