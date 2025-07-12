#!/usr/bin/env python3
import subprocess
import sys
import os
from time import sleep

def download_dailymotion_video(url, output_path="."):
    """
    Download a DailyMotion video using yt-dlp
    
    Args:
        url (str): URL of the DailyMotion video
        output_path (str): Directory to save the video (default: current directory)
    Returns:
        bool: True if download succeeded, False if failed
    """
    try:
        print(f"\nDownloading video from {url}...")
        result = subprocess.run([
            "yt-dlp",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            "--merge-output-format", "mp4",
            "--no-warnings",
            url
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Download completed successfully!")
            return True
        else:
            print(f"Error downloading video: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def process_url_file(file_path, output_path=".", delay=5):
    """
    Process a text file containing DailyMotion URLs
    
    Args:
        file_path (str): Path to text file with URLs
        output_path (str): Directory to save videos
        delay (int): Seconds to wait between downloads
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return
        
    try:
        # Check if yt-dlp is installed
        subprocess.run(["yt-dlp", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("Error: yt-dlp is not installed. Please install it first:")
        print("pip install yt-dlp")
        return
    except subprocess.CalledProcessError:
        print("Error: yt-dlp is not working properly")
        return

    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
        
    total = len(urls)
    print(f"Found {total} URLs to process in {file_path}")
    
    for i, url in enumerate(urls, 1):
        print(f"\nProcessing URL {i} of {total}")
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        success = download_dailymotion_video(url, output_path)
        
        if not success:
            print(f"Failed to download: {url}")
            
        if i < total:  # No delay after last download
            print(f"Waiting {delay} seconds before next download...")
            sleep(delay)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dailymotion_batch_downloader.py <urls_file.txt> [output_directory] [delay_seconds]")
        print("Example: python dailymotion_batch_downloader.py my_videos.txt ./downloads 10")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "."
    delay = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    
    process_url_file(file_path, output_path, delay)
