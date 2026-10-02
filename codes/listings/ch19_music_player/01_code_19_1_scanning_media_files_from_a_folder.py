# Desktop Audio Player and Frequency Visualizer -- Code 19.1: Scanning media files from a folder
# (book source: ch19_music_player.tex, line 37)

import os

def load_music_folder(folder_path):
    valid_extensions = ('.mp3', '.wav', '.ogg', '.flac')
    playlist_files = []
    
    for file in os.listdir(folder_path):
        if file.lower().endswith(valid_extensions):
            full_path = os.path.join(folder_path, file)
            playlist_files.append((file, full_path))
            
    return playlist_files
