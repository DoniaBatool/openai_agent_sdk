from agents import Agent, Runner
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# Spanish translation agent
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="Translate the user's message to Spanish."
)

# Italian translation agent
italian_agent = Agent(
    name="Italian Agent",
    instructions="Translate the user's message to Italian."
)

# Orchestrator agent does all the combining & validation itself!
orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions=(
        "If the user wants translation to Spanish, use the Spanish Agent tool. "
        "If the user wants translation to Italian, use the Italian Agent tool. "
        "If both, call both agents. "
        "When you receive translations, combine them in a formatted message like:\n"
        "Spanish: <translation>\nItalian: <translation>.\n"
        "If any translation looks incorrect, mention it. Never translate yourself!"
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="spanish_translator",
            tool_description="Translate English text to Spanish."
        ),
        italian_agent.as_tool(
            tool_name="italian_translator",
            tool_description="Translate English text to Italian."
        )
    ]
)

# --- RUN ---
user_input = input("What do you want to translate, and to which languages? ")
result = Runner.run_sync(orchestrator_agent, user_input)
print("\nFinal Output:")
print(result.final_output)
