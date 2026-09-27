from typing import TypedDict, List
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # Current user input
    question: str

    # Shared conversation memory
    messages: Annotated[List[BaseMessage], add_messages]

    # Outputs from each agent
    plan: str
    research: str
    draft: str
    final_answer: str