from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool
import asyncio, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

@dataclass
class UserContext:
    name: str
    user_id: int

@function_tool
async def greet_user(wrapper: RunContextWrapper[UserContext]) -> str:
    return f"Hello, {wrapper.context.name}! (ID: {wrapper.context.user_id})"

# --- DYNAMIC INSTRUCTION FUNCTION ---
def make_dynamic_instructions(wrapper: RunContextWrapper[UserContext],agent) -> str:
    ctx = wrapper.context
    return f"Greet the user '{ctx.name}' (ID: {ctx.user_id}) warmly! Don't forget to mention their name  and id in the greeting."

async def main():
    ctx = UserContext(name="Alice", user_id=456)
    agent = Agent[UserContext](
        name="Greeter",
        instructions=make_dynamic_instructions,    # <-- DYNAMIC!
        tools=[greet_user],
    )
    result = await Runner.run(
        starting_agent=agent,
        input="Hi there!",
        context=ctx,
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

