import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from state import AgentState

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)


def planner(state: AgentState):
    prompt = f"""
    You are a planning agent.

    Customer Question:
    {state['question']}

    Create a short plan to solve the customer's issue.
    """

    response = llm.invoke(prompt)

    return {"plan": response.content}


def researcher(state: AgentState):
    prompt = f"""
    You are a research agent.

    Customer Question:
    {state['question']}

    Plan:
    {state['plan']}

    Find the important information needed to answer.
    """

    response = llm.invoke(prompt)

    return {"research": response.content}


def writer(state: AgentState):
    prompt = f"""
    You are a professional customer support writer.

    Question:
    {state['question']}

    Research:
    {state['research']}

    Write a helpful, polite response.
    """

    response = llm.invoke(prompt)

    return {"draft": response.content}


def reviewer(state: AgentState):
    prompt = f"""
    Review this customer support response.

    Draft:
    {state['draft']}

    Improve grammar, clarity and professionalism.
    Return only the final response.
    """

    response = llm.invoke(prompt)

    return {"final_answer": response.content}