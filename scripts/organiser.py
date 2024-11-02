import os
import openai
from fetch_file_content import fetch_file_content

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code_structure(file_content):
    """Analyzes the structure of a file and generates suggestions for organization."""
    completion = openai.chat.Completion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code organization assistant for SwiftUI projects."},
            {"role": "user", "content": f"Analyze the structure of this code and suggest if any large views or components should be moved to separate files:\n{file_content}"}
        ]
    )
    return completion.choices[0].message["content"]

def run(owner, repo, branch, file_path):
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
