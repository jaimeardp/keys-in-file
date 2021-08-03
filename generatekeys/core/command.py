from PyInquirer import prompt, Separator
from core.helper import save_file_config, load_file_config
#import helper

class SpawnCommandLine:
    

    def __init__(self) -> None:
        self.ecmd = EstateCommandLine()

    def spawn_questions(self, node_questions):
        answers: dict
        if node_questions.lower() == "actions":
            answers = prompt(self.ecmd.get_actions())
            try:
                self.ecmd.enviroments = answers["envs"].split(",") # Setting variables enviroments in the state
                # save file of config
                save_file_config(answers)
            except Exception as e:
                print(str(e))
                # load file of config 
                tmp_enviroments = load_file_config()
                print(tmp_enviroments)
                self.ecmd.enviroments = tmp_enviroments.split(",")
                
        elif node_questions.lower() == "create":
            answers = prompt(self.ecmd.get_create())
        elif node_questions.lower() == "validate":
            answers = prompt(self.ecmd.get_validate()) 
        return answers

class EstateCommandLine:

    #validate_choices_list: list = []

    #create_choices_checkbox: list = [Separator('= The Enviroments types ='),]

    enviroments: list

    def __init__(self) -> None:
        pass

    def get_actions(self):
        actions = [
            {
                'type': 'list',
                'name': 'user_option',
                'message': 'Welcome to security keys',
                'choices': ["create","validate","decrypt"]
            },
            {
                'type': 'input',
                'name': 'envs',
                'message': 'Escribe los entornos de desarrollo que quieres generar',
                'when': lambda answers : answers["user_option"] == "create"
            }
        ]
        return actions

    def get_create(self):
        create = [
            {
                'type': 'checkbox',
                'message': 'Select enviroments',
                'name': 'enviroments',
                'choices': [Separator('= The Enviroments types =')] + [{'name': env} for env in self.enviroments],
                'validate': lambda answer: 'You must choose at least one topping.' \
                    if len(answer) == 0 else True
            },
            {
                'type': 'input',
                'name': 'params',
                'message': 'Escribe las palabras de referencia para crear la llave secreta',
            }
        ]
        return create
    
    def get_validate(self):
        validate = [
            {
                'type': 'list',
                'name': 'enviroment_option',
                'message': 'Seleccion el entorno al cual vas a validar',
                'choices': [env for env in self.enviroments]
            }
        ]
        return validate

