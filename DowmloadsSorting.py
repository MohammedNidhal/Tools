import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define paths and file extensions
DOWNLOADS_FOLDER = r"PATH TO THE FOLDER TO CLEAN (DOWNLOADS)"
FOLDERS = { #File Extensions
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "zip": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "exe": [".exe", ".msi", ".bat"],
    "pdf": [".pdf"]
}

# Function to move files to their respective folders
def move_file(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    for folder, extensions in FOLDERS.items():
        if file_ext.lower() in extensions:
            dest_folder = os.path.join(DOWNLOADS_FOLDER, folder)
            os.makedirs(dest_folder, exist_ok=True)  # Create the folder if it doesn't exist
            shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
            print(f"Moved {file_path} to {dest_folder}")
            break

# Event handler for monitoring the folder
class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            move_file(event.src_path)

# Main function to start tracking
def monitor_downloads():
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()
    
    print(f"Monitoring {DOWNLOADS_FOLDER} for new files...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_downloads()
