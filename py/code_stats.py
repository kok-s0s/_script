import os
import sys


class ProjectTree:
    def __init__(self, project_path):
        self.project_path = project_path
        self.ignore_folders = set(["build", "out", "target"])

    def should_ignore(self, name):
        """
        Check if a folder should be ignored
        """
        return name.startswith(".") or name in self.ignore_folders

    def get_size(self, path):
        """
        Calculate the size of a file or directory
        """
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            total_size = 0
            with os.scandir(path) as entries:
                for entry in entries:
                    if not self.should_ignore(entry.name):
                        total_size += self.get_size(entry.path)
            return total_size
        else:
            return 0

    def format_size(self, size):
        """
        Format file size
        """
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0

    def tree_structure(self, path, indent=""):
        """
        Display the tree structure of folders and files
        """
        if os.path.isfile(path):
            print(
                f"{indent}- {os.path.basename(path)} ({self.format_size(self.get_size(path))})"
            )
        elif os.path.isdir(path) and not self.should_ignore(os.path.basename(path)):
            print(
                f"{indent}+ {os.path.basename(path)} ({self.format_size(self.get_size(path))})"
            )
            with os.scandir(path) as entries:
                for entry in entries:
                    self.tree_structure(entry.path, indent + "  ")

    def display_tree(self):
        """
        Display the tree structure of the project
        """
        if os.path.exists(self.project_path):
            self.tree_structure(self.project_path)
        else:
            print("The specified path does not exist.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 project_tree.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]
    project_tree = ProjectTree(project_path)
    project_tree.display_tree()
