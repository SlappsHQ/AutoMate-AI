import os
import requests

# GitHub repository details
owner = "SlappsHQ"
repo = "Agent"
branch = "main"
github_token = os.getenv("AUTOMATE_GITHUB_TOKEN")

# Issue details
file_path = "Agent/roadmap.md"
line_number = 42  # Adjust to the line you need
title = f"Issue at line {line_number} in {file_path}"
body = f"There's a potential issue in [{file_path} line {line_number}](https://github.com/{owner}/{repo}/blob/{branch}/{file_path}#L{line_number}).\n\nPlease review this section."

# GitHub API URL to create the issue
url = f"https://api.github.com/repos/{owner}/{repo}/issues"
headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Payload for creating the issue
data = {
    "title": title,
    "body": body,
}

# Create the issue
response = requests.post(url, headers=headers, json=data)
if response.status_code == 201:
    print("Issue created successfully!")
else:
    print(f"Failed to create issue: {response.status_code}")
    print(response.json())
