from agents import Agent, Runner, RunConfig, function_tool, ModelSettings
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
    model_settings=ModelSettings(
        include_usage=False
    )
)

config = RunConfig(tracing_disabled=True)#if false , you will get tracing logs on openai dashboard
result = Runner.run_sync(agent, "What is 2 plus 3?", run_config=config)
print(result.final_output)

