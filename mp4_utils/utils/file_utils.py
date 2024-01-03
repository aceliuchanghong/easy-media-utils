import os
import shutil


def copy_file(source_path, destination_path):
    video_name = os.path.splitext(os.path.basename(source_path))[0]
    if os.path.exists(destination_path + "/" + video_name + ".mp4"):
        print("copy File already exists in the destination.")
    elif not os.path.exists(source_path):
        print("copy Source file does not exist.")
    else:
        shutil.copy(source_path, destination_path)
        # print("File copied successfully.")


def move_file(source_path, destination_path):
    video_name = os.path.splitext(os.path.basename(source_path))[0]
    if os.path.exists(destination_path + "/" + video_name + ".mp4"):
        print("move File already exists in the destination.")
        os.remove(source_path)
    elif not os.path.exists(source_path):
        print("move Source file does not exist.")
    else:
        shutil.move(source_path, destination_path)
        # print("File moved successfully.")
