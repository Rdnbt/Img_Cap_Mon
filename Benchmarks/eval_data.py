import csv
import random

# Path to the original CSV file
original_csv_file = 'path/to/original_dataset.csv'

# Path to the new CSV file for the extracted subset
subset_csv_file = 'path/to/extracted_subset.csv'

# Number of image-text pairs to extract
num_pairs_to_extract = 1000

# Seed for randomization
seed_value = 42

# Set the random seed
random.seed(seed_value)

# Read the original CSV file
with open(original_csv_file, 'r') as file:
    reader = csv.reader(file, delimiter='|')
    header = next(reader)  # Skip the header line
    rows = list(reader)  # Read all the rows into a list

# Select random rows without shuffling
subset_rows = random.sample(rows, num_pairs_to_extract)

# Write the subset rows to the new CSV file
with open(subset_csv_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(header)  # Write the header line
    writer.writerows(subset_rows)

print(f"Successfully extracted {num_pairs_to_extract} image-text pairs to {subset_csv_file}.")
