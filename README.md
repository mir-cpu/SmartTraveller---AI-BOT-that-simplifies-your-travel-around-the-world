# 🤖 LangChain Conversational Chatbot

A conversational AI chatbot built using **LangChain**, **OpenAI**, and **Streamlit**, featuring **conversation buffer memory** to maintain chat context across interactions.

This project demonstrates how to build a modern GenAI-powered chatbot with memory, clean architecture, and a simple web UI.

---

## ✨ Features

* 💬 Conversational chatbot using LangChain
* 🧠 Conversation Buffer Memory (remembers previous messages)
* ⚡ Powered by OpenAI chat models
* 🌐 Interactive UI built with Streamlit
* 🔐 Secure API key handling using environment variables
* 🧩 Modular and easy-to-extend codebase

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **LangChain**
* **OpenAI**
* **Streamlit**
* **dotenv** (for environment variables)

---

## 📂 Project Structure

```
chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files (venv, secrets, cache)
├── .env.example           # Example environment variables
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/langchain-chatbot.git
cd langchain-chatbot
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

> ⚠️ Never commit `.env` files to GitHub.

---

### 5️⃣ Run the Application

```bash
streamlit 
```
