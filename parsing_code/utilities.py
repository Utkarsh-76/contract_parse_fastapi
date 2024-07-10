import os
from dir_path import base_dirname


def empty_temp_folder():
    """
    delete all files from the temp folder
    """

    temp_folder = os.path.join(base_dirname, 'data', 'temp')

    files = os.listdir(temp_folder)
    for file_name in files:
        file_path = os.path.join(temp_folder, file_name)
        os.remove(file_path)


def get_folder(folder_):
    if not os.path.exists(folder_):
        os.makedirs(folder_)

    return folder_
