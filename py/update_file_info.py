# Created by: kok-s0s
# Last Modified at: Wed Dec 27 14:24:04 2023
# File Name: update_file_info.py

import os
import sys
import time

# Mapping of comment prefixes for different file types
FILE_TYPE_COMMENT_PREFIX = {
    ".py": "# ",
    ".java": "// ",
    ".c": "// ",
    ".cpp": "// ",
    ".h": "// ",
    ".html": "<!-- ",
    ".css": "/* ",
    ".js": "// ",
    ".sh": "# ",
    # Add more file types and corresponding comment prefixes
}


def get_file_info(file_path):
    """
    Get file information: last modification time, file name
    """
    try:
        # Get file last modification time
        modify_time = time.ctime(os.path.getmtime(file_path))
        # Get file name
        file_name = os.path.basename(file_path)
        return modify_time, file_name
    except Exception as e:
        print(f"Error getting file information: {e}")
        sys.exit(1)


def update_file_header(file_path, modify_time, file_name, comment_prefix):
    """
    Insert or update information in the file header: creator, last modification time, file name, with the specified comment prefix, and a newline
    """
    try:
        with open(file_path, "r+") as file:
            content = file.read()

            # Find the entire file header
            header_start = content.find(comment_prefix)
            header_end = content.find("\n\n") if header_start != -1 else -1

            existing_info = ""  # Initialize existing_info as an empty string

            if header_start != -1 and header_end != -1:
                existing_info = content[header_start:header_end]

                # Remove the old information from the entire file header
                content = content.replace(existing_info, "").strip()

            file.seek(0, 0)
            header = f"{comment_prefix}Created by: kok-s0s\n{comment_prefix}Last Modified at: {modify_time}\n{comment_prefix}File Name: {file_name}\n"
            file.write(header + "\n" + content)

            # Return the update status
            return existing_info == ""

    except Exception as e:
        print(f"Error updating file header: {e}")
        sys.exit(1)


def process_file_or_folder(path, file_extension=None):
    """
    Process a single file or all code files within a folder based on the provided path and optional file extension
    """
    if os.path.isfile(path):
        # Single file case
        modify_time, file_name = get_file_info(path)
        _, current_extension = os.path.splitext(path)
        current_extension = current_extension.lower()

        # Check if the file type is supported
        if current_extension in FILE_TYPE_COMMENT_PREFIX:
            # Get the comment prefix
            comment_prefix = FILE_TYPE_COMMENT_PREFIX[current_extension]

            # Update file header information and get the update status
            updated = update_file_header(path, modify_time, file_name, comment_prefix)

            if updated:
                print(
                    f"File information has been successfully inserted in the file header: {path}"
                )
            else:
                print(
                    f"File information has been successfully updated in the file header: {path}"
                )

    elif os.path.isdir(path):
        # Folder case
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                _, current_extension = os.path.splitext(file_path)
                current_extension = current_extension.lower()

                # Check if the file type is supported
                if not file_extension or (
                    file_extension and current_extension == f".{file_extension.lower()}"
                ):
                    if current_extension in FILE_TYPE_COMMENT_PREFIX:
                        # Get file information
                        modify_time, file_name = get_file_info(file_path)

                        # Get the comment prefix
                        comment_prefix = FILE_TYPE_COMMENT_PREFIX[current_extension]

                        # Update file header information and get the update status
                        updated = update_file_header(
                            file_path, modify_time, file_name, comment_prefix
                        )

                        if updated:
                            print(
                                f"File information has been successfully inserted in the file header: {file_path}"
                            )
                        else:
                            print(
                                f"File information has been successfully updated in the file header: {file_path}"
                            )
    else:
        print("Invalid file or folder path.")
        sys.exit(1)


def main():
    # Check parameters
    if len(sys.argv) not in [2, 3]:
        print("Usage: python3 script.py <file_path_or_folder> [file_extension]")
        sys.exit(1)

    target_path = sys.argv[1]
    file_extension = sys.argv[2] if len(sys.argv) == 3 else None

    process_file_or_folder(target_path, file_extension)


if __name__ == "__main__":
    main()
