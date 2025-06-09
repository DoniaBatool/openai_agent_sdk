from agents import Agent, Runner, WebSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

agent= Agent(
    name="News Agent",
    instructions="""You are a news agent that can search the latest news on a given topic.
                    Compile the information you find into a concise summary.No markdown, 
                    just plain text""",
    tools=[WebSearchTool()]
)
while True:
    query=(input("Enter your news query (or 'quit' to exit): "))
    if query.lower() == 'quit':
        break
result= Runner.run_sync(agent, input=query)
print("\nResult:")
print(result.final_output)
print("\n" + "-"*50 + "\n")