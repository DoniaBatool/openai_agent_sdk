from agents import Agent, Runner
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# --- Specialist agents ---

eye_specialist = Agent(
    name="Eye Specialist",
    instructions="You are an eye specialist. Answer medical queries about eyes, vision, eye diseases, treatments, and eye care only.",
    handoff_description="Handles all eye/vision related medical questions."
)

dentist = Agent(
    name="Dentist",
    instructions="You are a dentist. Answer medical queries about teeth, gums, dental problems, treatments, and oral care only.",
    handoff_description="Handles all teeth, gum, and oral health related questions."
)

# --- Triage agent ---

triage_agent = Agent(
    name="Medical Triage Agent",
    instructions=(
        "You are a medical triage assistant. When a user asks a question, "
        "identify if it relates to eyes/vision or teeth/oral health. "
        "If it is about eyes or vision, handoff to the Eye Specialist agent. "
        "If it is about teeth, gums, or mouth, handoff to the Dentist agent. "
        "If it's unclear, politely ask the user for more details about which body part they need help with."
    ),
    handoffs=[eye_specialist, dentist]
)

# --- Example run ---

user_query = input("Enter your medical question (e.g., 'What causes red eyes?' or 'How to treat a toothache?'): ")

result = Runner.run_sync(triage_agent, user_query)
print(result.final_output)
