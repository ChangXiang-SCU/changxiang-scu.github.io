import os
from PIL import Image

def crop_and_resize(image_path, output_path, target_width=500, target_height=300):
    try:
        img = Image.open(image_path)
        # Resize width to target_width, maintaining aspect ratio
        w_percent = (target_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
        
        # Crop from top to target_height
        img = img.crop((0, 0, target_width, target_height))
        
        img.save(output_path)
        print(f"Processed {image_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

image_dir = r"c:\Users\Chang\changxiang-scu.github.io\images"
files = [
    "paper_2024_chi.png",
    "paper_2025_autoui.png",
    "paper_2025_aspire.png",
    "paper_2022_iceb.png",
    "paper_2021_iceb.png",
    "paper_2023_chi.png",
    "paper_2025_aaai.png"
]

for f in files:
    input_path = os.path.join(image_dir, f)
    output_path = os.path.join(image_dir, "thumb_" + f)
    if os.path.exists(input_path):
        crop_and_resize(input_path, output_path)
    else:
        print(f"File not found: {input_path}")
