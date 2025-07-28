import copy
from agents import Agent

# 1️⃣ Original Agent 
orig_agent = Agent(
    name="HelperAgent",
    instructions="You help the user kindly."
)
orig_agent.tools = ["translate", "summarize"]

# 2️⃣ Deep Copy creation
deep_agent = copy.deepcopy(orig_agent)

# ——— Nested Mutation on Original ———
orig_agent.tools.append("spellcheck")
print("After appending to orig_agent.tools:")
print("orig_agent.tools:", orig_agent.tools)
print("deep_agent.tools:", deep_agent.tools)
# deep_agent.tools ---- No change reflect 

# ——— Top-level Mutation on Original ———
orig_agent.name = "UltraHelper"
print("\nAfter changing orig_agent.name:")
print("orig_agent.name:", orig_agent.name)
print("deep_agent.name:", deep_agent.name)
# deep_agent.name remains unaffected----- ("HelperAgent")


#============================================================================================

# ——— Nested Mutation on deep copy ———
deep_agent.tools.append("Testcheck")
print("After appending to deep_agent.tools:")
print("deep_agent.tools:", deep_agent.tools)
print("orig_agent.tools:",orig_agent.tools)
# orig_agent.tools ---- No change reflect 


# ——— Top-level Mutation on Deep Copy ———
deep_agent.name = "personal Assistant"
print("\nAfter changing deep_agent.name:")
print("deep_agent.name:", deep_agent.name)
print("orig_agent.name:", orig_agent.name)
# orig_agent.name remains unaffected----- ("UltraHelper")