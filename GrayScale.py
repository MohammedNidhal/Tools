from PIL import Image
import os

def convert_to_grayscale(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each file in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Check if it's a file and has an image extension
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg','PNG','JPG','JPEG')):
            # Open the image file
            with Image.open(file_path) as img:
                # Convert the image to grayscale
                grayscale_img = img.convert('L')
                
                # Define the path to save the grayscaled image
                output_path = os.path.join(output_dir, file_name)
                
                # Save the grayscaled image
                grayscale_img.save(output_path)

# Example usage:
input_directory = r"Images Directory" # Replace with the path to your images directory
output_directory = r"ImagesGrayScale Directory"  # Replace with the path where you want to save the grayscaled images

convert_to_grayscale(input_directory, output_directory)
