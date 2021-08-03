import os
#import json
#import shutil
import tempfile
from core.command import SpawnCommandLine
#from prompt_toolkit.validation import Validator, ValidationError


def main():

    spawnqs = SpawnCommandLine()

    answers = spawnqs.spawn_questions("actions")

    print(answers)

    try:
        pass

    except KeyError as e:
        print(str(e))
        print(os.path.exists("enviroments"))
    except Exception as e:
        print(str(e))

    try:

        if answers.get("user_option") == "create":
            print("Bienvenido a create option")
            rcreate = spawnqs.spawn_questions("create")
            print(rcreate)
        elif answers.get("user_option") == "validate":
            print("Bienvenido a validate option")
            rvlidate = spawnqs.spawn_questions("validate")
            print(rvlidate)
        elif answers.get("user_option") == "decrypt":
            print("Bienvenido a decrypt option")
    
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()