import os


def get_current_path_abs():
    """
        get current path
    """
    path = os.path.abspath(os.getcwd())
    return path

def create_folder_temp(new_folder):
    """
        create folder if not exist
    """
    try:
        path_formated = os.path.join(get_current_path_abs(), new_folder)
        os.mkdir(path_formated)
        return path_formated
    except:
        return path_formated


def format_path_abs(base_path, filename):
    """
        format and concat parent path with child (or filename) path
    """
    path_formated = os.path.join(base_path, filename)
    return path_formated