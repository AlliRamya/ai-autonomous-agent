# 🤖 Autonomous AI Agent for Business Document Generation

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Overview

This project is an **Autonomous AI Agent** that accepts a natural language request, plans its own execution steps, generates structured business content using an LLM, and exports the final result as a polished Microsoft Word document.

The project was built as part of a **Python AI Engineer – Autonomous Agents Assessment** to demonstrate:

- Autonomous Planning
- AI Reasoning
- LLM Integration
- Tool Orchestration
- Error Handling & Recovery
- REST API Development
- Automated Document Generation

---

# ✨ Features

✅ Accepts Natural Language Requests

✅ Autonomous Task Planning

✅ Dynamic Execution Pipeline

✅ Google Gemini LLM Integration

✅ Retry & Fallback Mechanism

✅ Microsoft Word (.docx) Generation

✅ FastAPI REST API

✅ Modular Project Structure

---

# 🏗 System Architecture

```
                   User Request
                         │
                         ▼
                FastAPI POST /agent
                         │
                         ▼
                  Planner Agent
                         │
             Generates Task List
                         │
                         ▼
                 Executor Agent
                         │
       Executes Tasks One-by-One
                         │
                         ▼
                 Gemini LLM API
                         │
         Generates Business Content
                         │
                         ▼
             Word Document Generator
                         │
                         ▼
               proposal.docx
                         │
                         ▼
                JSON API Response
```

---

# 🔄 Agent Workflow

```
User Request
      │
      ▼
Planner Agent
      │
      ▼
Task List Generation
      │
      ▼
Executor Agent
      │
      ▼
LLM Content Generation
      │
      ▼
Retry Logic
      │
      ▼
Fallback Response (if needed)
      │
      ▼
Document Generator
      │
      ▼
Generated Proposal (.docx)
```

---

# 📂 Project Structure

```
ai-autonomous-agent/
│
├── agent/
│   ├── planner.py
│   ├── executor.py
│   ├── prompts.py
│
├── tools/
│   ├── llm.py
│   ├── document.py
│
├── generated_docs/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| API | FastAPI |
| LLM | Google Gemini |
| Document Generation | python-docx |
| Configuration | dotenv |
| API Testing | Swagger UI |
| Logging | Python logging |

---

# 🧠 Autonomous Agent Design

The system follows a simple autonomous workflow.

### Step 1

Receive user request.

↓

### Step 2

Planner Agent analyzes the request.

↓

### Step 3

Planner creates its own TODO list.

↓

### Step 4

Executor processes each task.

↓

### Step 5

Gemini generates section-wise content.

↓

### Step 6

Retry logic handles temporary API failures.

↓

### Step 7

Fallback content is used if all retries fail.

↓

### Step 8

Document Generator creates the final Word document.

---

# 🚀 API

## POST

```
/agent
```

### Request

```json
{
    "request": "Create a proposal for an AI chatbot for a banking company."
}
```

---

### Response

```json
{
    "status": "success",
    "document": "generated_docs/proposal.docx"
}
```

---

# 📄 Example Output

The generated proposal contains:

- Executive Summary

- Objectives

- Scope

- Technology Stack

- Implementation Plan

- Timeline

- Budget

- Conclusion

---

# 🔁 Error Handling & Recovery

This project implements **Retry + Fallback Logic**.

If Gemini returns

- 429 (Quota Exceeded)

or

- 503 (Server Busy)

the system

- Retries automatically
- Switches between multiple Gemini models
- Uses predefined fallback responses if all models fail

This improves reliability and ensures uninterrupted document generation.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-autonomous-agent.git
```

Go to project folder

```bash
cd ai-autonomous-agent
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Sample Test Cases

## Test Case 1

```
Create a proposal for implementing an AI chatbot in a banking system.
```

---

## Test Case 2

```
Create a project plan for migrating a hospital's legacy software to a cloud-based AI-powered system with timeline, risks, assumptions, budget and recommendations.
```

---

# 📈 Future Improvements

- Conversation Memory

- RAG Integration

- Multi-Agent Workflow

- Tool Calling

- Reflection Agent

- Human-in-the-loop Approval

- Vector Database

- Streaming Responses

- Docker Deployment

- CI/CD Pipeline

---

# 🎯 Assessment Objectives Covered

✔ Autonomous Planning

✔ Python Development

✔ FastAPI API Design

✔ Tool Orchestration

✔ LLM Integration

✔ Error Handling

✔ Business Document Generation

✔ Software Engineering Principles

✔ Modular Architecture

---

# 👩‍💻 Author

**Alli Ramya**

AI / ML Engineer

Python | FastAPI | LLMs | Autonomous Agents | Generative AI

GitHub: https://github.com/YOUR_USERNAME

---

## ⭐ If you found this project useful, consider giving it a Star.
## Future Improvements
- Memory
- RAG
- Tool calling
- Multi-agent workflow
