from fastapi import FastAPI
from pydantic import BaseModel

from agent.orchestrator import agent

app = FastAPI(
    title="Autonomous AI Agent",
    version="1.0.0",
    description="AI Agent capable of planning, executing tasks, reflecting, and generating Word documents."
)


class AgentRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent is running."
    }


@app.post("/agent")
def run_agent(request: AgentRequest):
    return agent.run(request.request)