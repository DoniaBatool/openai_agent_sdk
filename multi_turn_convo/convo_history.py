from agents import Agent, Runner, TResponseInputItem
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

# 1. Agent banayein
mood_agent = Agent(
    name="MoodBot",
    instructions="You are a friendly bot , ask the user's mood and help accordingly."
)

# 2. Pehli conversation history
convo: list[TResponseInputItem] = [
    {"role": "user", "content": "Assalamualaikum!"}
     
]

# 3. Pehli run: greeting
result = Runner.run_sync(mood_agent, convo)
# result.final_output mein agent ka jawab hoga, aur
# result.to_input_list() se updated history milegi

# 4. Updated history nikal kar convo mein assign karein
convo = result.to_input_list()

# 5. Ab user kahe:
convo.append({"role": "user", "content": "Aaj mood kaisa hai aapka?"})

# 6. Dobara run
result =  Runner.run_sync(mood_agent, convo)

# 7. Phir se history update kijiye
convo = result.to_input_list()

# 8. Teesra turn:
convo.append({"role": "user", "content": "Mujhe thoda udaas lag raha hai."})
result = Runner.run_sync(mood_agent, convo)
print(result.to_input_list())
# 9. Final history aur agent ka jawab dekhein
#for msg in result.to_input_list():
    #print(msg)
