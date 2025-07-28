from agents import Agent
# Original agent
orig_agent = Agent(
    name="Helper",
    instructions="You help the user politely."
)

# Assignment: new_ref is only pointing towards orig_agent
new_ref = orig_agent

# Mutation in orig_agent
orig_agent.instructions = "You are super helpful!"
print(new_ref.instructions)

# Mutation in new_ref
new_ref.instructions = "You are super intelligent!"
print(orig_agent.instructions)

# Output: You are super helpful!
# new_ref and orig_agent both are same objects
#Note: Here we are just assigning one Agent object to a new variable . No new object has been made . 
# this variable new_ref is just the reference of the Agent object i.e orig_agent means that the variable 
#new_ref is pointing towards the old agent object i.e orig_agent.In this CASE IF YOU WILL MAKE CHANGES TO THE 
# orig_agent OR TO THE new_ref , the changes will be reflected everywhere.

