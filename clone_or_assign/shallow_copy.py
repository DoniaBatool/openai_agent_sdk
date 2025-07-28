import copy
from agents import Agent

# 1️⃣ Original Agent 
orig_agent = Agent(
    name="HelperAgent",
    instructions="You help the user kindly."
)
# Nested attribute: list of tools
orig_agent.tools = ["translate", "summarize"]

# 2️⃣ Shallow Copy creation
shallow_agent = copy.copy(orig_agent)

# ——— Shared Mutation Example ———red
# if we make chages to the nested list it will remain shared
orig_agent.tools.append("spellcheck")
# shallow_agent.tools.append("spellcheck")
print("After appending to orig_agent.tools:")
print("orig_agent.tools:", orig_agent.tools)
print("shallow_agent.tools:", shallow_agent.tools)
# Output dono mein ['translate', 'summarize', 'spellcheck']

# ——— Independent (Non-shared) Mutation Example ———
# Top-level attribute (immutable) means changing it in one object will not affect the other object
orig_agent.name = "SuperHelper"
# shallow_agent.name = "SuperHelper"
print("\nAfter changing orig_agent.name:")
print("orig_agent.name   :", orig_agent.name)
print("shallow_agent.name:", shallow_agent.name)
# shallow_agent.name will remain "HelperAgent" ,
# however the name of orig_agent will become SuperHelper
