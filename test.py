import os
from moviepy.editor import VideoFileClip

def get_total_duration(directory):
    total_duration = 0.0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.m4v'):
                print(file)
                file_path = os.path.join(root, file)
                with VideoFileClip(file_path) as video:
                    total_duration += video.duration
                
    return total_duration

def main():
    directory_path = input() #e.g: C:\Folder\Inner Folder
    total_duration = get_total_duration(directory_path)
    print(f"Total duration of all videos: {total_duration} seconds")
    hours = total_duration // 3600
    minutes = (total_duration % 3600) // 60
    seconds = total_duration % 60
    print(f"Total duration: {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")

if __name__ == "__main__":
    main()
