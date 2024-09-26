import yt_dlp
import os
url = r"url of the youtube playlist"
download_directory = r"PATH OF THE DOWNLOAD LOCATION Directory"

L=["https://www.youtube.com/watch?v=BKLW6JjU-iU&list=PLZbyDagGD6qkMlCxh6HRJK-ZfNxjsO9ow"]
# Ensure the directory exists
os.makedirs(download_directory, exist_ok=True)

# Define options for yt-dlp
ydl_opts = {
    'format': 'best',  # Download the best video and audio format in one file if available
    'noplaylist': False,  # Set to True if you only want to download a single video from the playlist
    'abort-on-error': True,  # Stop the script if any error occurs
    'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),  # Output template with the specified path
    'postprocessors': [],  # No post-processing, no merging
}

# Create a yt-dlp instance with the specified options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
