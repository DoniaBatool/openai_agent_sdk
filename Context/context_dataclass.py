from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool
import asyncio, os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# 1. Define a context dataclass with arbitrary fields.
@dataclass
class UserContext:
    name: str
    user_id: int
    # (You can also add methods or other attributes here.)

# 2. A tool function that uses the context.
@function_tool
async def greet_user(wrapper: RunContextWrapper[UserContext]) -> str:
    # Access the context object via wrapper.context
    """Fetch the name and id of the user. Call this function to get user's name and id information."""
    return f"Hello, {wrapper.context.name}! (ID: {wrapper.context.user_id})"

# 3. Assemble the agent and run it with the context.
async def main():
    ctx = UserContext(name="Alice", user_id=456)
    agent = Agent[UserContext](
        name="Greeter",
        instructions="Greet the user politely",
        tools=[greet_user],
    )
    result = await Runner.run(
        starting_agent=agent,
        input=f"Hi there!",
        context=ctx,       # Pass the context object here
    )
    print(result.final_output)  # e.g. "Hello, Alice! (ID: 456)"

if __name__ == "__main__":
    asyncio.run(main())