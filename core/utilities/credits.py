import platform
from colorama import Fore, Back, Style
from pyfiglet import Figlet


class Credits:

    def __init__(self, title: str):
        self.__title = title
        self.APP_NAME = 'Flask APP CLI'

    def get_finish_project(self):
        if self.__title == '':
            print(Back.RED + 'ERROR: Project Name not found')
        else:
            print('-------------------------------------\n')
            f = Figlet(font='slant', justify='center')
            print(f.renderText(self.APP_NAME))
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
            print(Fore.CYAN + f"cd {self.__title}")
            print(Fore.YELLOW + 'Crear el entorno virtual: (Recuerda agregar este directorio en el archivo .gitignore)')
            print(Fore.CYAN + "python -m venv .venv")
            if 'windows' in platform.platform().lower():
                print(Fore.YELLOW + 'Activar el entorno virtual: (Windows)')
                print(Fore.CYAN + ".venv/Scripts/activate")
            else:
                print(Fore.YELLOW + 'Activar el entorno virtual: (Linux, Mac)')
                print(Fore.CYAN + "source .venv/bin/activate")
            print(Fore.YELLOW + 'Instalar las dependencias:')
            print(Fore.CYAN + "pip install -r requirements.txt")
            print(Fore.YELLOW + 'Ejecutar la aplicación:')
            print(Fore.CYAN + "python ./src/run.py")
            print(Fore.YELLOW + 'El proyecto se ejecutará en: http://127.0.0.1:5000')

