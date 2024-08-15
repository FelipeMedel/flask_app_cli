import platform
from colorama import Fore, Back, Style


class Credits:

    def __init__(self, title: str):
        self.__title = title

    def get_finish_project(self):
        if self.__title == '':
            print(Back.RED + 'ERROR: Project Name not found')
        else:
            print('-------------------------------------\n')
            print('Gracias por utilizar FLASK APP CLI\n')
            print()
            print(Fore.GREEN + 'Recomendación:\n')
            print('La solución que brinda Flask App Cli, es una referencia en la arquitectura de directorios,')
            print('esto quiere decir, que puedes modificarla y ajustarla según sea la necesidad del proyecto que')
            print('acabas de generar.')
            print()
            print('-------------------------------------\n')
            print(Fore.BLUE + f'El proceso de creación del proyecto {self.__title} finalizó correctamente!')
            print()
            print(Fore.YELLOW + 'Acceda a la raíz del proyecto:')
            print(Back.CYAN + Style.BRIGHT + f"cd {self.__title}")
            print(Fore.YELLOW + 'Crear el entorno virtual: (Recuerda agregar este directorio en el archivo .gitignore)')
            print(Back.CYAN + Style.BRIGHT + "python -m venv .venv")
            if 'windows' in platform.platform().lower():
                print(Fore.YELLOW + 'Activar el entorno virtual: (Windows)')
                print(Back.CYAN + Style.BRIGHT + ".venv/Scripts/activate")
            else:
                print(Fore.YELLOW + 'Activar el entorno virtual: (Linux, Mac)')
                print(Back.CYAN + Style.BRIGHT + "source .venv/bin/activate")
            print(Fore.YELLOW + 'Instalar las dependencias:')
            print(Back.CYAN + Style.BRIGHT + "pip install -r requirements.txt")
