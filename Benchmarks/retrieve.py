import os
import shutil
import csv

# Path to the folder where you extracted the Flickr30K dataset
flickr30k_dataset_path = "/Users/erdenebat/Desktop/Erdenebat/Research/ImageCaptioning/flickr30k_images/flickr30k_images"

# Path to the CSV file containing the randomly selected captions
captions_file = "output_1000.csv"

# Path to the folder where you want to store the retrieved images
output_folder = "flickr1000"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file
with open(captions_file, "r") as file:
    reader = csv.reader(file, delimiter="|")
    captions = list(reader)

# Process each caption
for caption in captions:
    # Extract the image name from the caption
    image_name = caption[0].strip()

    # Build the path to the image in the Flickr30K dataset
    image_path = os.path.join(flickr30k_dataset_path, image_name)

    # Check if the image exists
    if os.path.exists(image_path):
        # Build the path to copy the image to the output folder
        output_path = os.path.join(output_folder, image_name)

        # Copy the image to the output folder
        shutil.copy(image_path, output_path)
    else:
        print(f"Image {image_name} not found in the dataset.")

print("Image retrieval and storage completed.")
