from langgraph.graph import StateGraph, END

from state import AgentState
from agents import planner, researcher, writer, reviewer

# Create Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("planner", planner)
workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)
workflow.add_node("reviewer", reviewer)

# Entry Point
workflow.set_entry_point("planner")

# Connect Nodes
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "reviewer")
workflow.add_edge("reviewer", END)

# Compile Graph
app = workflow.compile()