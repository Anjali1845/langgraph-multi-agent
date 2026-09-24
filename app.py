import streamlit as st
from graph import app

st.set_page_config(
    page_title="LangGraph Multi-Agent AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LangGraph Multi-Agent AI")
st.caption("Planner → Researcher → Writer → Reviewer")

st.divider()

question = st.text_area(
    "Ask your customer support question",
    placeholder="Example: I paid twice for my internship. How do I get a refund?"
)

if st.button("Generate Response", use_container_width=True):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("All agents are collaborating..."):

            result = app.invoke({
                "question": question,
                "plan": "",
                "research": "",
                "draft": "",
                "final_answer": ""
            })

        st.success("Workflow Completed ✅")

        with st.expander("🧠 Planner"):
            st.write(result["plan"])

        with st.expander("🔍 Researcher"):
            st.write(result["research"])

        with st.expander("✍️ Writer"):
            st.write(result["draft"])

        st.subheader("✅ Final Answer")
        st.write(result["final_answer"])