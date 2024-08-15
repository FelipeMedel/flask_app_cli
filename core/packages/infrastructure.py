import os
from os.path import exists
from colorama import Fore
from .assets import (EnvTemplate,
                     RequirementTemplate,
                     ConfigTemplate,
                     ApplicationTemplate)


class Infrastructure:

    def __init__(self, project_name: str, root: str = 'app', with_files: bool = True):
        self.__project_name = project_name
        self.__root_name = f'./{project_name}/src'
        self.__root = root
        self.__with_files = with_files
        self.__DEFAULT_ROUTES = [
            f'./{self.__root_name}/{self.__root}/blueprints',
            f'./{self.__root_name}/{self.__root}/controllers',
            f'./{self.__root_name}/{self.__root}/decorators',
            f'./{self.__root_name}/{self.__root}/middlewares',
            f'./{self.__root_name}/{self.__root}/models',
            f'./{self.__root_name}/{self.__root}/schemas',
            f'./{self.__root_name}/{self.__root}/services',
            f'./{self.__root_name}/{self.__root}/utilities'
        ]

    def create_project_dir(self):
        self.create_dir(path=self.__project_name, is_project=True)

    def create_env_file(self):
        file_name = f'{self.__root_name}/.env'
        if not exists(file_name):
            self.create_file_empty(path=self.__root_name, file_name='.env')
        self.write_file(path=file_name, content=EnvTemplate().get_data())

    def create_requirement_file(self):
        file_name = f'{self.__project_name}/requirements.txt'
        if not exists(file_name):
            self.create_file_empty(path=self.__project_name, file_name='requirements.txt')
        self.write_file(path=file_name, content=RequirementTemplate().load_dependencies())

    def create_all_dir(self):
        # Add sources dir
        if not os.path.isdir(self.__root_name):
            self.create_dir()
            # create run and wsgi
            self.create_file_empty(path=self.__root_name, file_name='run.py')
            self.write_file(path=f'{self.__root_name}/run.py', content=ApplicationTemplate().get_content_run())
            self.create_file_empty(path=self.__root_name, file_name='wsgi.py')
            self.write_file(path=f'{self.__root_name}/wsgi.py',
                            content=ApplicationTemplate(develop=False).get_content_run())

        # Add settings dir
        if not os.path.isdir(f'./{self.__root_name}/settings'):
            self.create_config_dir()

        # Add root application dir
        if not os.path.exists(f'./{self.__root_name}/{self.__root}'):
            self.create_dir(path=f'./{self.__root_name}/{self.__root}')
            open(f'./{self.__root_name}/{self.__root}/__init__.py', "w").close()
            # writer __init__ application
            self.write_file(path=f'./{self.__root_name}/{self.__root}/__init__.py',
                            content=ApplicationTemplate().get_content_application())

        # Add subdirectories on root application
        if self.__with_files:
            # Add .env file
            self.create_env_file()
            self.create_requirement_file()
            # Add init package dir
            for route in self.__DEFAULT_ROUTES:
                if not os.path.exists(route):
                    self.create_dir(path=route)
                    open(f'{route}/__init__.py', "w").close()

    def create_dir(self, path: str = '', is_project: bool = False):
        if path == '':
            path = self.__root_name
        os.mkdir(path)

        if is_project:
            print(Fore.BLUE + f'El proyecto {path} se a creado correctamente!')
        else:
            print(Fore.GREEN + 'Se creó el siguiente directorio en el proyecto' + Fore.WHITE + path)
            if self.__with_files:
                self.create_file_empty(path=path)

    def create_file_empty(self, path: str = '', file_name: str = '__init__.py'):
        if path == '':
            path = self.__root_name
        open(f'{path}/{file_name}', "w").close()
        print(Fore.GREEN + 'Se ha creado el siguiente archivo.' + Fore.WHITE + f'{path}/{file_name}')

    def write_file(self, path: str = '', content: str = ''):
        if path == '':
            path = self.__root_name
        with open(f'{path}', "w") as f:
            f.write(content)
            f.close()
        print(Fore.WHITE + 'El archivo ' + Fore.GREEN + f'{path}' + Fore.WHITE + ' fue modificado!')

    def create_config_dir(self):
        setting_dir = f'./{self.__root_name}/settings'
        os.mkdir(setting_dir)
        print(Fore.GREEN + 'El directorio settings fue creado!')
        self.create_file_empty(path=setting_dir)
        self.write_file(path=f'{setting_dir}/__init__.py', content=ConfigTemplate().get_content_import_file())
        self.create_file_empty(path=setting_dir, file_name='config.py')
        self.write_file(path=f'{setting_dir}/config.py', content=ConfigTemplate().get_content_file())

