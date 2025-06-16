# OpenAI Agents SDK Examples and Patterns

*This repository provides a **living collection** of practical examples and patterns for using the OpenAI Agents SDK. It includes hands-on Python scripts and notebooks demonstrating agentic workflows such as multi-agent coordination (triage/handoff), tool integration, structured data exchange, and execution tracing.*

## Target Audience

This project is geared towards developers, AI practitioners, and researchers interested in learning the OpenAI Agents SDK through code examples. Familiarity with Python and basic LLM concepts is expected. Beginners can start with the simple demos in the **Basics/** folder, while experienced users can explore advanced patterns like multi-agent handoffs and custom tool usage. Overall, the examples aim to help both newcomers and seasoned AI engineers build and experiment with agentic workflows.

## Live and Evolving Project Notice

The repository is a **live, evolving resource**. As the OpenAI Agents SDK grows and new features are released, the author regularly adds new examples and experiments. Users are encouraged to check back for updates. Feel free to suggest ideas or contribute new examples via issues and pull requests.

## Features

- **Modular Examples:** Each concept or pattern is implemented in its own script or notebook (for instance, a `handoff3.py` script for escalation flows or `structured.py` for structured outputs).
- **Multi-Agent Handoffs:** Demos of agents delegating or escalating tasks to other agents, showcasing triage/coordinator agent patterns.
- **Agent-as-Tool:** Examples where one agent is invoked as a tool by another agent, illustrating recursive agent usage.
- **Structured I/O:** Use of Pydantic models and structured schemas to enforce reliable JSON-like inputs and outputs.
- **Hosted Tools:** Integration of external APIs or web-based tools (e.g. search, computation services) as agent tools.
- **Tool-Forcing Patterns:** Techniques to guide an agent to use specific tools or handle inputs in a predetermined way.
- **Tracing and Debugging:** Step-by-step tracing examples to inspect agent reasoning and debug workflows.
- **Workflow Visualizations:** UML/Graphviz diagrams in the `GRAPHVIZ/` folder that illustrate the logic and flow of agent interactions.
- **Chainlit UI (Optional):** Some examples support [Chainlit](https://chainlit.io) for an interactive user interface (see `chainlit.md` for setup instructions).

## Installation and Prerequisites

Ensure you have **Python 3.8 or higher** installed. You will also need an OpenAI API key. Perform the following steps in a terminal:

```bash
# Clone the repository
git clone https://github.com/DoniaBatool/openai_agent_sdk.git
cd openai_agent_sdk

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows use: .\venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt


# Create a `.env` file in the project root with your OpenAI API key, for example:


`OPENAI_API_KEY=sk-...` 

# Make sure to keep this key secure (the repository uses `.gitignore` to exclude it).

## Usage

After installation, you can run the example scripts directly. For instance, to run a basic agent example:

`python basics/hello.py` 

This will start a simple "Hello Agent" demo. Other scripts are named by their purpose (e.g. files in `HANDOFF/` demonstrate handoff flows, `Structured_INP_OUT/` shows structured output, etc.). Alternatively, if you have the provided CLI tools installed, you can use:

`uv run basics/hello.py` 

which sets up the environment and executes the script.

# Some examples are Jupyter notebooks (`.ipynb`) for interactive exploration. You can open them with:

`jupyter notebook` 

and then run the cells.

Optionally, for a richer interface, install [Chainlit](https://chainlit.io) and run Chainlit-enabled examples with:

`chainlit run basics/hello.py`

```


## Repository Structure Overview

Each folder groups related examples and materials:

-   `Basics/` – Core examples (e.g., a simple "hello world" agent).
    
-   `Agent_ModelSettings/` – Examples configuring `Agent` and `ModelSettings` for custom behavior.
    
-   `Agent_as_tool/` – Demonstrations of using one agent as a tool for another.
    
-   `Function_Tools/` – Using standalone Python functions or scripts as agent tools.
    
-   `HANDOFF/` – Multi-agent coordination examples with handoff and escalation patterns.
    
-   `HOSTED_TOOLS/` – Integration with external or hosted APIs/services as agent tools.
    
-   `Structured_INP_OUT/` – Enforcing structured inputs/outputs (e.g. via Pydantic models).
    
-   `Tracing/` – Showcasing the built-in tracing of agent execution for debugging.
    
-   `GRAPHVIZ/` – PlantUML or Graphviz diagrams illustrating agent workflows.
    
-   `agentic_patterns/` – Additional agentic design patterns and orchestrations.
    
-   `Documentation/` – Detailed documents and PDFs explaining concepts and usage.
    
-   `chainlit.md` – Instructions for using Chainlit with the examples.
    
-   Root files: e.g., `hello.py` (a minimal agent script), `requirements.txt`, etc.

## Credits

**Author:** Donia Batool (GitHub). This repository and its content are licensed under the MIT License.

## Call to Action

If you find this repository useful, please **⭐ star it on GitHub** and consider sharing it with others. Contributions are very welcome – feel free to open issues or submit pull requests with new examples and ideas. Together, we can build a robust set of agentic AI patterns and workflows[medium.com](https://medium.com/@donia1510aptech/diving-into-openai-agents-sdk-building-a-living-repository-of-examples-4f180cd0f04c#:~:text=Call%20to%20Action%3A).