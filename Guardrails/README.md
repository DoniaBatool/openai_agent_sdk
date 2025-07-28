# Guardrails Module

This folder demonstrates how to implement and use input and output guardrails in agent-based systems. Guardrails are safety or quality checks that validate user input or agent output, ensuring that the system behaves as intended and prevents undesired or unsafe interactions.

## File Descriptions

### 1. `input_guardrail.py`
- **Purpose:** Demonstrates how to use input guardrails to filter or block undesirable user inputs before they reach the agent.
- **Details:**
  - Defines a simple input guardrail function `no_forbidden` using the `@input_guardrail` decorator. This function checks if the user input contains the word "forbidden" (case-insensitive).
  - If the forbidden word is found, the guardrail triggers a "tripwire" and blocks the input, returning a message and raising an `InputGuardrailTripwireTriggered` exception.
  - If the input is clean, the agent proceeds as normal.
  - The `SimpleEcho` agent is created with this input guardrail attached. It simply echoes the input back if allowed.
  - The script tests the agent with both safe and forbidden inputs, demonstrating how the guardrail blocks unsafe input and provides detailed feedback about the violation.
  - Example output includes information about which guardrail was triggered, the reason, and the tripwire status.

### 2. `output_guardrail.py`
- **Purpose:** Demonstrates how to use output guardrails to validate or enforce quality on agent responses before they are returned to the user.
- **Details:**
  - Defines a Pydantic model `PolitenessCheckOutput` to structure the output of the guardrail (e.g., whether the response is polite and a message for the user).
  - Implements an output guardrail function `polite_guard` using the `@output_guardrail` decorator. This function checks if the agent's response contains the word "please" (case-insensitive).
  - If the response is not polite (does not include "please"), the guardrail triggers a tripwire, returning a message and raising an `OutputGuardrailTripwireTriggered` exception.
  - The `PoliteAgent` agent is created with this output guardrail attached. Its instructions specify to use "please" in responses if the user's request contains it.
  - The script tests the agent with both impolite and polite requests, showing how the guardrail enforces the desired output style and provides detailed feedback if the check fails.
  - Example output includes the guardrail's name, details about the failure, and the structured output from the guardrail function.

---

## Summary

The Guardrails folder provides practical examples of:
- **Input Guardrails:** Preventing unsafe or unwanted user inputs from reaching the agent, with custom logic and detailed feedback.
- **Output Guardrails:** Enforcing quality or safety standards on agent responses, ensuring outputs meet specific criteria before being returned to the user.
- **Tripwire Mechanism:** Both input and output guardrails can "trip" and block the flow, raising exceptions with detailed context for handling or logging.
- **Extensibility:** The guardrail pattern can be extended to cover a wide range of input/output validation, moderation, or compliance scenarios in agentic systems.

Use these examples as templates for building safer, more robust, and user-friendly agent-based applications. 