import asyncio
from dataclasses import dataclass
from typing import Literal
from agents import Agent, Runner

# Story outline generator agent
story_maker = Agent(
    name="StoryMaker",
    instructions="Create a very short story outline from the user’s input. Use feedback to improve if any."
)

# Judge agent (with output_type so it returns feedback + score)
@dataclass
class JudgeFeedback:
    feedback: str
    score: Literal["pass", "fail"]

judge = Agent(
    name="Judge",
    instructions="Judge the outline. If it’s not good, give feedback. Never pass on the first try.",
    output_type=JudgeFeedback
)

async def main():
    user_input = input("What kind of story do you want? ")
    outline_input = user_input
    feedback = ""

    while True:
        # StoryMaker agent creates outline
        outline_result = await Runner.run(story_maker, f"{outline_input}\n{feedback}" if feedback else outline_input)
        outline = outline_result.final_output
        print(f"Outline: {outline}")

        # Judge agent gives feedback
        judge_result = await Runner.run(judge, outline)
        judge_out = judge_result.final_output
        print(f"Judge: {judge_out.score}, Feedback: {judge_out.feedback}")

        if judge_out.score == "pass":
            break
        feedback = judge_out.feedback  # Use feedback in next loop

    print("\nFinal approved outline:")
    print(outline)

if __name__ == "__main__":
    asyncio.run(main())
