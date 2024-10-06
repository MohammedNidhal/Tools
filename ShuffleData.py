import os
import random
import shutil


base_dir = r"C:\Users\moham\Desktop\Stage2\Existing Models\dataset"
categories = ["B&L", "B&R", "Back", "BackLeft", "BackRight", "F&L", "F&R", "Front", "FrontLeft", "FrontRight", "Left", "Right"]
image_dir = os.path.join(base_dir, "images")
label_dir = os.path.join(base_dir, "labels")

# Create train and validate directories if they don't exist
train_image_dir = os.path.join(image_dir, "train")
validate_image_dir = os.path.join(image_dir, "val")
train_label_dir = os.path.join(label_dir, "train")
validate_label_dir = os.path.join(label_dir, "val")

os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(validate_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(validate_label_dir, exist_ok=True)

# Supported image formats
image_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.JPEG', '.JPG')

# Collect all image and label file paths
image_paths = []
label_paths = []

for category in categories:
    category_dir = os.path.join(base_dir, category)
    for filename in os.listdir(category_dir):
        if filename.endswith(image_formats):
            image_paths.append(os.path.join(category_dir, filename))
            label_paths.append(os.path.join(category_dir, os.path.splitext(filename)[0] + ".txt"))

# Shuffle and split the data
data = list(zip(image_paths, label_paths))
random.shuffle(data)
split_idx = int(0.8 * len(data))

train_data = data[:split_idx]
validate_data = data[split_idx:]

# Helper function to copy files
def copy_files(data, target_image_dir, target_label_dir):
    for image_path, label_path in data:
        shutil.copy(image_path, target_image_dir)
        shutil.copy(label_path, target_label_dir)

# Copy training data
copy_files(train_data, train_image_dir, train_label_dir)

# Copy validation data
copy_files(validate_data, validate_image_dir, validate_label_dir)

print(f"Training data: {len(train_data)} images")
print(f"Validation data: {len(validate_data)} images")
