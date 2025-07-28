from agents import Agent, Runner, RunContextWrapper, handoff
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# ─── Specialist agents ───────────────────────────────────────────────────────────
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

# ─── Callbacks ───────────────────────────────────────────────────────────────────
def on_math_handoff(ctx: RunContextWrapper[None]):
    print("🔔 Handing off to Math Tutor agent")

def on_history_handoff(ctx: RunContextWrapper[None]):
    print("🔔 Handing off to History Tutor agent")

# ─── 1) Input filter function ────────────────────────────────────────────────────
def filter_user_only(input_data):
    # HandoffInputData.messages mein ChatMessage objects hote hain
    contents = [m.content for m in input_data.messages]
    print("[InputFilter] Passing only these messages to child agent:", contents)
    # Sirf aakhri message rakho
    input_data.messages = input_data.messages[-1:]
    return input_data

# ─── 2) Handoff tools with input_filter ─────────────────────────────────────────
history_handoff_tool = handoff(
    history_tutor_agent,
    on_handoff=on_history_handoff,
    input_filter=filter_user_only
)
math_handoff_tool = handoff(
    math_tutor_agent,
    on_handoff=on_math_handoff,
    input_filter=filter_user_only
)

# ─── 3) Triage agent ─────────────────────────────────────────────────────────────
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You determine which agent to use based on the user's homework question. "
        "If neither agent is relevant, provide a general response."
    ),
    handoffs=[history_handoff_tool, math_handoff_tool]
)

# ─── 4) Run and observe ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Math question
    result = Runner.run_sync(triage_agent, "How do I add 2 and 2?")
    print("Final Output:", result.final_output)

    # History question
    result = Runner.run_sync(triage_agent, "How did WW2 start?")
    print("Final Output:", result.final_output)
