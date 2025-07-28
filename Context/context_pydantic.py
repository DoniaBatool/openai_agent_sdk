from pydantic import BaseModel
from agents import Agent, Runner, RunContextWrapper, function_tool
import asyncio, os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")
class UserContextModel(BaseModel):
    name: str
    user_id: int
    is_pro: bool = False

@function_tool
async def describe_user(wrapper: RunContextWrapper[UserContextModel]) -> str:
    ctx = wrapper.context
    status = "Pro user" if ctx.is_pro else "regular user"
    return f"User {ctx.name} (ID {ctx.user_id}) is a {status}."

async def main():
    ctx_model = UserContextModel(name="Bob", user_id=789, is_pro=True)
    agent = Agent[UserContextModel](
        name="User Describer",
        instructions="Describe the user based on context.",
        tools=[describe_user],
    )
    result = await Runner.run(
        starting_agent=agent,
        input="Who is the user?",
        context=ctx_model,
    )
    print(result.final_output)  # e.g. "User Bob (ID 789) is a Pro user."
