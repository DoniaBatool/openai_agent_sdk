from agents import (
    Agent,
    Runner,
    RunContextWrapper,
    output_guardrail,                # Due to decorator the function will be wrapped in OutputGuardrail 
    GuardrailFunctionOutput,         # guardrail function's return type
    OutputGuardrailTripwireTriggered # if tripwire=true then exception will be raised
)
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# 2) Pydantic model for detailed guardrail output info
class PolitenessCheckOutput(BaseModel):
    is_polite: bool    # it will check if the response has "please" in it
    message: str       # if impolite, what output should be given to the user?

# 3) Output guardrail define karna: ensure agent ki response me "please" shamil ho
@output_guardrail(name="politeness_check")
def polite_guard(
    ctx: RunContextWrapper[None],  # run context (memory/session waghera)
    agent: Agent,                  # Agent instance
    agent_output: str              # Agent's generated output text
) -> GuardrailFunctionOutput:
    """
    This guardrail will check if the agent response contains the word 'please',
    otherwise tripwire will be triggered .
    """
    found = "please" in agent_output.lower()
    return GuardrailFunctionOutput(
        output_info=PolitenessCheckOutput(
            is_polite=found,
            message=(
                "Politeness OK."
                if found
                else "Response not polite enough—include 'please'."
            )
        ),
        tripwire_triggered=not found
    )

# 4) Agent create karna aur output guardrail attach karna
agent = Agent(
    name="PoliteAgent",
    instructions="if the user's request contains the word 'please', handle it politely using the word 'please', " \
    "otherwiswe don't include the word 'please'.",
    output_guardrails=[polite_guard],  
)

# 5) Test inputs: 1-impolite, 2- polite
tests = [
    "Give me the status update.",               # impolite
    "Please give me the status update.",        # polite
]

# 6) Runner.run to check the result or exception
for req in tests:
    print(f"\nRequest: {req}")
    try:
        res = Runner.run_sync(agent, req)
        # if you get this response then the input was polite
        print("✅ Agent response:", res.output_guardrail_results)
    except OutputGuardrailTripwireTriggered as e:
        # exception e.guardrail_result contains OutputGuardrailResult object
        result = e.guardrail_result
        info: PolitenessCheckOutput = result.output.output_info
        print("🚫 Guardrail failed:", result.guardrail.name)
        print("  🚫 Details:", info.message)
        print("  🚫 guardrail:", result.agent)
        print(" 🚫  guardrail:", result.agent_output)
        print("  🚫 guardrail:", result.output)#from this output we can further get output_info and tripwire_triggered
        print("  🚫 guardrail:", result.guardrail)
        print("  🚫 guardrail:", result.output.tripwire_triggered)
   
