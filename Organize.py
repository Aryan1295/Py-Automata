import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_extension = filename.split('.')[-1]
        destination_folder = os.path.join(folder_path, file_extension)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(os.path.join(folder_path, filename), destination_folder)

folder_path = "path/to/your/folder"
organize_files(folder_path)
