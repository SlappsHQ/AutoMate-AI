import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Example usage
    prompt = "Hello!"
    completion = get_completion(prompt)
    print("Response from OpenAI:", completion)
