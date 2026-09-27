import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from state import AgentState

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)


# -------------------------
# Planner Agent
# -------------------------
def planner(state: AgentState):
    history = "\n".join(
        [f"{type(m).__name__}: {m.content}" for m in state["messages"][-10:]]
    )

    prompt = f"""
You are a planning agent.

Conversation History:
{history}

Current User Question:
{state['question']}

Identify the customer's intent in one sentence.
"""

    response = llm.invoke(prompt)

    return {
        "plan": response.content,
        "messages": [HumanMessage(content=state["question"])]
    }


# -------------------------
# Research Agent
# -------------------------
def researcher(state: AgentState):
    prompt = f"""
You are a customer support researcher.

Plan:
{state['plan']}

Customer Question:
{state['question']}

Provide useful information that should appear in the reply.
"""

    response = llm.invoke(prompt)

    return {"research": response.content}


# -------------------------
# Writer Agent
# -------------------------
def writer(state: AgentState):
    prompt = f"""
Write a professional customer support response.

Research:
{state['research']}

Question:
{state['question']}
"""

    response = llm.invoke(prompt)

    return {"draft": response.content}


# -------------------------
# Reviewer Agent
# -------------------------
def reviewer(state: AgentState):
    prompt = f"""
Improve this response for clarity, grammar and professionalism.

Draft:
{state['draft']}
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content,
        "messages": [AIMessage(content=response.content)]
    }