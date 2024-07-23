import sys
import os

def extract_counts(lines):
    counts = {'T': 0, 'N': 0, 'V': 0, 'Q': 0, 'S': 0}
    for line in lines:
        if line.startswith('N ='):
            counts['N'] = int(line.split('=')[1].strip())
        elif line.startswith('V ='):
            counts['V'] = int(line.split('=')[1].strip())
        elif line.startswith('Q ='):
            counts['Q'] = int(line.split('=')[1].strip())
        elif line.startswith('S ='):
            counts['S'] = int(line.split('=')[1].strip())
        elif line.startswith('Total ='):
            counts['T'] = int(line.split('=')[1].strip())
    return counts

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        # Extract counts from the end of the file
        counts = extract_counts(lines[-10:])  # Assuming the counts are among the last 10 lines

        with open(output_file, 'w') as outfile:
            # Write the counts as the first rows of the CSV
            for key in ['T', 'N', 'V', 'Q', 'S']:
                outfile.write(f"{key}, {counts[key]}\n")
            
            rule = None
            for line in lines:
                line = line.strip()
                if line.startswith("Rule:"):
                    # Extract the rule identifier
                    rule = line.split(' - ')[0].replace('Rule: ', '').strip()
                elif line.startswith("Score:") and rule:
                    # Extract the score
                    score = line.split(': ')[1].strip()
                    # Write the rule and score to the output file
                    outfile.write(f"{rule}, {score}\n")
                    rule = None  # Reset rule after processing
        print(f"Processed data written to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('ipsyn-100.cex'):
            input_file = os.path.join(folder_path, filename)
            # Create output file name
            base_name = filename[:-len('.ipsyn-100.cex')]
            output_file = os.path.join(folder_path, f"{base_name}_scores.csv")
            # Process each file
            process_file(input_file, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Provided path is not a directory: {folder_path}")
        sys.exit(1)

    process_folder(folder_path)

