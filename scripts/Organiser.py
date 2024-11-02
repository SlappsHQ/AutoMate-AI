# organizer.py

import os
import openai
from fetch_github_file import fetch_file_content

# GitHub repository and file details
owner = "SlappsHQ"
repo = "Agent"
file_path = "Agent/roadmap.md"  # Example file path to analyze

# Initialize OpenAI API client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

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

# Fetch the file content
file_content = fetch_file_content(owner, repo, file_path, github_token=os.getenv("AUTOMATE_GITHUB_TOKEN"))

# Analyze the content if successfully fetched
if file_content:
    print("Analyzing code structure...")
    suggestion = analyze_code_structure(file_content)
    print("Organizer's suggestion:")
    print(suggestion)
else:
    print("File content could not be retrieved for analysis.")
