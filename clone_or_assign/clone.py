from agents import Agent

# Original agent
orig_agent = Agent(
    name="Pirate",
    instructions="Speak like a pirate: Arrr!",
    tools=["tester"]
)

# Clone: independent new instance with modified instructions
clone_agent = orig_agent.clone(
    name="Robot",
    instructions="Speak like a robot: Beep boop."
)
clone_agent.tools.append("tester2")
#orig_agent.tools.append("tester2")
# Mutate clone
orig_agent.instructions = "Robotic voice engaged."

print(orig_agent.instructions)   # Speak like a pirate: Arrr!
print(orig_agent.name)
print(orig_agent.tools)
print(clone_agent.instructions)  # Robotic voice engaged.
print(clone_agent.name)
print(clone_agent.tools)
# clone_agent and orig_agent both different objects of the Agent class , and 
# changes in any of these objects will not affect the other object, both the objects aree independent
