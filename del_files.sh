#!/bin/bash

# Ensure the folder path and time argument are provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 /path/to/folder 'HH:MM'"
    exit 1
fi

# Set the folder path and specified time with today's date
FOLDER="$1"
TIME="$(date +%Y-%m-%d) $2"

# Check if the specified folder exists
if [ ! -d "$FOLDER" ]; then
    echo "Error: Folder $FOLDER does not exist."
    exit 1
fi

# Find and delete files created at the specified time in the specified folder
find "$FOLDER" -type f -newermt "$TIME" ! -newermt "$TIME + 1 minute" -exec rm -f {} \;

echo "Files created at $TIME in $FOLDER have been deleted."

