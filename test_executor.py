from agent.planner import planner
from agent.executor import executor

request = "Create a proposal for an AI chatbot for a bank."

plan = planner.create_plan(request)

document = executor.execute(
    request,
    plan["tasks"]
)

print(document)