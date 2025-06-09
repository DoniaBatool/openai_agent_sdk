from agents import Agent, Runner
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

class Tutorial(BaseModel):
    outline: str
    tutorial: str

tutorial_generator = Agent(
    name="Tutorial Generator",
    handoff_description="Used for generating a tutorial based on an outline.",
    instructions=(
        "Given a programming topic and an outline, your job is to generate code snippets for each section of the outline."
        "Format the tutorial in Markdown using a mix of text for explanation and code snippets for examples."
        "Where it makes sense, include comments in the code snippets to further explain the code."
    ),
    output_type=Tutorial
)

outline_builder = Agent(
    name="Outline Builder",
    instructions=(
        "Given a particular programming topic, your job is to help come up with a tutorial. You will do that by crafting an outline."
        "After making the outline, hand it to the tutorial generator agent."
    ),
    handoffs=[tutorial_generator]
)

tutorial_response = Runner.run_sync(outline_builder, "Loops in Java")
print(tutorial_response.final_output)