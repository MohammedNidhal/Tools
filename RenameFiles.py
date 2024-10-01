import os

def rename_files_in_directory(directory, prefix="", start_number=1, padding=0):
    """Rename all files in the specified directory in a given order."""
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    
    # Supported file extensions
    file_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'] # Example of renaming image files
    
    # Get all file files in the directory
    file_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in file_extensions]
    
    # Sort the files to maintain a consistent order
    file_files.sort()
    
    for i, filename in enumerate(file_files):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        
        # Generate the new name with the given prefix, padded number, and extension
        new_name = f"{str(start_number + i)}{ext}"
        
        # Create the full old and new paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
directory_path = r"Directory of the file extensions to modify"
rename_files_in_directory(directory_path, prefix="file_", start_number=1, padding=3) # Rename it with numbers (sequential data to easily identify the files when treating them)
