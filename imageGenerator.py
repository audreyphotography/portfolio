import os
import json

# Root image folder
image_root = "images"
output_json = "imagesJsonFile.json"

# Supported extensions (case-insensitive)
valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".JPG", ".JPEG", ".PDF"}

# Collected image data
image_data = []

for category in os.listdir(image_root):
    category_path = os.path.join(image_root, category)
    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            # Remove leading ._ if present
            clean_name = filename
            if filename.startswith("._"):
                clean_name = filename[2:]
            ext = os.path.splitext(clean_name)[1].lower()
            if ext in valid_extensions:
                image_data.append({
                    "src": f"{image_root}/{category}/{clean_name}",
                    "category": category
                })

# Save to JSON
with open(output_json, "w") as f:
    json.dump(image_data, f, indent=2)

print(f"✅ Created {output_json} with {len(image_data)} entries.")