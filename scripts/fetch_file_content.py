# fetch_github_file.py

import requests
import base64
import os

def fetch_file_content(owner, repo, file_path, branch="main", github_token=None):
    """
    Fetches the content of a specific file from a GitHub repository.

    Args:
        owner (str): GitHub repository owner.
        repo (str): GitHub repository name.
        file_path (str): Path to the file within the repository.
        branch (str): Branch from which to fetch the file.
        github_token (str): GitHub token for authentication.

    Returns:
        str: Decoded file content if successful, otherwise None.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}"
    headers = {
        "Authorization": f"Bearer {github_token or os.getenv('AUTOMATE_GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3.raw"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_data = response.json()
        return base64.b64decode(file_data["content"]).decode("utf-8")
    else:
        print(f"Failed to fetch file content: {response.status_code}, {response.text}")
        return None
