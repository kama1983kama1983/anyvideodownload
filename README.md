# Universal Video Downloader

A Python script to download videos from any supported website (YouTube, Dailymotion, Vimeo, etc.) with resolution selection.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 📹 Download videos from 1000+ supported websites
- 🎚️ Select specific resolution (480p, 720p, 1080p, etc.)
- 📁 Batch download from text files
- ⏲️ Configurable delay between downloads
- 🛡️ Safe filename handling
- ✅ Automatic format selection

## Supported Websites

Works with all sites supported by yt-dlp including:
- YouTube
- Dailymotion
- Vimeo
- Twitter
- Facebook
- Instagram
- TikTok
- Twitch clips
- And [1000+ more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/universal-video-downloader.git
cd universal-video-downloader
```

2. Install dependencies:
```bash
pip install yt-dlp
```

## Usage

### Basic Command
```bash
python universal_video_downloader.py urls.txt
```

### Full Options
```bash
python universal_video_downloader.py <input_file> [output_directory] [delay_seconds] [resolution]
```

### Examples
1. Download videos at best quality:
```bash
python universal_video_downloader.py my_videos.txt
```

2. Download at 720p to specific folder:
```bash
python universal_video_downloader.py urls.txt ./videos 5 720p
```

3. Download from mixed sources (YouTube, Twitter, etc.):
```bash
python universal_video_downloader.py mixed_urls.txt ./downloads
```

### Input File Format
Create a text file with one URL per line:
```
https://www.youtube.com/watch?v=example1
https://vimeo.com/example2
https://twitter.com/example3
```

## Configuration Options

| Parameter       | Description                          | Default   |
|-----------------|--------------------------------------|-----------|
| input_file      | Text file containing URLs            | Required  |
| output_directory| Where to save downloaded videos      | ./        |
| delay_seconds   | Delay between downloads              | 5         |
| resolution      | Video resolution (e.g., 720p)       | Best available |

## Troubleshooting

**Error: yt-dlp not found**  
Install it with: `pip install yt-dlp`

**Error: Invalid URL**  
Ensure URLs start with http:// or https://

**Some sites not working**  
Update yt-dlp: `pip install --upgrade yt-dlp`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

💡 **Tip**: For the best experience, keep yt-dlp updated regularly as video sites change their APIs frequently.
```

This README includes:

1. Clear title and badges
2. Feature list with emojis
3. Installation instructions
4. Detailed usage examples
5. Input file format explanation
6. Configuration options table
7. Troubleshooting section
8. License and contribution info

The formatting uses GitHub-Flavored Markdown and includes:
- Code blocks for commands
- Tables for parameters
- Emojis for visual organization
- Links to external resources

You can copy this directly to a `README.md` file in your project root. For the license mentioned, you'll need to create a separate `LICENSE` file with the MIT license text.
