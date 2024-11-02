# Agent/AutoMate/scripts/controller.py

import os
import sys
from organiser import run

# Print diagnostic information
print("Current directory:", os.getcwd())
print("Files in current directory:", os.listdir())
print("Files in scripts directory:", os.listdir(os.path.dirname(__file__)))

# Get parameters dynamically from command-line arguments
if len(sys.argv) < 5:
    print("Usage: controller.py <commit_id> <owner> <repo> <branch> <file_path>")
    sys.exit(1)

commit_id = sys.argv[1]
owner = sys.argv[2]
repo = sys.argv[3]
branch = sys.argv[4]
file_path = sys.argv[5]

# Call the run function with the parameters passed from run_automate.py
run(owner, repo, branch, file_path)
