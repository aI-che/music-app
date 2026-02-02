import yt_dlp
import pygame
import os

def playmusic(song_name):
    print(f"Now playing: {song_name}")
    
    # Check for existing temporary file and remove it
    if os.path.exists("current_song.mp3"):
        try:
            # Stop any music playing to release the file lock
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
            os.remove("current_song.mp3")
        except Exception as e:
            print(f"Could not remove old file: {e}")

    settings = {
        'format': 'bestaudio/best',
        'outtmpl': 'current_song.%(ext)s',  # Renamed from calinan_sarki
        'default_search': 'ytsearch',   
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(settings) as ydl:
            ydl.download([song_name])
        
        # Initialize mixer if not already initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        pygame.mixer.music.load('current_song.mp3')
        pygame.mixer.music.play()

    except Exception as e:
        print(f"Something went wrong: {e}")

def download(song_name):
    print("Song is being downloaded...")

    settings = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',   
        'default_search': 'ytsearch',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(settings) as ydl:
            ydl.download([song_name])
        print("Song downloaded successfully.") # Fixed typo
    except Exception as e:
        print(f"Something went wrong: {e}")


# --- Main Loop ---
print("WELCOME TO MY MUSIC APP")

while True:
    print("-" * 30)
    print("1. Play a song")
    print("2. Download a song (MP3)")
    print("q. Quit")

    choose = input("Enter your choice: ") # Translated
    
    if choose == '1':
         search = input("Enter song name: ") # Translated
         playmusic(search)
         input("Press Enter to continue...")
    elif choose == '2':
         search = input("Enter song name: ") # Translated
         download(search)
         input("Press Enter to continue...")
    elif choose == 'q':
        print("Bye bye!")
        try:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            
            # Clean up the temporary file
            if os.path.exists("current_song.mp3"):
                os.remove("current_song.mp3")
        except:
            pass
        break
    else:
        print("Invalid value")
        input("Press Enter to try again...")