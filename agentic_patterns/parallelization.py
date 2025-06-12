import asyncio
from agents import Agent, Runner

# Agent 1: Weather from Source A
weather_agent_a = Agent(
    name="Weather Source A",
    instructions="Give the weather for the given city as per Source A."
)

# Agent 2: Weather from Source B
weather_agent_b = Agent(
    name="Weather Source B",
    instructions="Give the weather for the given city as per Source B."
)

async def main():
    city = input("Which city's weather do you want? ")

    # Dono agents ko **parallel** run karte hain
    task_a = Runner.run(weather_agent_a, city)
    task_b = Runner.run(weather_agent_b, city)
    result_a, result_b = await asyncio.gather(task_a, task_b)

    print(f"\nWeather from Source A: {result_a.final_output}")
    print(f"Weather from Source B: {result_b.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
