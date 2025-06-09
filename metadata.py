from agents import Agent, Runner, ModelSettings
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

settings = ModelSettings(
    metadata={"user_id": "donia313", "session": "spring2025"}
)
agent = Agent(
    name="MetaAgent",
    instructions="Give facts.",
    model="gpt-4o",
    model_settings=settings
)
result = Runner.run_sync(agent, "Tell me about honeybees.")
print(result.last_agent)