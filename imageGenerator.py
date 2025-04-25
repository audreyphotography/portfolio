import os
import json
import re

# Folder where your images live
image_folder = "images"
output_json = "imagesJsonFile.json"

# Valid extensions
valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".JPG", ".JPEG", ".PNG", ".GIF"}

# Function to extract the numeric part of the filename
def extract_index(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')  # Push unnumbered files to the end

# Get and sort image files by numeric index
image_files = [f for f in os.listdir(image_folder) if os.path.splitext(f)[1] in valid_extensions]
sorted_files = sorted(image_files, key=extract_index)

# Create relative paths
image_paths = [f"{image_folder}/{filename}" for filename in sorted_files]

# Save to JSON
with open(output_json, "w") as f:
    json.dump(image_paths, f, indent=2)

print(f"✅ Successfully created {output_json} with {len(image_paths)} images sorted by index.")
