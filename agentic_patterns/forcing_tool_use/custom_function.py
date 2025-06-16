from agents import Agent, Runner, function_tool, ToolsToFinalOutputResult

async def my_custom_behavior(context, results):
    # Hum sirf city name ko UPPERCASE kar ke dikhayenge
    output = results[0].output
    return ToolsToFinalOutputResult(
        is_final_output=True,
        final_output=f"CITY: {output.split()[-1].upper()}"  # e.g., "CITY: KARACHI"
    )

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Weather Agent",
    instructions="Tell the user the weather. Always use the tool.",
    tools=[get_weather],
    tool_use_behavior=my_custom_behavior
)

import asyncio
async def main():
    result = await Runner.run(agent, "What's the weather in Karachi?")
    print(result.final_output)

asyncio.run(main())
