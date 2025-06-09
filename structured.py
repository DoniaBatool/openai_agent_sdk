from pydantic import BaseModel
from agents import Agent, Runner
import os
from dotenv import load_dotenv


load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    cooking_time: int # in minutes
    servings: int

recipe_agent = Agent(
    name="Recipe Agent", 
    instructions=("You are an agent for creating recipes. You will be given the name of a food and your job"
                  " is to output that as an actual detailed recipe. The cooking time should be in minutes."),
    output_type=Recipe
)

response = Runner.run_sync(recipe_agent, "Italian Sasuage with Spaghetti")
recipe = response.final_output