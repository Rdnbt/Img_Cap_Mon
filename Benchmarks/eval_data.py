import csv
import random

# Path to the original CSV file
original_csv_file = 'results.csv'

# Path to the new CSV file for the extracted subset
subset_csv_file = 'output_1000.csv'

# Number of image-text pairs to extract
num_pairs_to_extract = 1000

# Seed for randomization
seed_value = 1

# Set the random seed
random.seed(seed_value)

# Read the original CSV file
with open(original_csv_file, 'r') as file:
    reader = csv.reader(file, delimiter='|')
    header = next(reader)  # Skip the header line
    rows = list(reader)  # Read all the rows into a list

# Shuffle the rows
random.shuffle(rows)

# Select random rows with different images
selected_rows = []
selected_images = set()  # Set to keep track of selected images

for row in rows:
    image_name = row[0].strip()
    if image_name not in selected_images:
        selected_rows.append(row)
        selected_images.add(image_name)

    if len(selected_rows) == num_pairs_to_extract:
        break

# Write the subset rows to the new CSV file
with open(subset_csv_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(header)  # Write the header line
    writer.writerows(selected_rows)

print(f"Successfully extracted {num_pairs_to_extract} image-text pairs to {subset_csv_file}.")
