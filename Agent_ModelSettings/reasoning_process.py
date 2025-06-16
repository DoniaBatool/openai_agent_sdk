from agents import Agent, Runner,  ModelSettings
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

settings = ModelSettings(
    reasoning={"effort": "high"}   # ya "medium", ya "low"
)

agent = Agent(
    name="Reasoning Assistant",
    instructions="You are a helpful assistant",
    model="o4-mini",
    model_settings=settings
)

result = Runner.run_sync(agent, "Write a five line poem on AI Agents.")
print("o4-mini (reasoning) Output:\n", result.final_output)
