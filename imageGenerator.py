import os
import json

# Root folder where your categorized image folders are located
image_root = "images"
output_json = "imagesJsonFile.json"

# Valid file extensions (case-insensitive)
valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".JPG", ".JPEG", ".PDF"}

# Store image data entries
image_data = []

for category in os.listdir(image_root):
    category_path = os.path.join(image_root, category)
    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            # Skip Mac metadata files and hidden files
            if filename.startswith("._") or filename.startswith(".DS_") or filename.startswith("."):
                continue

            ext = os.path.splitext(filename)[1].lower()
            if ext in valid_extensions:
                image_data.append({
                    "src": f"{image_root}/{category}/{filename}",
                    "category": category
                })

# Save the result to a JSON file
with open(output_json, "w") as f:
    json.dump(image_data, f, indent=2)

print(f"✅ Created {output_json} with {len(image_data)} entries.")