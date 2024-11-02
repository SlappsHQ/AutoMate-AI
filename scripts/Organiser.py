import os
import sys
import requests
import openai

# GitHub repository and commit details
owner = "SlappsHQ"
repo = "Agent"
commit_id = '478fd202b1dcdac7ec93078d9df3068f2e519145'  # The commit SHA passed as an argument
file_path = sys.argv[2] if len(sys.argv) > 2 else None

# Access tokens
openai_api_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("AUTOMATE_GITHUB_TOKEN")

# Initialize OpenAI API client
client = openai.OpenAI(api_key=openai_api_key)

def fetch_file_content(file_path):
    """Fetches the content of a specific file from GitHub."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3.raw"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch file content: {response.status_code}, {response.text}")
        return None

def analyze_code_structure(file_content):
    """Analyzes the structure of a file and generates suggestions for organization."""
    completion = client.chat_completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code organization assistant for SwiftUI projects."},
            {"role": "user", "content": f"Analyze the structure of this code and suggest if any large views or components should be moved to separate files:\n{file_content}"}
        ]
    )
    return completion.choices[0].message.content

# Fetch the content of the file to check for structure
if file_path:
    file_content = fetch_file_content(file_path)
    if file_content:
        print("Analyzing code structure...")
        suggestion = analyze_code_structure(file_content)
        print("Organiser's suggestion:")
        print(suggestion)
else:
    print("No file path provided for analysis.")
