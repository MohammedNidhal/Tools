import yt_dlp

def download_youtube_video(video_url, download_path='./'):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'format': 'best',  # Downloads the best quality video available
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f'Download completed! Video saved to: {download_path}')
    except Exception as e:
        print(f'An error occurred: {e}')
# Example usage
if __name__ == "__main__":
    video_url = r"YoutubeURL"
    download_youtube_video(video_url,)
