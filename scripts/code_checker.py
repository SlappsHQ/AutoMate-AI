import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Analyze this code:\n\n{code}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Example code analysis
code_snippet = """
def example():
    print("Hello, World!")
"""

feedback = analyze_code(code_snippet)
print("AI Feedback:\n", feedback)
