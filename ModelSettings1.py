from agents import Agent, Runner, ModelSettings
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# default model gpt-4o
agent1 = Agent(
    name="Haiku agent 1",
    instructions="Always respond in haiku form",
    model_settings=ModelSettings(
        temperature=0.3,
        max_tokens= 150
    )
)


agent2 = Agent(
    name="Haiku agent 2",
    instructions="Reply in haiku form but use different metaphors.",
    model="gpt-4o-mini",
    model_settings=ModelSettings (
       
        temperature= 0.3,
        max_tokens=150
    )
)


agent3 = Agent(
    name="Poetry agent",
    instructions="Always reply in rhyming poetry.",
    model= "gpt-3.5-turbo",
    model_settings=ModelSettings (
        
        temperature= 0.8,
        max_tokens= 200
    )
)

# Example usage (one prompt per agent)


result1 = Runner.run_sync(agent1, "Write a haiku about sunrise.")
result2 = Runner.run_sync(agent2, "Write a haiku about rain.")
result3 = Runner.run_sync(agent3, "Write a short poem about the ocean.")

print("Agent 1:", result1.final_output)
print("Agent 2:", result2.final_output)
print("Agent 3:", result3.final_output)
