import os
import time
import ctypes
from PIL import Image

# Define constants
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

def set_wallpaper(image_path):
    # Convert image to BMP format if not already
    if not image_path.lower().endswith('.bmp'):
        bmp_path = image_path.rsplit('.', 1)[0] + '.bmp'
        with Image.open(image_path) as img:
            img.save(bmp_path, 'BMP')
        image_path = bmp_path
    
    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

def change_wallpaper(directory, interval):
    images = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    if not images:
        print("No images found in the directory.")
        return
    
    while True:
        for image_name in images:
            image_path = os.path.join(directory, image_name)
            set_wallpaper(image_path)
            time.sleep(interval)

if __name__ == "__main__":
    # Change these variables as needed
    image_directory = r"D:\Football\FC Barcelona"  # Directory containing images
    change_interval = 10  # Time in seconds to change wallpaper

    change_wallpaper(image_directory, change_interval)
