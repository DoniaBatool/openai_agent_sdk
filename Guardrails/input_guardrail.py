from agents import (
    Agent,
    Runner,
    input_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
)

import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# Simple input guardrail: input should not contain the word-- “forbidden” 
@input_guardrail(name="no_forbidden_word")
def no_forbidden(ctx, agent, user_input: str) -> GuardrailFunctionOutput:
    if "forbidden" in user_input.lower():
        return GuardrailFunctionOutput(
            output_info="Found forbidden word",
            tripwire_triggered=True,
        )
    return GuardrailFunctionOutput(
        output_info="All good",
        tripwire_triggered=False,
    )

# Agent that will run in parallel with the input_guardrail
agent = Agent(
    name="SimpleEcho",
    instructions="Echo the input back.",
    input_guardrails=[no_forbidden],
)

# Test 
for text in ["Hello world", "This has a forbidden word"]:
    print(f"\nInput: {text}")
    try:
        out = Runner.run_sync(agent, text)
        print("✅ Response:", out.final_output)
    except InputGuardrailTripwireTriggered as e:
        # IN e.guardrail_result we have this InputGuardrailResult 
        res = e.guardrail_result
        print("🚫 INPUT Guardrail:", res.guardrail)
        print("🚫 Input Guardrail Result:", res.output)
        print("🚫 Guardrail Name:", res.guardrail.name)
        print("   reason/Info:", res.output.output_info)
        print("   tripwire TRIGGERED:", res.output.tripwire_triggered)

