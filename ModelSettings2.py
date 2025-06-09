from agents import Agent, Runner, ModelSettings
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

model_setting_haiku = ModelSettings(
    temperature=0.3,
    max_tokens=150
)
model_setting_poetry = ModelSettings(
    temperature=0.8,
    max_tokens=200
)

# default model gpt-4o
agent1 = Agent(
    name="Haiku agent 1",
    instructions="Always respond in haiku form",
    model_settings=model_setting_haiku 
)


agent2 = Agent(
    name="Haiku agent 2",
    instructions="Reply in haiku form but use different metaphors.",
    model="gpt-4o-mini",
    model_settings=model_setting_poetry
)



# Example usage (one prompt per agent)


result1 = Runner.run_sync(agent1, "Write a haiku about sunrise.")
result2 = Runner.run_sync(agent2, "Write a haiku about rain.")


print("Agent 1:", result1.final_output)
print("Agent 2:", result2.final_output)
