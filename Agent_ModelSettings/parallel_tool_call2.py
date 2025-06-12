
from agents import Agent, Runner, ModelSettings,function_tool
import os
from dotenv import load_dotenv


load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

@function_tool
def get_temperature(city: str) -> str:
    return f"The temperature in {city} is 35°C."

settings = ModelSettings(
    parallel_tool_calls=True  # Enable parallel tool calls or to disable :False
)

agent = Agent(
        name="Weather & Temp Agent",
        instructions="Use the tools to answer about both weather and temperature if asked.",
        tools=[get_weather, get_temperature],
        model="gpt-4o",
        model_settings=settings
    )

result = Runner.run_sync(agent, "Tell me the weather and temperature in Karachi.")
print(result.final_output)

