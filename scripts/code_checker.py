# AutoMate/scripts/code_checker.py

import sys
import openai
import os
import subprocess

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 3: Retrieve commit ID from the argument
commit_id = sys.argv[1] if len(sys.argv) > 1 else None
if not commit_id:
    print("No commit ID provided.")
    sys.exit(1)

# Step 4: Retrieve commit details using the commit ID
result = subprocess.run(
    ["git", "show", "--name-only", "--pretty=format:%b", commit_id],
    capture_output=True,
    text=True,
)
commit_data = result.stdout.strip()

# Step 5: Pass commit data to OpenAI for analysis
completion = client.chat.completions.create(
    model="gpt-4",  # Update to your specific model if needed
    messages=[
        {"role": "system", "content": "You are a code review assistant."},
        {"role": "user", "content": "Please review the following code changes:\n{commit_data}"}
    ]
)

# Access and print the assistant's message content
print(completion.choices[0].message.content)




