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

# Step 4: Retrieve and truncate commit details
result = subprocess.run(
    ["git", "show", "--pretty=format:%B", commit_id],
    capture_output=True,
    text=True,
)
commit_data = result.stdout.strip()

# Truncate to the first 300 lines
max_lines = 300
truncated_commit_data = "\n".join(commit_data.splitlines()[:max_lines])

# Print the truncated data for verification
print("Truncated Commit Data (First 300 Lines):")
print(truncated_commit_data)  # This outputs the first 300 lines to verify content

# Step 5: Pass truncated commit data to OpenAI for analysis
completion = client.chat_completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code review assistant."},
        {"role": "user", "content": f"Please review the following code changes:\n{truncated_commit_data}"}
    ]
)

# Access and print the assistant's message content
print(completion.choices[0].message["content"])
