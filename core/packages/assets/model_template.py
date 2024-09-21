

class ModelTemplate:

    def __init__(self, table_name: str = 'TableName', **params):
        self.__table_name = table_name
        self.__params: dict = params

    def __create_table(self):
        script = f"""create table if not exist {self.__table_name} """
        script += '\n(\n'
        data = self.__params.get('fields', [])
        first_lap = True
        for column in data:
            if len(data) > 1 and not first_lap:
                script += ',\n'

            if first_lap:
                first_lap = False

            if column['primary']:
                script += f"\t{column['key']} INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria'"
            else:
                default = ''
                comment = ''
                nullable = 'NULL'
                if column['default']:
                    default = f"DEFAULT '{column['default']}'"
                if column['nullable']:
                    nullable = 'NOT NULL'
                if column['comment']:
                    comment = f"COMMENT '{column['comment']}'"
                script += f'\t{column["key"]} {column["type"]} {nullable} {default} {comment}'
        script += '\n);\n'
        return script

    @staticmethod
    def __get_column_type(_type):
        if 'varchar' in _type:
            size = _type.replace('varchar', '')
            return f'String{size}'
        elif 'date' in _type or 'datetime' in _type:
            return 'DateTime'
        elif _type.upper() in ('JSON', 'TEXT', 'LONGTEXT', 'TINYINT'):
            return _type.upper()
        return 'Integer'

    @staticmethod
    def __get_import_types(columns: dict, _type: str = 'standard'):
        response = {
            'standard': [],
            'special': []
        }
        for column in columns:
            column_type = column['type'].lower()

            if column_type.upper() in response[_type]:
                continue

            if 'varchar' in column_type:
                if 'String' in response[_type]:
                    continue
                response['standard'].append('String')
            elif 'int' in column_type and column['primary']:
                continue
            elif 'int' == column_type:
                if 'Integer' in response[_type]:
                    continue
                response['standard'].append('Integer')
            elif 'datetime' in column_type or 'date' in column_type:
                if 'DateTime' in response[_type]:
                    continue
                response['standard'].append('DateTime')
            elif 'text' in column_type:
                response['special'].append('TEXT')
            elif 'longtext' in column_type:
                response['special'].append('LONGTEXT')
            elif 'json' in column_type:
                response['special'].append('JSON')
            elif 'tinyint' in column_type:
                response['special'].append('TINYINT')

        result = ''
        if len(response[_type]) > 0:
            if _type == 'standard':
                result = f'{", ".join(response[_type])}'
            elif _type == 'special':
                result = f'from sqlalchemy.dialects.mysql import {", ".join(response[_type])}'
        return result

    def __get_content_model(self):
        columns = self.__params.get('fields', dict())
        with_base_model = self.__params.get('withBaseModel')
        content = f'from sqlalchemy import Column, {self.__get_import_types(columns=columns)}\n'
        content += f'{self.__get_import_types(columns=columns, _type="special")}\n'
        if with_base_model:
            content += 'from . import BaseModel\n'
        else:
            root_path = self.__params.get('rootPath', 'app')
            content += f'from {root_path} import db\n'
        content += '\n\n'
        model_name = self.__table_name.title().replace('_', '')
        if with_base_model:
            content += f'class {model_name}Model(BaseModel):\n'
        else:
            content += f'class {model_name}Model(db.Model):\n'
        content += '\n'
        content += f'\t__tablename__ = "{self.__table_name}"\n'
        content += '\n'
        for column in columns:
            if with_base_model and column['primary']:
                continue

            content += (f"\t{column['key']} = Column({self.__get_column_type(_type=column['type'])}, "
                        f"nullable={column['nullable']}")
            if column['nullable']:
                if column['default'] == 'null':
                    column['default'] = None
                content += f", default={column['default']}"
            if column['comment']:
                content += f", comment='{column['comment']}'"
            content += ")\n"

        content += '\n'
        return content

    def get_content_base_model(self):
        content = 'from typing import Union, List\n'
        content += f'from {self.__params.get("root", "app")} import db\n'
        content += '\n\n'
        content += 'class BaseModel(db.Model):\n'
        content += '\t__abstract__ = True\n'
        content += '\n'
        if self.__params.get('id', False):
            content += '\tid = db.Column(db.Integer, primary_key=True, nullable=False)\n'
        content += '\n'
        content += '\tdef delete(self):\n'
        content += '\t\ttry:\n'
        content += '\t\t\tdb.session.delete(self)\n'
        content += '\t\t\tdb.session.commit()\n'
        content += '\t\texcept Exception as e:\n'
        content += "\t\t\tprint(f'Error DELETE: {e}')\n"
        content += '\t\t\tdb.session.rollback()\n'
        content += '\n'
        content += '\tdef save(self, commit: bool =True):\n'
        content += '\t\ttry:\n'
        content += '\t\t\tdb.session.add(self)\n'
        content += '\t\t\tdb.session.flush()\n'
        content += '\t\t\tif commit:\n'
        content += '\t\t\t\tdb.session.commit()\n'
        content += '\t\t\treturn self\n'
        content += '\t\texcept Exception as e:\n'
        content += "\t\t\tprint(f'Error SAVE: {e}')\n"
        content += '\t\t\tdb.session.rollback()\n'
        content += '\n'
        content += '\tdef save_all(self: Union[List]):\n'
        content += '\t\ttry:\n'
        content += '\t\t\tdb.session.bulk_save_objects(self)\n'
        content += '\t\t\tdb.session.flush()\n'
        content += '\t\t\tdb.session.commit()\n'
        content += '\t\texcept Exception as e:\n'
        content += "\t\t\tprint(f'Error SAVE_ALL: {e}')\n"
        content += '\t\t\tdb.session.rollback()\n'
        content += '\n'
        return content

    def create_table_for_script(self):
        return self.__create_table()

    def get_content_model_in_code(self):
        return self.__get_content_model()
