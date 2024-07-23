#!/bin/bash
# Check for correct usage
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 folder_path n output_directory"
    exit 1
fi

folder_path=$1
n=$2
output_directory=$3

# Check if the output directory exists, if not, create it
if [ ! -d "$output_directory" ]; then
    mkdir -p "$output_directory"
fi

# Iterate over all .cha files in the given folder
for file in "$folder_path"/*.cha; do
    if [ ! -f "$file" ]; then
        echo "No .cha files found in the folder."
        exit 1
    fi

    base_filename=$(basename "$file" .cha)

    # Read the file's header
    header=$(awk '/@Types:/ {print; exit} {print}' "$file")
    num_header_lines=$(echo "$header" | wc -l)

    # Process each file and split it based on `n` lines of contents
    tail -n +$(($num_header_lines + 1)) "$file" | awk -v n="$n" \
        -v base_filename="$base_filename" -v output_directory="$output_directory" '
    BEGIN {
        header = ARGV[1]
        split(header, header_buffer, "\n")
        ARGV[1] = ""
        total_lines = 0
    }
    {
        lines[++total_lines] = $0
    }
    END {
        parts = int(total_lines / n)
        remainder = total_lines % n

        for (part_number = 1; part_number <= parts; part_number++) {
            file_path = output_directory "/" base_filename part_number ".cha"
            start_line = (part_number - 1) * n + 1
            end_line = start_line + n - 1

            # Output the header to the new file
            for (i = 1; i <= length(header_buffer); i++) {
                print header_buffer[i] > file_path
            }

            # Output the body lines to the new file
            for (line = start_line; line <= end_line; line++) {
                print lines[line] >> file_path
            }
            print "@End" >> file_path
        }
        if (remainder > 0) {
            file_path = output_to_directory "/" base_filename (parts + 1) ".cha"
            start_line = parts * n + 1
            end_line = total_lines
            
            # Output the header to the last file containing the remainder
            for (i = 1; i <= length(header_buffer); i++) {
                print header_buffer[i] > file_path
            }
            
            # Output the remainder lines to the last new file
            for (line = start_line; line <= end_line; line++) {
        print lines[line] >> file_path
            }
            print "@End" >> file_path
        }
    }' "$(echo "$header")"
done
echo "Processing completed."