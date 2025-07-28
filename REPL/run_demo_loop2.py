import asyncio
from agents import Agent, run_demo_loop, Handoff, InputGuardrail, OutputGuardrail,FunctionTool

# 1) Define a simple tool
@FunctionTool
def echo_tool(ctx, text: str) -> str:
    return f"Echo: {text}"

# 2) Define guardrails
class LengthGuard(InputGuardrail):
    def validate(self, ctx, item):
        if len(item.content) > 100:
            return False, "Input too long"
        return True, None

# 3) Create a specialist agent for shouting
shout_agent = Agent(
    name="ShoutAgent",
    instructions="Respond in uppercase."
)

# 4) Main agent with tool, handoff, and guardrails
agent = Agent(
    name="Helper",
    instructions="Use the echo tool or handoff to shout.",
    tools=[echo_tool],
    handoffs=[shout_agent],
    input_guardrails=[LengthGuard()],
    output_guardrails=[OutputGuardrail()],  # built-in check
    output_type=str,
)

# 5) Run REPL without streaming
async def main():
    await run_demo_loop(agent, stream=False)

if __name__ == "__main__":
    asyncio.run(main())
