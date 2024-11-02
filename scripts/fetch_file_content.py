import requests
import base64
import os

# GitHub repository details
owner = "SlappsHQ"
repo = "Agent"
branch = "main"
file_path = "Agent/roadmap.md"  # Change this to your specific file path within the repo

# GitHub API URL for the specific file
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}"

# Headers with the GitHub token for authentication
headers = {
    "Authorization": f"Bearer {os.getenv('AUTOMATE_GITHUB_TOKEN')}"  # Ensure AUTOMATE_GITHUB_TOKEN is set in your environment
}

# Fetch file details
response = requests.get(url, headers=headers)

if response.status_code == 200:
    file_data = response.json()
    content = base64.b64decode(file_data["content"]).decode("utf-8")  # Decode the base64 file content
    
    print("File Content:")
    print(content)
else:
    print(f"Failed to fetch file content: {response.status_code}, {response.text}")
