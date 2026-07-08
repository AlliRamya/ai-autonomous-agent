import json

from tools.llm import gemini
from agent.prompts import planner_prompt


class Planner:

    def create_plan(self, request, previous_context=None):

        if previous_context is None:
            previous_context = []

        # Create planning prompt
        prompt = planner_prompt(
            request,
            previous_context
        )

        # Ask Gemini
        response = gemini.generate(prompt)

        # Clean markdown
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:

            plan = json.loads(response)

            return plan

        except Exception as e:

            print("Planner JSON Error:", e)
            print(response)

            # Fallback plan
            return {
                "document_type": "Proposal",
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


planner = Planner()