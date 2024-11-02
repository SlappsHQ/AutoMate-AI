import requests
import openai
import os
from fetch_file_content import fetch_file_content  # Corrected import

# GitHub repository details
owner = "SlappsHQ"
repo = "Agent"
file_path = "Agent/Views/ChatView.swift"  # Set your specific file path within the repo
branch = "main"

# Access tokens
openai_api_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("AUTOMATE_GITHUB_TOKEN")

# Set OpenAI API key
openai.api_key = openai_api_key

def analyze_code_structure(file_content):
    """Analyzes the structure of a file and generates suggestions for organization."""
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code organization assistant for SwiftUI projects."},
            {"role": "user", "content": f"Analyze the structure of this code and suggest if any large views or components should be moved to separate files:\n{file_content}"}
        ]
    )
    return completion.choices[0].message.content

# Fetch the content of the file to check for structure
file_content = fetch_file_content(owner, repo, file_path, branch, github_token)
if file_content:
    print("Analyzing code structure...")
    suggestion = analyze_code_structure(file_content)
    print("Organiser's suggestion:")
    print(suggestion)
else:
    print("No file content available for analysis.")
