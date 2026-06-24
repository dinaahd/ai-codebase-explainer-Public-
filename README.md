# 💻 AI Codebase Explainer  
### 🚀 Understand any codebase instantly using AI

---

## 🧠 Overview

AI Codebase Explainer is a Gen AI-powered tool that helps developers quickly understand unfamiliar codebases using Large Language Models (LLMs).

It provides structured explanations and allows interactive questioning, acting like a **developer copilot**.

---

## 🚀 Features

- 📂 Upload or paste code  
- 📁 Multi-file support (simulate repository understanding)  
- 📘 AI-generated structured explanations  
- 💬 Ask questions about the code (interactive Q&A)  
- ⚡ Clean and responsive UI using Streamlit  

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **AI Model:** LLM via OpenRouter API (LLaMA 3.1)  
- **Tools:** Git, GitHub  

---

## ⚙️ Installation & Setup

### 1. Clone the repository

bash

git clone https://github.com/dinaahd/ai-codebase-explainer.git

cd ai-codebase-explainer

### 2. Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

##3. Install dependencies
pip install -r requirements.txt

### 4. Set API Key

Windows

setx OPENROUTER_API_KEY "your_api_key"

Mac/Linux

export OPENROUTER_API_KEY="your_api_key"

### 5. Run the application

streamlit run app.py

---

## 💡 Use Cases

- Understand unfamiliar codebases quickly
- Assist beginners in learning programming
- Improve developer productivity
- Analyze and debug logic efficiently

---
## 🔮 Future Improvements

🔗 GitHub repository integration

📊 Code visualization (flow diagrams)

💾 Chat history and memory

🌐 Support for more programming languages

---

## 👩‍💻 Author

Dina Ahd

🔗 GitHub: https://github.com/dinaahd

💼 LinkedIn: www.linkedin.com/in/dina-ahd

---

## ⭐ Acknowledgements

OpenRouter for LLM API access

Streamlit for rapid UI development

---
