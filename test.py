from tools.llm import gemini

response = gemini.generate(
    "Say hello in one sentence."
)

print(response)