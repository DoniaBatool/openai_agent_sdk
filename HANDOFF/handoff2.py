from agents import Agent, Runner
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide assistance with math queries. Explain your reasoning at each step and include examples"
)


# This agent has the capability to handoff to either the history or math tutor agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question." +
    "If neither agent is relevant, provide a general response.",
    handoffs=[history_tutor_agent,math_tutor_agent]
)
result = Runner.run_sync(triage_agent, "How do I add 2 and 2?")
print(result.final_output)

#result = Runner.run_sync(triage_agent, "How did WW2 start?")
#print(result.final_output)