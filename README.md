# Autonomous AI Agent

## Overview
A FastAPI-based autonomous AI agent that accepts natural language requests, creates an execution plan, generates structured business documents, and exports them as Microsoft Word (.docx) files.

## Features
- Autonomous task planning
- LLM integration (Gemini)
- Retry and fallback mechanism
- Word document generation
- FastAPI REST API
- Modular architecture

## Architecture
Planner → Executor → LLM → Document Generator

## Tech Stack
- Python
- FastAPI
- Google Gemini API
- python-docx
- dotenv

## API

POST /agent

Request:
{
  "request": "Create a business proposal for an AI chatbot."
}

Response:
{
  "status": "success",
  "document": "generated_docs/proposal.docx"
}

## Project Structure
agent/
tools/
generated_docs/
app.py
requirements.txt

## Future Improvements
- Memory
- RAG
- Tool calling
- Multi-agent workflow
