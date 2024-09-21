import os
from colorama import Fore
from core.utilities import PathFiles, GeneratorHash
from core.utilities.manage_json import read_json, write_json
from .assets import ModelTemplate


class Model:

    def __init__(self, table_name: str = '', path: str = 'src/migrations', **params: dict):
        self.__table_name = table_name
        self.__path = path
        self.__params = params
        self.__hash_name = GeneratorHash().get_hash()
        self.__default_models = f'models.json'
        self.__default_versions = 'versions'
        self.__create_dir()

    def __create_dir(self, path: str = ''):
        path = self.__path + (f'/{path}' if path else '')
        if not os.path.isdir(path):
            os.mkdir(path)
            print(Fore.GREEN + 'Se creó el siguiente directorio en el proyecto ' + Fore.WHITE + path)

    def __create_file_empty(self, path: str = '', file_name: str = '__init__.py'):
        if path == '':
            path = self.__path + '/' + self.__default_models
        open(f'{path}/{file_name}', "w").close()
        print(Fore.GREEN + 'Se ha creado el siguiente archivo. ' + Fore.WHITE + f'{path}/{file_name}')

    def __create_file(self, path: str = '', content: str = '', action: str = 'a'):
        if path == '':
            path = self.__path + '/' + self.__default_models
        if content != '':
            try:
                with open(f'{path}', action, encoding='utf-8') as f:
                    f.write(content.encode('utf-8').decode())
                    f.close()
                print(Fore.WHITE + 'El archivo ' + Fore.GREEN + f'{path}' + Fore.WHITE + ' fue modificado!')
            except:
                new_file_path = path.split('/')
                print(path)
                self.__create_file_empty(path=new_file_path[0], file_name=new_file_path[1])
                self.__create_file(path=path, content=content)
        else:
            open(f'{path}', "w").close()
            print(Fore.GREEN + 'Se ha creado el siguiente archivo. ' + Fore.WHITE + f'{path}')

    def generate_base_model(self):
        path = PathFiles(dir_name='models').get_root_dir()
        content = ModelTemplate(**{'id': self.__params.get('id', False)}).get_content_base_model()
        self.__create_file(path=path + '/base_model.py', content=content)
        self.__create_file(path=path + '/__init__.py', content='from .base_model import BaseModel\n')

    def create_migration_model(self, key, primary, _type, nullable, default, comment):
        path = self.__path + '/' + self.__default_models
        data = read_json(path=path)
        new_table = {
            "key": key,
            "primary": primary,
            "type": _type,
            "nullable": nullable,
            "default": default,
            "comment": comment,
            "generate": False,
            "generationDate": None
        }
        is_exist = False
        for model in data:
            if self.__table_name in model:
                is_exist = True
                break

        is_new = False
        if is_exist:
            exist_field = [x for x in data[self.__table_name] if x['key'] == new_table['key']]
            if len(exist_field) == 0:
                data[self.__table_name].append(new_table)
                is_new = True
            elif self.__params.get('update', False):
                for model in data[self.__table_name]:
                    if model['key'] == new_table['key']:
                        model['primary'] = new_table['primary']
                        model['type'] = new_table['type']
                        model['nullable'] = new_table['nullable']
                        model['default'] = new_table['default']
                        model['comment'] = new_table['comment']
        else:
            result = {
                self.__table_name: [new_table]
            }
            data.update(result)
        data[self.__table_name] = sorted(data[self.__table_name], key=lambda x: x['key'])
        write_json(path=path, data=data)
        return is_new

    @staticmethod
    def __get_data_env(path: str):
        response = ''
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                if 'DB_NAME' in line:
                    response = (line.split('=')[1]
                                .replace('"', '')
                                .replace(' ', '_')
                                .replace('\n', '')
                                )
                    break
        return response

    def load_model(self):
        self.__create_dir(path=self.__default_versions)
        script_content = ''
        data_models = read_json(path=self.__path + '/' + self.__default_models)
        # TODO: pendiente consultar la cantidad de versiones generadas para agregar un identificado numérico
        #   secuencias que comience en _1
        file_name = self.__path + '/' + self.__default_versions + f'/script_{self.__hash_name}.sql'
        database_name = self.__get_data_env(path='src/.env')
        self.__create_file(path=file_name, content=f'USE DATABASE {database_name};\n\n')

        tables = data_models.keys()
        for model in tables:
            script_content += (ModelTemplate(table_name=model, **{'fields': data_models[model]})
                               .create_table_for_script())

        if script_content:
            self.__create_file(path=file_name, content=script_content)
        if self.__params.get('generate', False):
            exist_base_model, path_base_model = (PathFiles(dir_name='models')
                                                 .get_file_for_path(file_name='base_model.py'))
            path = PathFiles(dir_name='models').get_root_dir()
            for model in tables:
                params = {
                    'fields': data_models[model],
                    'withBaseModel': exist_base_model,
                    'rootPath': PathFiles().get_root_path()
                }
                model_content = (ModelTemplate(table_name=model, **params)
                                 .get_content_model_in_code())
                self.__create_file(path=f'{path}/{model.lower()}_model.py', content=model_content, action='w')
                # TODO: pendiente validar si la importación ya existe en el archivo __init__.py del package models
                import_text = f'from .{model.lower()}_model import {model.title().replace("_", "")}Model\n'
                self.__create_file(path=f'{path}/__init__.py', content=import_text)

    def show_migration_models(self, _all: bool = False):
        data = read_json(path=self.__path + '/' + self.__default_models)
        if _all:
            for model in data:
                text = f"""============================\nTable: {model}\n============================"""
                print(text)
                for field in data[model]:
                    print(field)
        else:
            if self.__table_name in data:
                text = f"""============================\nTable: {self.__table_name}\n============================"""
                print(text)
                for field in data[self.__table_name]:
                    print(field)
            else:
                print(f'Table {self.__table_name} not found')
