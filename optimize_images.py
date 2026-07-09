import os
from PIL import Image

ASSETS_DIR = r"c:\Users\j3ll0\.gemini\antigravity\scratch\dog_trainer_website\assets"
MAX_SIZE = (800, 600)

def optimize_image(filepath):
    try:
        with Image.open(filepath) as img:
            # We don't want to optimize gifs or svgs, only jpeg, jpg, webp, png
            if img.format not in ['JPEG', 'WEBP', 'PNG']:
                return

            original_size = os.path.getsize(filepath)
            
            # Convert RGBA to RGB for JPEG
            if img.format == 'JPEG' and img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize if needed (maintains aspect ratio)
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            
            # Save it back with compression
            quality = 85
            temp_filepath = filepath + ".tmp"
            
            # Try saving and checking size until it's under 200KB or quality drops to 20
            while True:
                img.save(temp_filepath, format=img.format, quality=quality, optimize=True)
                new_size = os.path.getsize(temp_filepath)
                if new_size <= 200 * 1024 or quality <= 20:
                    break
                quality -= 5

            # Replace original with optimized
            os.replace(temp_filepath, filepath)
            print(f"Optimized {os.path.basename(filepath)}: {original_size // 1024}KB -> {new_size // 1024}KB")

    except Exception as e:
        print(f"Failed to optimize {filepath}: {e}")

if __name__ == "__main__":
    for filename in os.listdir(ASSETS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
            filepath = os.path.join(ASSETS_DIR, filename)
            optimize_image(filepath)
    print("Optimization complete.")
