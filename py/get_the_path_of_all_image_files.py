# Created by: kok-s0s
# Last Modified at: Wed Dec 27 14:23:43 2023
# File Name: get_the_path_of_all_image_files.py

import os
import sys


def find_images(folder_path, extensions=["jpg", "jpeg", "png", "gif"]):
    images = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                images.append(os.path.join(root, file))
    return images


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py folder_path")
        sys.exit(1)

    # Get the folder path from the command-line arguments
    folder_path = sys.argv[1]

    # Check if the specified folder exists
    if not os.path.isdir(folder_path):
        print(f"The specified folder '{folder_path}' does not exist.")
        sys.exit(1)

    # Call the function to find image files recursively
    image_files = find_images(folder_path)

    # Print the found image files
    if not image_files:
        print(f"No image files found in '{folder_path}' or its subfolders.")
    else:
        print("Image files found:")
        for image_file in image_files:
            print(image_file)
