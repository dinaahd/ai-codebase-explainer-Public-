import streamlit as st
from openai import OpenAI
import os

# ---------- CONFIG ----------
st.set_page_config(
    page_title="AI Codebase Explainer",
    page_icon="💻",
    layout="wide"
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
# ---------- HEADER ----------
st.markdown("""
# 💻 AI Codebase Explainer  
### Understand any codebase instantly using AI
---
""")

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

# ---------- INPUT COLUMN ----------
with col1:
    st.subheader("📂 Input Code")

    uploaded_files = st.file_uploader(
        "Upload code files",
        type=["py", "java", "cpp", "js"],
        accept_multiple_files=True
    )

    code_input = ""

    if uploaded_files:
        for file in uploaded_files:
            code_input += f"\n\n# File: {file.name}\n"
            code_input += file.read().decode("utf-8")
    else:
        code_input = st.text_area("Paste your code here:", height=400)

# ---------- OUTPUT COLUMN ----------
with col2:
    st.subheader("📘 AI Output")

    if st.button("🚀 Explain Code"):
        if code_input:
            with st.spinner("Analyzing code..."):

                prompt = f"""
                You are a senior software engineer.

                Analyze this code and explain:

                1. What problem this code solves
                2. Step-by-step working
                3. Important functions and logic
                4. Possible improvements
                5. Time/space complexity (if applicable)

                Code:
                {code_input}
                """

                response = client.chat.completions.create(
                    model="meta-llama/llama-3.1-8b-instruct",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                st.success("Analysis Complete!")
                st.write(response.choices[0].message.content)

        else:
            st.warning("Please provide code.")

# ---------- Q&A SECTION ----------
st.markdown("## 💬 Ask Questions About Code")

question = st.text_input("Ask something about the code:")

if st.button("💡 Get Answer"):
    if code_input and question:
        with st.spinner("Thinking..."):

            prompt = f"""
            You are a helpful coding assistant.

            Answer the question based only on the code.

            Code:
            {code_input}

            Question:
            {question}
            """

            response = client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.write(response.choices[0].message.content)

    else:
        st.warning("Provide both code and a question.")