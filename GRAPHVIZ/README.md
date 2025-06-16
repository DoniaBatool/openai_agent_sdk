# GRAPHVIZ

The **GRAPHVIZ** folder contains examples related to visualizing agent workflows using Graphviz. These examples show how an agent’s decision process (like tool usage and message flow) can be rendered as a graph, which is helpful for debugging and understanding complex agent interactions.

-   **agent_flow.ipynb** – A Jupyter Notebook that generates a visualization of an agent’s flow. In this notebook, an agent is run on a sample task, and the notebook uses Graphviz (via the SDK’s visualization extension) to draw a directed graph of the agent’s reasoning steps. This could include nodes for the agent’s prompts, tool calls, and final answer, with arrows indicating the sequence. The interactive notebook likely explains each step, and then displays the resulting graph image for inspection.
    
-   **agent_flow.py** – A Python script version of the agent flow visualization. It runs a similar agent task as the notebook and programmatically produces a Graphviz graph (for example, outputting a `.gv` or image file). Running this script might output a file or open a window showing the graph of the agent’s decision path. This script is useful for generating a quick visualization without using Jupyter.
    

Using these examples, you can learn how to employ the `draw_graph` or related utilities from the Agents SDK. They demonstrate how an agent’s internal process (especially when tools and multiple steps are involved) can be externalized into a flowchart. This is particularly valuable for debugging multi-step agent logic or for presentations/documentation of how an AI agent operates.