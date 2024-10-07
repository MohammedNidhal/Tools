import os
import csv

def list_directory_elements(directory_path, file_extension=None):
    all_files = os.listdir(directory_path)

    if file_extension:
        filtered_files = [f for f in all_files if f.endswith(file_extension)]
    else:
        filtered_files = all_files  

    csv_file_path = os.path.join(directory_path, 'directory_contents.csv')
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File Name"])  

        for file in filtered_files:
            writer.writerow([file])  

    print(f"CSV file created: {csv_file_path}")

# Usage Example
if __name__ == "__main__":
    directory =r"C:\Users\moham\Desktop"
    extension = r".txt"
    list_directory_elements(directory, extension)
