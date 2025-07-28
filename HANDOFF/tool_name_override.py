from agents import Agent, Runner, RunContextWrapper, handoff
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# 1) Specialist agents define karte hain
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

# 2) on_handoff callbacks
def on_math_handoff(ctx: RunContextWrapper[None]):
    print("Handing off to math tutor agent")

def on_history_handoff(ctx: RunContextWrapper[None]):
    print("Handing off to history tutor agent")

# 3) handoff tools banate hue tool_name_override set karna
history_handoff_tool = handoff(
    history_tutor_agent,
    on_handoff=on_history_handoff,
    tool_name_override="ask_history_expert"        # custom tool name for history
)

math_handoff_tool = handoff(
    math_tutor_agent,
    on_handoff=on_math_handoff,
    tool_name_override="ask_math_expert"           # custom tool name for math
)

# 4) Triage agent jis mein dono handoff tools attach hon
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You determine which agent to use based on the user's homework question. "
        "If neither agent is relevant, provide a general response."
    ),
    handoffs=[history_handoff_tool, math_handoff_tool]
)

# 5) Runner se sync run karke dekhen
result = Runner.run_sync(triage_agent, "How do I add 2 and 2?")
print("Output:", result.new_items)
# Aap console mein dekhenge: 
#   • Pehle “ask_math_expert” tool call hui
#   • Phir on_math_handoff print hoga
#   • Aur Math Tutor ka jawab return hoga

#result = Runner.run_sync(triage_agent, "How did WW2 start?")
#print("Output:", result.final_output)
# Ab “ask_history_expert” tool call hogi, on_history_handoff print hoga, 
# phir History Tutor ka jawab return hoga
