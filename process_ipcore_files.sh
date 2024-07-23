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

# Iterate over all files in the folder ending with 'ipcore.cex'
for file in "$folder_path"/*ipcore-100.cex; do
    # Check if the file exists
    if [ -f "$file" ]; then
        # Get the base name of the file (without path and extension)
        base_name=$(basename "$file" .ipcore-100.cex)
        # Define the output file name
        output_file="${folder_path}/${base_name}_ipsyn.txt"
        
        # Process the file, extract every third line, remove the first 6 characters, and save to the output file
        awk 'NR % 3 == 1 {print substr($0, 7)}' "$file" | head -n 100 > "$output_file"
        
        echo "Processed '$file' and saved to '$output_file'."
    fi
done

echo "All files processed."

