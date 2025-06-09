import streamlit as st
from agents import Agent, Runner
from agents.extensions.visualization import draw_graph
import os
from dotenv import load_dotenv
import graphviz

# Step 1: Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY is not set in the environment variables.")
    st.stop()

# Step 2: Streamlit UI
st.title("🧠 Agentic Haiku Generator")
st.markdown("Enter a prompt for the agent. It will respond and show the internal workflow graph.")

# Step 3: Prompt Input
prompt = st.text_input("📝 Enter a prompt:", "Write a haiku about recursion in programming.")

# Step 4: Run agent on submit
if st.button("🚀 Run Agent"):
    with st.spinner("Running agent..."):
        agent = Agent(name="Assistant", instructions="You are a helpful assistant")
        result = Runner.run_sync(agent, prompt)
        
        st.subheader("🧾 Agent Output")
        st.success(result.final_output)

        st.subheader("🔍 Agent Graph")
        dot = draw_graph(agent, return_dot=True)  # get the dot object
        st.graphviz_chart(str(dot))  # Render using Streamlit's Graphviz
