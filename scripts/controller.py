import os

print("Current directory:", os.getcwd())
print("Files in current directory:", os.listdir())
print("Files in scripts directory:", os.listdir(os.path.dirname(__file__)))

# Then try importing organiser
from AutoMate.scripts.organiser_1 import run
