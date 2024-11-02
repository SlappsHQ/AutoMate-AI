# # AutoMate/scripts/code_checker.py

# import sys
# import requests
# import openai
# import os

# # GitHub repository and commit details
# owner = "SlappsHQ"
# repo = "Agent"
# commit_id = sys.argv[1]  # The commit SHA passed as an argument

# openai_api_key = os.getenv("OPENAI_API_KEY")

# automate_github_token = os.getenv("AUTOMATE_GITHUB_TOKEN")

# print(f"OpenAI API Key: {openai_api_key}")
# print(f"Automate GitHub Token: {automate_github_token}")

# # Initialize OpenAI API client
# client = openai.OpenAI(api_key=openai_api_key)


# # Fetch commit details using GitHub API
# url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_id}"
# headers = {
#     "Authorization": f"Bearer {automate_github_token}"
# }
# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     commit_data = response.json()
#     files = commit_data.get("files", [])

#     # Collect patches from changed files
#     patch_data = "\n".join(file.get("patch", "") for file in files)
#     patch_data = patch_data[:1000]  # Truncate for token limit

#     print("Truncated Commit Data for Analysis:")
#     print(patch_data)

#     # Send patch data to OpenAI
#     completion = client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a code review assistant."},
#             {"role": "user", "content": f"Please review the following code changes:\n{patch_data}"}
#         ]
#     )
#     print(completion.choices[0].message.content)
# else:
#     print(f"Failed to fetch commit data: {response.status_code}, {response.text}")
