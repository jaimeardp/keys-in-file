import os


def get_current_path_abs():
    path = os.path.abspath(os.getcwd())
    return path

def create_folder_temp(new_folder):
    try:
        path_formated = os.path.join(get_current_path_abs(), new_folder)
        os.mkdir(path_formated)
        return path_formated
    except:
        return path_formated


def format_path_abs(base_path, filename):
    path_formated = os.path.join(base_path, filename)
    return path_formated