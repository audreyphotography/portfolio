import os
import json

# Root folder where your categorized folders live
image_root = "images"
output_json = "imagesJsonFile.json"

# Accepted image extensions (case-insensitive)
valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}

# Build list of image data
image_data = []

for category in os.listdir(image_root):
    category_path = os.path.join(image_root, category)
    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in valid_extensions:
                image_data.append({
                    "src": f"{image_root}/{category}/{filename}",
                    "category": category
                })

# Save the data to a JSON file
with open(output_json, "w") as f:
    json.dump(image_data, f, indent=2)

print(f"✅ Created {output_json} with {len(image_data)} entries.")