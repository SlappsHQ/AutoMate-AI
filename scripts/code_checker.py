from openai import OpenAI
import os

# Initialize the client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a chat completion request
completion = client.chat.completions.create(
    model="gpt-4",  # Update to your specific model if needed
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

# Access and print the assistant's message content
print(completion.choices[0].message.content)
