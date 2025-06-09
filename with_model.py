from agents import Agent, Runner
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gpt-4o-mini")

result = Runner.run_sync(agent, "Write a five line poem on AI Agents.")
print(result.final_output)
