import re
from collections import defaultdict
import argparse
import os

def parse_scores(filename):
    # Initialize dictionaries to hold scores
    scores = defaultdict(int)
    category_totals = defaultdict(int)
    
    # Read the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Improved regex pattern to capture scores
    scoring_lines = re.findall(r'-\s*(\w\d+):\s*(\d+)', content)
    
    # Process each scoring line
    for item, score in scoring_lines:
        score = min(int(score), 2)
        scores[item] += score
    
    # Calculate subtotals
    for item, score in scores.items():
        category = item[0]
        category_totals[category] += score
    
    # Calculate total
    total = sum(category_totals.values())
    
    # Prepare the output in the required format
    output = []
    output.append(f"T, {total}")
    for category in ['N', 'V', 'Q', 'S']:
        output.append(f"{category}, {category_totals[category]}")
    for item in sorted(scores.keys()):
        output.append(f"{item}, {scores[item]}")
    
    return '\n'.join(output)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Evaluate and summarize scoring information from a text file.')
    parser.add_argument('input_file', type=str, help='The input file to be evaluated')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the input file name
    input_file = args.input_file
    
    # Call the function to parse scores
    result = parse_scores(input_file)
    
    # Create the output file name
    output_file = f"{os.path.splitext(input_file)[0]}_score.txt"
    
    # Write the result to the output file
    with open(output_file, 'w') as file:
        file.write(result)
    
    print(f"Output written to {output_file}")

if __name__ == '__main__':
    main()

