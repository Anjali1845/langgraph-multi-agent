# 🤖 LangGraph Multi-Agent Customer Support AI

A production-style **Multi-Agent Customer Support Assistant** built using **LangGraph, LangChain, Google Gemini, and Streamlit**. The system simulates how multiple AI agents collaborate to understand customer issues, research solutions, draft responses, and review them before delivering a polished final answer.

---

## 🚀 Demo

This project accepts customer support queries such as:

> *"I paid twice for my internship fee. What should I do?"*

The workflow automatically generates a professional customer support response through four specialized AI agents.

---

## ✨ Features

* 🧠 Multi-Agent architecture using LangGraph
* 📋 Planner agent analyzes customer intent
* 🔍 Researcher agent gathers relevant information
* ✍️ Writer agent drafts a professional response
* ✅ Reviewer agent improves grammar, tone & clarity
* 🎨 Clean Streamlit web interface
* ⚡ Powered by Google Gemini LLM

---

## 🏗️ Architecture

`Customer Query`

⬇

**🧠 Planner**

Understands the issue & creates a response strategy

⬇

**🔍 Researcher**

Collects support policies & required details

⬇

**✍️ Writer**

Creates the first customer support email

⬇

**✅ Reviewer**

Polishes the response and returns the final answer

---

## 🛠️ Tech Stack

* Python 3.12
* LangGraph
* LangChain
* Google Gemini API
* Streamlit
* python-dotenv

---

## 📂 Project Structure

```text
langgraph-multi-agent/
│
├── app.py              # Streamlit UI
├── graph.py            # LangGraph workflow
├── agents.py           # Planner, Researcher, Writer, Reviewer
├── state.py            # Shared state schema
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Anjali1845/langgraph-multi-agent.git
cd langgraph-multi-agent
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Query

```text
My name is Anjali.
I paid twice for my internship fee.
```

The application generates a complete customer support email including refund guidance, required documents, ticket reference, and professionally reviewed communication.

---

## 🎯 Learning Outcomes

Through this project I learned:

* Building Multi-Agent workflows using LangGraph
* Designing AI agent collaboration pipelines
* Managing shared state across agents
* Integrating Gemini with LangChain
* Creating interactive AI applications using Streamlit
* Structuring production-ready Python projects

---

## 👩‍💻 Author

**Moka Anjali**

B.Tech CSE (AI & ML)

GitHub: **@Anjali1845**

---

## ⭐ Future Improvements

* Conversation memory
* Knowledge base (RAG + FAISS)
* PDF policy retrieval
* Ticket generation
* Email integration
* Human-in-the-loop approval
