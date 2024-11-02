import sys
import openai
import os
import requests

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# GitHub repository details
owner = "SlappsHQ"
repo = "Agent"
commit_id = sys.argv[1] if len(sys.argv) > 1 else None

if not commit_id:
    print("No commit ID provided.")
    sys.exit(1)

print("Commit ID:", commit_id)

# GitHub API URL for the specific commit
url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_id}"
headers = {
    "Authorization": f"Bearer {os.getenv('MY_GITHUB_TOKEN')}"  # Use the new token variable
}


# Step 4: Retrieve only the new code additions using the GitHub API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    commit_data = response.json()
    files = commit_data.get("files", [])
    
    # Format the code changes for analysis
    formatted_data = ""
    for file in files:
        filename = file["filename"]
        patch = file.get("patch", "No changes available")
        formatted_data += f"File: {filename}\nChanges:\n{patch}\n{'-'*40}\n"
    
    # Truncate data for token limit compliance
    max_tokens = 1000  # Adjust as needed
    formatted_data = formatted_data[:max_tokens]

    # Print for verification
    print("Truncated Commit Data for Analysis:")
    print(formatted_data)

    # Pass the refined commit data to OpenAI for analysis
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code review assistant."},
            {"role": "user", "content": f"Please review the following code changes:\n{formatted_data}"}
        ]
    )

    # Access and print the assistant's response
    print(completion.choices[0].message.content)

else:
    print(f"Failed to fetch commit data: {response.status_code}, {response.text}")
