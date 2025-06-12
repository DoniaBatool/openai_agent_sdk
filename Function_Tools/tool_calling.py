from agents import Agent, Runner, function_tool
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

@function_tool
def get_weather(city: str) -> str:
    print(f"Getting weather for {city}")
    return "sunny"

@function_tool
def get_temperature(city: str) -> str:
    print(f"Getting temperature for {city}")
    return "70 degrees"

agent = Agent(
    name="Weather Agent",
    instructions="You are the local weather agent. You are given a city and you need to tell the weather and temperature. For any unrelated queries, say I cant help with that.",
    tools=[get_weather, get_temperature]
)

result = Runner.run_sync(agent, "Dallas")
print(result.final_output)
