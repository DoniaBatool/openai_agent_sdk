import asyncio
from agents import Agent, run_demo_loop
#from agents.repl import run_demo_loop   # Now available

async def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant."
    )
    await run_demo_loop(agent, stream=False)

if __name__ == "__main__":
    asyncio.run(main())
