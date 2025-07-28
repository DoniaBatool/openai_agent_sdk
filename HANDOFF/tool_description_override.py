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

# ─── Handoff tools with description override ──────────────────────────────────────
history_handoff_tool = handoff(
    history_tutor_agent,
    on_handoff=on_history_handoff,
    tool_description_override="Transfer this question to the History Tutor for detailed context and timelines."
)

math_handoff_tool = handoff(
    math_tutor_agent,
    on_handoff=on_math_handoff,
    tool_description_override="Transfer this question to the Math Tutor for step by step solution and examples."
)

# ─── Triage agent ─────────────────────────────────────────────────────────────────
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You determine which agent to use based on the user's homework question. "
        "If neither agent is relevant, provide a general response."
    ),
    handoffs=[history_handoff_tool, math_handoff_tool]
)

# ─── Run examples ────────────────────────────────────────────────────────────────
result = Runner.run_sync(triage_agent, "How do I add 2 and 2?")
print("Math query output:", result.final_output)

result = Runner.run_sync(triage_agent, "How did WW2 start?")
print("History query output:", result.final_output)
