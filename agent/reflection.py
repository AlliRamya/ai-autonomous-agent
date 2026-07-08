from tools.llm import gemini
from agent.prompts import reflection_prompt


class Reflection:

    def review(self, document):

        prompt = reflection_prompt(document)

        return gemini.generate(prompt)


reflection = Reflection()