import sys
import openai
import os
import subprocess

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Retrieve commit ID from the argument
commit_id = sys.argv[1] if len(sys.argv) > 1 else None
if not commit_id:
    print("No commit ID provided.")
    sys.exit(1)

# Retrieve only the changed lines in the commit with filenames, limited to the diff portion
result = subprocess.run(
    ["git", "diff", "--unified=0", commit_id, "--minimal"],  # Retrieves minimal diff changes only
    capture_output=True,
    text=True,
)

# Limiting to a preview of 50 lines for testing
commit_data = "\n".join(result.stdout.strip().splitlines()[:50])

# Display truncated commit data for verification
print("Truncated Commit Data for Analysis (50 lines):")
print(commit_data)

# Pass the refined commit data to OpenAI for analysis
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code review assistant."},
        {"role": "user", "content": f"Please review the following code changes:\n{commit_data}"}
    ]
)

# Access and print the assistant's response
print(completion.choices[0].message.content)
