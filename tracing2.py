from agents import Agent, Runner, function_tool, ModelSettings, trace
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


@function_tool
def add(a: int, b: int) -> int:
    return a + b

agent = Agent(
    name="CalcAgent",
    instructions="Use the add tool if asked about addition.",
    tools=[add],
    model="gpt-4o",
    
)

with trace("Final Workflow"):
    result = Runner.run_sync(agent, "What is 2 plus 3?")
    print(result.final_output)

