# 🎵 Terminal Music Player & Downloader

Stream YouTube songs instantly or download them as MP3s using your terminal.

## ✨ Features

* **Stream Mode:** Listen to songs instantly using `ffplay` (saves disk space).
* **Download Mode:** Save songs as MP3 (192kbps) with metadata.
* **Search:** Automatically finds the best match on YouTube.
* **Lightweight:** Runs entirely in your terminal.

---

## ⚙️ Installation & Requirements

⚠️ **Important:** For this application to work correctly, **`ffplay`** and **`ffprobe`** must be installed on your system. These are included in the FFmpeg package.

### How to Install FFmpeg (Windows)

1.  **Download:** Go to [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/) and download the file named `ffmpeg-git-full.7z` (or .zip).
2.  **Extract:** Unzip the downloaded file. You will see a folder named `bin`.
3.  **Setup:**
    * Inside the `bin` folder, you will find `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe`.
    * **Option A (Easy):** Copy these 3 files and paste them directly into the same folder as this project's `main.py` file.
    * **Option B (Recommended):** Move the extracted folder to `C:\ffmpeg` and add `C:\ffmpeg\bin` to your System Environment Variables (PATH).

### How to Install Python Libraries

Once FFmpeg is ready, install the required Python library:

```bash
pip install -r requirements.txt