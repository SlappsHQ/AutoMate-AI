import os
from organiser import run

# Print diagnostic information
print("Current directory:", os.getcwd())
print("Files in current directory:", os.listdir())
print("Files in scripts directory:", os.listdir(os.path.dirname(__file__)))

# Set up parameters for the `run` function
commit_id = os.getenv("GITHUB_SHA")  # Example dynamic value, or pass this as an argument if available
owner = "SlappsHQ"
repo = "Agent"
branch = "main"
file_path = "Agent/roadmap.md"  # Example path for testing; update as needed

# Call the run function with the dynamic parameters
run(owner, repo, branch, file_path)
