import os
from colorama import Fore
from core.utilities.manage_json import read_json, write_json


class Model:

    def __init__(self, table_name: str, path: str = 'src/migrations'):
        self.__table_name = table_name
        self.__path = path
        self.__default_models = 'models.json'
        self.__create_dir()

    def __create_dir(self):
        if not os.path.isdir(self.__path):
            os.mkdir(self.__path)

    def __create_file(self, content: str = ''):
        path = self.__path + '/' + self.__default_models
        if content != '':
            with open(f'{path}', "w", encoding='utf-8') as f:
                f.write(content.encode('utf-8').decode())
                f.close()
            print(Fore.WHITE + 'El archivo ' + Fore.GREEN + f'{path}' + Fore.WHITE + ' fue modificado!')
        else:
            open(f'{path}', "w").close()
            print(Fore.GREEN + 'Se ha creado el siguiente archivo. ' + Fore.WHITE + f'{path}')

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
        if is_exist:
            data[self.__table_name].append(new_table)
        else:
            result = {
                self.__table_name: [new_table]
            }
            data.update(result)
        data[self.__table_name] = sorted(data[self.__table_name], key=lambda x: x['key'])
        write_json(path=path, data=data)

    def load_model(self):
        """
        Carga y crea un modelo tomando como referencia un archivo JSON
        """
        pass

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
