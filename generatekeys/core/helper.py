import os
import tempfile

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


def save_file_config(answers: dict) -> bool: 
    with tempfile.NamedTemporaryFile(dir=os.path.dirname("enviroments")) as f:
        print(f.name)
        #shutil.copy(f.name, 'enviroments2021')
        os.link(f.name, "enviroments")
        enviroments_str = "".join(answers["envs"])
        f.write(b"" + enviroments_str.encode())
        print(os.path.exists(f.name))
    return os.path.exists("enviroments")

def load_file_config():
    enviroments: str = ""
    with open("enviroments", "r+") as f:
        enviroments = f.read()
    print("Texto leido del archivo temporal : ", enviroments)
    return enviroments