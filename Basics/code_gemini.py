import os
import chainlit as cl
from agents import Agent, RunConfig, OpenAIChatCompletionsModel, Runner, AsyncOpenAI, ModelSettings
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-1.5-flash",
)

run_config=RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=False,
)

agent1=Agent(
    name="You are a helpful Assistant",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    model_settings=ModelSettings(
        include_usage=False
    )
)

result=Runner.run_sync(agent1,"Who is the founder of Pakistan?",run_config=run_config)
print(result.final_output)