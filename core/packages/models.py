import os
from colorama import Fore
from core.utilities import PathFiles
from core.utilities.manage_json import read_json, write_json
from .assets import ModelTemplate


class Model:

    def __init__(self, table_name: str = '', path: str = 'src/migrations', **params: dict):
        self.__table_name = table_name
        self.__path = path
        self.__params = params
        self.__default_models = 'models.json'
        self.__default_versions = 'versions'
        self.__create_dir()

    def __create_dir(self, path: str = ''):
        path = self.__path + (f'/{path}' if path else '')
        if not os.path.isdir(path):
            os.mkdir(path)
            print(Fore.GREEN + 'Se creó el siguiente directorio en el proyecto ' + Fore.WHITE + path)

    def __create_file(self, path: str = '', content: str = ''):
        if path == '':
            path = self.__path + '/' + self.__default_models
        if content != '':
            with open(f'{path}', "a", encoding='utf-8') as f:
                f.write(content.encode('utf-8').decode())
                f.close()
            print(Fore.WHITE + 'El archivo ' + Fore.GREEN + f'{path}' + Fore.WHITE + ' fue modificado!')
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
            "comment": comment
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

    def load_model(self):
        self.__create_dir(path=self.__default_versions)
        # TODO: pendiente por procesar el archivo models.json y generar el archivo de versiones,
        #  como también el método para generar el código del modelo

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
