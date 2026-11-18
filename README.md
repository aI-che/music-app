# Terminal Music Player

A **Python** terminal app that searches YouTube for a song by name, then **plays it right away** or **saves it as a 192 kbps MP3**.

## Features

- Find songs by name (the best YouTube match is picked automatically)
- Play mode: plays the song in the terminal
- Download mode: saves the song as an MP3 file

## Setup

```bash
pip install -r requirements.txt
```

**FFmpeg** is required. On Windows, download it from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and add its `bin` folder to `PATH`, or copy `ffmpeg.exe` and `ffprobe.exe` next to `main.py`.

## Run

```bash
python main.py
```

## Tech

Python · yt-dlp · Pygame · FFmpeg
