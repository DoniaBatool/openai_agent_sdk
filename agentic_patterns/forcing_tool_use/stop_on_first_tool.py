from agents import Agent, Runner, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Weather Agent",
    instructions="Tell the user the weather. Always use the tool.",
    tools=[get_weather],
    tool_use_behavior="stop_on_first_tool"
)

result = Runner.run_sync(agent, "What's the weather in Karachi?")
print(result.final_output)
