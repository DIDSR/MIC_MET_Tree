# utils/images.py

import base64

IMG_BASE_PATH = "img/"

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        print(f"Warning: Image not found at {image_path}")
        return None