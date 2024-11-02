import sys
import requests
import openai
import os

# GitHub repository and commit details
owner = "SlappsHQ"
repo = "Agent"
commit_id = sys.argv[1]  # The commit SHA passed as an argument

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fetch commit details using GitHub API
url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_id}"
headers = {
    "Authorization": f"Bearer {os.getenv('AUTOMATE_GITHUB_TOKEN')}"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    commit_data = response.json()
    files = commit_data.get("files", [])

    # Collect patches from changed files
    patch_data = "\n".join(file.get("patch", "") for file in files)
    patch_data = patch_data[:1000]  # Truncate for token limit

    print("Truncated Commit Data for Analysis:")
    print(patch_data)

    # Send patch data to OpenAI
    completion = client.chat_completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code review assistant."},
            {"role": "user", "content": f"Please review the following code changes:\n{patch_data}"}
        ]
    )
    print(completion.choices[0].message.content)
else:
    print(f"Failed to fetch commit data: {response.status_code}, {response.text}")
