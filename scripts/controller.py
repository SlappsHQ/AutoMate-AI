# Agent/AutoMate/scripts/controller.py

import sys
import os

# Ensure the script directory is in the Python path to locate organiser
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

import organiser

# Retrieve arguments passed from run_automate.py
commit_id = sys.argv[1]
owner = sys.argv[2]
repo = sys.argv[3]
branch = sys.argv[4]
file_path = sys.argv[5]

# Call organiser's run function with specified values
organiser.run(owner, repo, branch, file_path)
