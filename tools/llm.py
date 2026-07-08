import os
import time
import logging

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

# --------------------------------------------------
# Gemini Models (Priority Order)
# --------------------------------------------------

MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite"
]

# --------------------------------------------------
# Fallback Content
# --------------------------------------------------

FALLBACK_RESPONSES = {

    "Executive Summary":
"""
The proposed AI chatbot solution aims to improve customer service by providing instant, accurate, and 24×7 assistance. It automates routine banking queries, reduces operational costs, improves customer satisfaction, and enables employees to focus on complex customer needs.
""",

    "Objectives":
"""
• Improve customer satisfaction

• Reduce response time

• Provide 24×7 customer support

• Reduce operational costs

• Increase business efficiency

• Automate repetitive customer queries
""",

    "Scope":
"""
The project includes:

• Requirement gathering

• System design

• AI chatbot development

• Banking system integration

• FAQ automation

• Testing

• Deployment

• Maintenance
""",

    "Technology Stack":
"""
• Python

• FastAPI

• Google Gemini API

• PostgreSQL

• React

• Docker

• AWS

• Redis
""",

    "Implementation Plan":
"""
Phase 1
Requirement Analysis

Phase 2
System Design

Phase 3
Development

Phase 4
Testing

Phase 5
Deployment

Phase 6
Maintenance
""",

    "Timeline":
"""
Month 1
Planning & Requirements

Month 2
Development

Month 3
Integration & Testing

Month 4
Deployment
""",

    "Budget":
"""
Development : ₹8 Lakhs

Infrastructure : ₹3 Lakhs

Testing : ₹2 Lakhs

Training : ₹1 Lakh

Maintenance : ₹1.5 Lakhs
""",

    "Conclusion":
"""
The proposed AI chatbot will improve customer experience, automate banking services, reduce operational costs, and provide a scalable AI-powered solution for future business growth.
"""
}


def fallback_response(task=None):

    if task is None:
        return "Content generation unavailable."

    return FALLBACK_RESPONSES.get(
        task.strip(),
        f"{task}\n\nContent generation unavailable."
    )


# --------------------------------------------------
# Gemini Wrapper
# --------------------------------------------------

class Gemini:

    def generate(self, prompt: str, task: str = None):

        last_error = None

        for model in MODELS:

            logging.info(f"Using model: {model}")

            for attempt in range(3):

                try:

                    logging.info(f"Attempt {attempt+1}/3")

                    response = client.models.generate_content(
                        model=model,
                        contents=prompt
                    )

                    if response and response.text:

                        text = response.text.strip()

                        # Remove Markdown formatting
                        text = (
                            text.replace("```markdown", "")
                                .replace("```", "")
                                .replace("###", "")
                                .replace("**", "")
                                .strip()
                        )

                        return text

                    raise Exception("Empty response from Gemini.")

                except ClientError as e:

                    error = str(e)

                    # Quota exhausted
                    if "429" in error or "RESOURCE_EXHAUSTED" in error:

                        logging.warning(f"{model} quota exhausted.")

                        last_error = e

                        # Try next model
                        break

                    # Server unavailable
                    elif "503" in error or "UNAVAILABLE" in error:

                        wait = 2 ** attempt

                        logging.warning(
                            f"Server busy. Waiting {wait} seconds..."
                        )

                        time.sleep(wait)

                        last_error = e

                    else:

                        logging.error(error)

                        last_error = e

                        break

                except Exception as e:

                    logging.error(e)

                    last_error = e

                    break

        # --------------------------------------------------

        logging.error("All Gemini models failed.")

        if last_error:
            logging.error(last_error)

        print("=" * 60)
        print("Using Fallback for:", task)
        print("=" * 60)

        return fallback_response(task)


gemini = Gemini()