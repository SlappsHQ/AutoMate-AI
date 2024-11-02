from openai import OpenAI
import os

# Initialize the client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a chat completion request
completion = client.chat.completions.create(
    model="gpt-4",  # or use the specific model identifier you need
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

# Print the assistant's message
print(completion.choices[0].message["content"])
