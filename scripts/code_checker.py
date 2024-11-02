import sys
import openai
import os
import subprocess

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Retrieve commit ID from the argument
commit_id = sys.argv[1] if len(sys.argv) > 1 else None
if not commit_id:
    print("No commit ID provided.")
    sys.exit(1)

# Step 2: Retrieve only the changed lines for each file in the commit
result = subprocess.run(
    ["git", "show", "--pretty=", "--unified=0", commit_id],  # The `--pretty=` keeps metadata out of output
    capture_output=True,
    text=True,
)
commit_data = result.stdout.strip()

# Limit commit data to a reasonable length
max_tokens = 7500
commit_data = commit_data[:max_tokens]

# Print for verification
print("Truncated Commit Data for Analysis:")
print(commit_data)

# Step 3: Send commit data to OpenAI for analysis
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code review assistant."},
        {"role": "user", "content": f"Please review the following code changes:\n{commit_data}"}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)
