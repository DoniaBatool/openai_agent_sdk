# Multi-Turn Conversation Module

This folder demonstrates how to manage and maintain conversation history for multi-turn interactions with an agent. It provides a practical example of how to keep context across several user-agent exchanges, enabling more natural and context-aware conversations.

## File Descriptions

### 1. `convo_history.py`
- **Purpose:** Shows how to implement and manage multi-turn conversation history with an agent.
- **Details:**
  - Defines a simple agent called `MoodBot` that interacts with the user in a friendly manner, asking about their mood and responding accordingly.
  - Initializes a conversation history (`convo`) as a list of message objects, each with a `role` (e.g., "user") and `content` (the message text).
  - Runs the agent with the initial conversation history using `Runner.run_sync`, which returns the agent's response and the updated conversation history.
  - After each agent response, the conversation history is updated using `result.to_input_list()`, ensuring that all previous turns are preserved.
  - The script demonstrates multiple turns:
    - The user greets the agent.
    - The agent responds and the user asks about the agent's mood.
    - The agent responds again, and the user shares their own feelings.
    - After each turn, the conversation history is updated and passed back to the agent for the next turn.
  - The final conversation history is printed, showing the complete multi-turn exchange.
  - This approach allows the agent to maintain context, remember previous messages, and provide more coherent and contextually relevant responses.

---

## Summary

The multi_turn_convo folder provides a clear example of:
- **Maintaining Conversation History:** Keeping track of all previous messages in a conversation, enabling context-aware agent responses.
- **Multi-Turn Interactions:** Allowing the agent and user to exchange multiple messages, with each turn building on the previous context.
- **Practical Workflow:** Demonstrates how to update and reuse conversation history after each agent response, making it easy to implement in real-world applications.

Use this example as a template for building chatbots, virtual assistants, or any system that requires multi-turn, context-rich conversations with users. 