# Created by: kok-s0s
# Last Modified at: Wed Dec 27 14:39:38 2023
# File Name: sync_git_projects.py

import os
import subprocess
import sys


def sync_git_projects(folder_path):
    # Get the list of all files and folders in the target directory
    items = os.listdir(folder_path)

    # Iterate through each project
    for item in items:
        item_path = os.path.join(folder_path, item)

        # Check if it is a folder and contains a .git directory, indicating a Git project
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, ".git")):
            print(f"Syncing Git project: {item}")
            # Change to the project directory
            os.chdir(item_path)

            # Execute the git pull command
            subprocess.run(["git", "pull"])


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 sync_git_projects.py <folder_path>")
        sys.exit(1)

    # Get the target folder path from the command line arguments
    folder_path = sys.argv[1]

    # Check if the target folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found: {folder_path}")
        sys.exit(1)

    # Execute the synchronization operation
    sync_git_projects(folder_path)
