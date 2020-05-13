import os

from moviepy.editor import VideoFileClip


def convert():
    file_list_with_extension = os.listdir("songs")

    for file in file_list_with_extension:
        file_list = os.path.splitext(file)[0]
        file_mp3 = file_list + ".mp3"
        mp4 = VideoFileClip(os.path.join("songs", file))
        mp4.audio.write_audiofile(os.path.join("songs", file_mp3))
        mp4.close()

    for file in file_list_with_extension:
        file_extension = os.path.splitext(file)[-1]

        if os.path.isfile("songs" + "/" + file) and file_extension == ".mp4":
            os.remove("songs" + "/" + file)
