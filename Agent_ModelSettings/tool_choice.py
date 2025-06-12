from agents import Agent, Runner, ModelSettings,function_tool
import os
from dotenv import load_dotenv


load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

settings_auto = ModelSettings(tool_choice='auto')
settings_required = ModelSettings(tool_choice='required')
settings_none = ModelSettings(tool_choice='none') 

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny and warm."   # Dummy output

agent = Agent(
    name="WeatherBot",
    instructions="Give weather info using the tool if appropriate.",
    tools=[get_weather],
    model="gpt-4o",
    model_settings=settings_required
)

result = Runner.run_sync(agent, "What is your favourite weather?") 
#"What is the weather of Karachi?"What is your favourite weather?
print(result.final_output)