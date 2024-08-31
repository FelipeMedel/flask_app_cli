import os
from os.path import exists
from colorama import Fore
from .assets import (EnvTemplate,
                     RequirementTemplate,
                     ConfigTemplate,
                     ApplicationTemplate,
                     DatabaseTemplate)


class Infrastructure:

    def __init__(self, project_name: str, root: str = 'app', with_files: bool = True,
                 multitenant: bool = False, with_db: bool = False):
        self.__project_name = project_name
        self.__root_name = f'{project_name}/src'
        self.__root = root
        self.__with_files = with_files
        self.__with_db = with_db
        self.__multitenant = multitenant
        if not self.__with_db:
            self.__multitenant = False
        self.__DEFAULT_ROUTES = [
            f'{self.__root_name}/{self.__root}/blueprints',
            f'{self.__root_name}/{self.__root}/controllers',
            f'{self.__root_name}/{self.__root}/decorators',
            f'{self.__root_name}/{self.__root}/middlewares',
            f'{self.__root_name}/{self.__root}/models',
            f'{self.__root_name}/{self.__root}/schemas',
            f'{self.__root_name}/{self.__root}/services',
            f'{self.__root_name}/{self.__root}/utilities'
        ]

    def __create_env_file(self):
        file_name = f'{self.__root_name}/.env'
        if not exists(file_name):
            self.__create_file_empty(path=self.__root_name, file_name='.env')
        self.__write_file(path=file_name, content=EnvTemplate(with_db=self.__with_db).get_data())

    def __create_requirement_file(self):
        file_name = f'{self.__project_name}/requirements.txt'
        if not exists(file_name):
            self.__create_file_empty(path=self.__project_name, file_name='requirements.txt')
        self.__write_file(path=file_name, content=RequirementTemplate(with_db=self.__with_db).load_dependencies())

    def __create_dir(self, path: str = '', is_project: bool = False):
        if path == '':
            path = self.__root_name
        os.mkdir(path)

        if is_project:
            print(Fore.BLUE + f'El proyecto {path} se a creado correctamente!')
        else:
            print(Fore.GREEN + 'Se creó el siguiente directorio en el proyecto ' + Fore.WHITE + path)
            if self.__with_files:
                self.__create_file_empty(path=path)

    def __create_file_empty(self, path: str = '', file_name: str = '__init__.py'):
        if path == '':
            path = self.__root_name
        open(f'{path}/{file_name}', "w").close()
        print(Fore.GREEN + 'Se ha creado el siguiente archivo. ' + Fore.WHITE + f'{path}/{file_name}')

    def __write_file(self, path: str = '', content: str = ''):
        if path == '':
            path = self.__root_name
        with open(f'{path}', "w") as f:
            f.write(content)
            f.close()
        print(Fore.WHITE + 'El archivo ' + Fore.GREEN + f'{path}' + Fore.WHITE + ' fue modificado!')

    def __create_config_dir(self):
        setting_dir = f'{self.__root_name}/settings'
        os.mkdir(setting_dir)
        print(Fore.GREEN + 'El directorio settings fue creado!')
        self.__write_file(path=f'{setting_dir}/__init__.py', content=ConfigTemplate().get_content_import_file())
        self.__write_file(path=f'{setting_dir}/config.py',
                          content=ConfigTemplate(multitenant=self.__multitenant,
                                                 with_db=self.__with_db)
                          .get_content_file())

    def __create_documentation_dir(self):
        setting_dir = f'{self.__root_name}/documentation'
        os.mkdir(setting_dir)
        print(Fore.GREEN + 'El directorio documentation fue creado!')
        self.__create_file_empty(path=setting_dir, file_name='apidoc.json')

    def __create_config_files_multitenant(self):
        database_dir = f'{self.__root_name}/database'
        os.mkdir(database_dir)
        print(Fore.GREEN + 'El directorio database fue creado!')
        db_template = DatabaseTemplate()
        self.__write_file(path=f'{database_dir}/__init__.py', content=db_template.get_import_init())
        self.__write_file(path=f'{database_dir}/db_tenants.py', content=db_template.get_database_config())

    def create_project_dir(self):
        self.__create_dir(path=self.__project_name, is_project=True)

    def create_all_dir(self):
        # Add sources dir
        if not os.path.isdir(self.__root_name):
            self.__create_dir()
            # create run and wsgi
            self.__write_file(path=f'{self.__root_name}/run.py', content=ApplicationTemplate().get_content_run())
            self.__write_file(path=f'{self.__root_name}/wsgi.py',
                              content=ApplicationTemplate(develop=False).get_content_run())

        # Add settings dir
        if not os.path.isdir(f'{self.__root_name}/settings'):
            self.__create_config_dir()

        # Add root application dir
        if not os.path.exists(f'{self.__root_name}/{self.__root}'):
            self.__create_dir(path=f'{self.__root_name}/{self.__root}')
            open(f'{self.__root_name}/{self.__root}/__init__.py', "w").close()
            # writer __init__ application
            self.__write_file(path=f'{self.__root_name}/{self.__root}/__init__.py',
                              content=ApplicationTemplate().get_content_application())

        # Add documentation dir
        if not os.path.exists(f'{self.__root_name}/documentation'):
            self.__create_documentation_dir()

        if self.__multitenant:
            # Add multitenant dir
            if not os.path.exists(f'{self.__root_name}/database'):
                self.__create_config_files_multitenant()

        # Add .env file
        self.__create_env_file()
        self.__create_requirement_file()

        # Add subdirectories on root application
        if self.__with_files:
            # Add init package dir
            for route in self.__DEFAULT_ROUTES:
                if not os.path.exists(route):
                    self.__create_dir(path=route)
                    open(f'{route}/__init__.py', "w").close()
