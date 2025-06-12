from agents import Agent, Runner, ModelSettings
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

settings = ModelSettings(
    include_usage=False   # Usage stats chahiye
)

agent = Agent(
    name="UsageAgent",
    instructions="Reply to the prompt and track usage.",
    model="gpt-4o",
    model_settings=settings
)

result = Runner.run_sync(agent, "Tell me a fact about honeybees.")
print(result.final_output)
print("--- USAGE INFO ---")
print(result.raw_responses[0].usage)  # Yahan usage details ayengi!
