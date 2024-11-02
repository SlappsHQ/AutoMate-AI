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

# Step 4: Retrieve only the new code additions using `git show`
result = subprocess.run(
    ["git", "show", "--pretty=format:", commit_id, "--unified=0"],
    capture_output=True,
    text=True,
)
commit_data = result.stdout.strip()

# Truncate commit data for token limit compliance
max_tokens = 1000  # Reduced further for testing; adjust as needed
commit_data = commit_data[:max_tokens]

# Print for verification
print("Truncated Commit Data for Analysis:")
print(commit_data)

# Step 5: Pass the refined commit data to OpenAI for analysis
completion = client.chat_completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code review assistant."},
        {"role": "user", "content": f"Please review the following code changes:\n{commit_data}"}
    ]
)

# Access and print the assistant's response
print(completion.choices[0].message.content)
