# Agent/AutoMate/scripts/controller.py

import sys
import organiser

# Retrieve arguments passed from run_automate.py
commit_id = sys.argv[1]
owner = sys.argv[2]
repo = sys.argv[3]
branch = sys.argv[4]
file_path = sys.argv[5]

# Call organiser's run function with specified values
organiser.run(owner, repo, branch, file_path)
