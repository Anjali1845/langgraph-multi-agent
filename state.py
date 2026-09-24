from typing import TypedDict

class AgentState(TypedDict):
    question: str
    plan: str
    research: str
    draft: str
    final_answer: str