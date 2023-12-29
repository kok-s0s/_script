import os
import sys


def bulk_rename(directory, old_substring, new_substring):
    """
    Bulk rename files in a directory by replacing a substring in their names.

    Parameters:
        directory (str): The path to the directory containing the files.
        old_substring (str): The substring to be replaced in the filenames.
        new_substring (str): The substring to replace the old substring.

    Returns:
        None
    """
    try:
        # List all files in the directory
        files = os.listdir(directory)

        # Iterate through each file
        for file_name in files:
            # Create the new file name by replacing the old substring
            new_name = file_name.replace(old_substring, new_substring)

            # Construct the full paths
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} to {new_name}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print(
            "Usage: python bulk_rename.py <directory_path> <old_substring> <new_substring>"
        )
        sys.exit(1)

    # Retrieve command-line arguments
    directory_path = sys.argv[1]
    old_substring_to_replace = sys.argv[2]
    new_substring = sys.argv[3]

    # Call the bulk_rename function with the provided arguments
    bulk_rename(directory_path, old_substring_to_replace, new_substring)
