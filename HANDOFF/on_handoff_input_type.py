from pydantic import BaseModel
from agents import Agent, Runner,RunContextWrapper,handoff, function_tool
import os
from dotenv import load_dotenv
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")


class ManagerEscalation(BaseModel):
    issue: str # the issue being escalated
    why: str # why can you not handle it? Used for training in the future

@function_tool
def create_ticket(issue: str):
    """"
    Create a ticket in the system for an issue to be resolved.
    """
    print(f"Creating ticket for issue: {issue}")
    return "Ticket created. ID: 12345"
    # In a real-world scenario, this would interact with a ticketing system

manager_agent = Agent(
    name="Manager",
    handoff_description="Handles escalated issues that require managerial attention",
    instructions=f"""
        You handle escalated customer issues that the initial custom service agent could not resolve. 
        You will receive the issue and the reason for escalation. If the issue cannot be immediately resolved for the 
        customer, create a ticket in the system and inform the customer.
    """,
    tools=[create_ticket],
)

def on_manager_handoff(ctx: RunContextWrapper[None], input: ManagerEscalation):
    print("Escalating to manager agent: ", input.issue)
    print("Reason for escalation: ", input.why)

    # here we might store the escalation in a database or log it for future reference

customer_service_agent = Agent(
    name="Customer Service",
    instructions="You assist customers with general inquiries and basic troubleshooting. " +
                 "If the issue cannot be resolved, escalate it to the Manager along with the reason why you cannot fix the issue yourself.",
    handoffs=[handoff(
        agent=manager_agent,
        input_type=ManagerEscalation,
        on_handoff=on_manager_handoff,
    )]
)

result =  Runner.run_sync(customer_service_agent, "I have the issue with the tickets i have bought, can you redirect me to the manager?")
print(result.final_output)

#from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

#manager_agent = Agent(
    #name="Manager",
  
    #instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
        #You handle escalated customer issues that the initial custom service agent could not resolve. 
        #You will receive the issue and the reason for escalation. If the issue cannot be immediately resolved for the 
        #customer, create a ticket in the system and inform the customer.
   # """,
   # tools=[create_ticket],
#)

#another test prompt:
#how much is the ticket for dolphin show?