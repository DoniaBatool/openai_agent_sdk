import os
import chainlit as cl
from agents import Agent, RunConfig, OpenAIChatCompletionsModel, Runner, AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

run_config=RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

agent1=Agent(
    name="You are a helpful Assistant",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! I am a helpful assistant. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    result = await Runner.run(
        agent1,
        input=message.content,
        run_config=run_config,
    )
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()



 