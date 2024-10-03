import os
import shutil

# Define the source and destination directories
source_dir =r"D:\Archive\Untouched Data\Images"# Replace with your source directory
dest_dir = r"D:\Archive\Untouched Data\Images"# Replace with your destination directory

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Walk through the source directory
for root, dirs, files in os.walk(source_dir):
    #Skip the source directory itself
    if root == source_dir:
        continue
    
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, os.path.join(dest_dir, file))

print("All files have been moved to the destination directory.")
