# Clone or Assign Module

This folder demonstrates the differences between assignment, cloning, shallow copy, and deep copy when working with agent objects. Understanding these concepts is crucial for managing object references, independence, and mutations in Python.

## File Descriptions

### 1. `assign.py`
- **Purpose:** Shows what happens when you assign one agent object to another variable (reference assignment).
- **Details:**
  - Assigns the original agent to a new variable (`new_ref = orig_agent`).
  - Mutations to either variable affect the same underlying object, as both variables reference the same agent.
  - Demonstrates that changes to instructions via either reference are reflected in both.
  - No new object is created; both variables point to the same agent instance.

### 2. `clone.py`
- **Purpose:** Demonstrates how to create an independent clone of an agent object.
- **Details:**
  - Uses the agent's `clone` method to create a new, independent agent with modified attributes.
  - Mutations to the clone do not affect the original, and vice versa.
  - Both objects are fully independent, including their attributes and tools.
  - Useful for creating similar agents with different behaviors or properties.

### 3. `shallow_copy.py`
- **Purpose:** Shows how to create a shallow copy of an agent object using Python's `copy.copy`.
- **Details:**
  - The top-level agent object is copied, but nested mutable attributes (like lists) are shared between the original and the copy.
  - Mutations to nested attributes (e.g., appending to a tools list) affect both objects.
  - Mutations to top-level attributes (e.g., changing the agent's name) are independent.
  - Demonstrates the risks of shallow copying when objects have nested mutable state.

### 4. `deep_copy.py`
- **Purpose:** Demonstrates how to create a deep copy of an agent object using Python's `copy.deepcopy`.
- **Details:**
  - Both the agent and all nested attributes are fully copied, resulting in two completely independent objects.
  - Mutations to either the original or the deep copy (including nested attributes) do not affect the other.
  - Useful for duplicating complex objects with nested state that must remain independent.

---

## Summary

The clone_or_assign folder provides clear examples of:
- Reference assignment and its implications for shared state.
- Cloning for independent agent instances.
- Shallow vs. deep copying and their effects on nested attributes.

Use these examples to understand and control object copying and reference behavior in your own agent-based or Python applications. 