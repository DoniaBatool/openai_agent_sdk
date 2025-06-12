from agents import Agent, Runner
import os
from dotenv import load_dotenv


load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


# Define the specialized agents for shopping and support
shopping_agent = Agent(
    name="Shopping Agent",
    instructions="You are a shopping assistant who can help with product searches and recommendations."
)
support_agent = Agent(
    name="Support Agent",
    instructions="You are a customer support assistant who can help with order issues, returns, and FAQs."
    # ... (other parameters unchanged)
)

# Convert the specialized agents into tools by providing a name and description for each
shopping_tool = shopping_agent.as_tool(
    tool_name="shopping_assistant", 
    tool_description="Handle shopping-related queries (e.g. product recommendations, availability)."
)
support_tool = support_agent.as_tool(
    tool_name="customer_support", 
    tool_description="Handle customer support queries (e.g. returns, order status)."
)

# Create the triage/orchestrator agent that decides which tool (agent) to use
triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a triage agent. Determine if the user's request is about shopping or support, then use the appropriate tool to answer.",
    tools=[shopping_tool, support_tool]  # the triage agent can use the two agent-tools
)

# Run a sample query through the triage agent
result = Runner.run_sync(starting_agent=triage_agent, input="How do I track my order shipment?")
print(result.final_output)
