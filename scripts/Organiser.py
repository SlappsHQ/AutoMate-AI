# AutoMate/scripts/organiser.py

import os
import openai
from fetch_file_content import fetch_file_content

# OpenAI API key (ensure it's set in the environment)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.ChatCompletion(api_key=openai_api_key)

# Configuration for the GitHub repository
owner = "SlappsHQ"
repo = "Agent"
branch = "main"
file_path = "path/to/your/file"  # Set this to the file path you want to analyze

def analyze_code_structure(file_content):
    """Analyzes the structure of a file and generates suggestions for organization."""
    completion = client.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code organization assistant for SwiftUI projects."},
            {"role": "user", "content": f"Analyze the structure of this code and suggest if any large views or components should be moved to separate files:\n{file_content}"}
        ]
    )
    return completion.choices[0].message.content

def run():
    """Fetches file content and performs code structure analysis."""
    github_token = os.getenv("AUTOMATE_GITHUB_TOKEN")
    file_content = fetch_file_content(owner, repo, file_path, branch, github_token)
    
    if file_content:
        print("Analyzing code structure...")
        suggestion = analyze_code_structure(file_content)
        print("Organiser's suggestion:")
        print(suggestion)
    else:
        print("No file content available for analysis.")
