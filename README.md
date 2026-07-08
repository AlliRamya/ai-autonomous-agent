# 🤖 Autonomous AI Agent for Business Document Generation

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Overview

This project implements an **Autonomous AI Agent** capable of understanding natural language requests, planning its own execution strategy, executing tasks autonomously, generating structured business content using a Large Language Model (LLM), and exporting the final result as a professionally formatted Microsoft Word (.docx) document.

The system demonstrates modern AI engineering concepts including:

- Autonomous Task Planning
- AI Reasoning
- LLM Integration
- Tool Orchestration
- Retry & Fallback Logic
- REST API Development
- Automated Document Generation
- Modular Software Architecture

---

# ✨ Features

✅ Accepts Natural Language Requests

✅ Autonomous Task Planning

✅ Multi-step Execution Pipeline

✅ Google Gemini LLM Integration

✅ Retry & Fallback Mechanism

✅ Microsoft Word (.docx) Generation

✅ FastAPI REST API

✅ Modular Agent-Based Architecture

✅ Configurable Prompt Templates

---

# 🏗 System Architecture

> Replace the image below with your architecture diagram.

![Architecture](screenshots/architecture.png)

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

# 🤖 Agent Workflow

```
User Request
      │
      ▼
Planner Agent
      │
      ▼
Task Planning
      │
      ▼
Executor Agent
      │
      ▼
LLM Content Generation
      │
      ▼
Retry & Recovery Logic
      │
      ▼
Fallback Content (if required)
      │
      ▼
Document Generator
      │
      ▼
Generated Proposal (.docx)
```

---

# 🧩 Architecture Components

## Planner Agent

- Receives the user's request.
- Analyzes the business requirement.
- Creates its own execution plan.
- Generates a structured task list.

---

## Executor Agent

- Executes every task sequentially.
- Invokes the LLM for content generation.
- Collects generated content.
- Passes results to the document generator.

---

## LLM Module

- Uses Google Gemini.
- Generates business-quality content.
- Handles retry logic.
- Supports fallback responses.

---

## Document Generator

- Formats the generated content.
- Creates a professional Microsoft Word (.docx) document.
- Saves the generated proposal.

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
| Language | Python 3.11 |
| API Framework | FastAPI |
| LLM | Google Gemini |
| Document Generation | python-docx |
| Configuration | python-dotenv |
| API Testing | Swagger UI |
| Logging | Python Logging |

---

# 💡 Engineering Decisions

Instead of generating the entire document in a single LLM request, the system generates each section independently.

This approach provides:

- Better modularity
- Easier debugging
- Reduced prompt complexity
- Improved maintainability
- Easier future integration with RAG and external tools

---

# 🔌 API

## Endpoint

```
POST /agent
```

---

### Request

```json
{
    "request": "Create a proposal for implementing an AI chatbot for a banking company."
}
```

---

### Response

```json
{
    "status": "success",
    "message": "Document generated successfully.",
    "document": "generated_docs/proposal.docx",
    "tasks": [
        "Executive Summary",
        "Objectives",
        "Scope",
        "Technology Stack",
        "Implementation Plan",
        "Timeline",
        "Budget",
        "Conclusion"
    ]
}
```

---

# 📄 Example Output

The generated Microsoft Word document contains:

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

The project implements a robust **Retry + Fallback** mechanism.

If Gemini returns:

- HTTP 429 (Rate Limit)
- HTTP 503 (Service Unavailable)

the system automatically:

- Retries failed requests
- Switches between multiple Gemini models
- Uses predefined fallback responses when necessary

This ensures reliable document generation even during temporary API failures.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-autonomous-agent.git
```

Navigate to the project directory

```bash
cd ai-autonomous-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

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

Open Swagger UI

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
Create a project plan for migrating a hospital's legacy software to a cloud-based AI-powered system with timeline, risks, assumptions, budget, and recommendations.
```

---

# 🎯 Key Highlights

✔ Autonomous Planning

✔ AI Reasoning

✔ LLM Integration

✔ FastAPI REST API

✔ Tool Orchestration

✔ Retry & Recovery Logic

✔ Automated Business Document Generation

✔ Modular Software Architecture

---

# 🚀 Future Improvements

- Conversation Memory
- Retrieval-Augmented Generation (RAG)
- Tool Calling
- Multi-Agent Collaboration
- Reflection / Self-Evaluation Agent
- Human-in-the-loop Approval
- Vector Database Integration
- Streaming Responses
- Docker Support
- CI/CD Pipeline
- Cloud Deployment (AWS/Azure)

---

## ⭐ If you found this project useful, consider giving it a Star.
