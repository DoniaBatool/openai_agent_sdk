from agents import Agent, Runner, FileSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

agent= Agent(
    name="Linkedin Profile Analyst",
    instructions="You are a helpful assistant and you job is to respond to user query.",
    tools=[FileSearchTool(
        max_num_results=3,
        vector_store_ids=["vs_6842a4c66e5c819195425b4a342114c0"]
    )]
)
result= Runner.run_sync(agent, "What do you know about Donia's Profile?")
print(result.final_output)