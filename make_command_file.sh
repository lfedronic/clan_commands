#!/bin/bash

# Check if a path argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 /path/to/folder"
    exit 1
fi

# Store the provided folder path
folder_path="$1"

# Check if the provided path is a directory
if [ ! -d "$folder_path" ]; then
    echo "Error: '$folder_path' is not a directory."
    exit 1
fi

# Get the folder name
folder_name=$(basename "$folder_path")

# Create or clear the batch file
batch_file="${folder_name}_ipsyn.bat"
> "$batch_file"

# Iterate over all files in the folder
for file in "$folder_path"/*; do
    # Skip directories
    if [ -f "$file" ]; then
# Use the absolute path of the file
        abs_path=$(realpath "$file")
        echo "ipsyn +t*CHI +o –leng $abs_path" >> "$batch_file"
    fi
done

echo "Batch file '$batch_file' has been created/updated."

