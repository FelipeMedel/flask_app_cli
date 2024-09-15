

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
        return 'Integer'

    @staticmethod
    def __get_import_types(columns: dict, _type: str = 'standard'):
        response = {}
        for column in columns:
            column_type = column['type'].lower()
            if 'varchar' in column_type:
                response['standard'].append('String')
            elif 'int' in column_type:
                response['standard'].append('Integer')
            elif 'datetime' in column_type or 'date' in column_type:
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
        if len(response) > 0:
            if _type == 'standard':
                result = f', {", ".join(response[_type])}'
            elif _type == 'special':
                result = f'from sqlalchemy.dialects.mysql import {", ".join(response[_type])}'
        return result

    def __get_content_model(self, table_name: str, columns: dict):
        # TODO: pendiente por validar si se creó el base model o si el modelo es creado con db.model
        content = f'from sqlalchemy import Column, {self.__get_import_types(columns=columns)}\n'
        content += f'{self.__get_import_types(columns=columns, _type="special")}\n'
        content += 'from . import BaseModel\n'
        content += '\n\n'
        model_name = table_name.replace('_', '').title()
        content += f'class {model_name}Model(BaseModel):\n'
        content += '\n'
        content += f'\t__tablename__ = "{table_name}"\n'
        content += '\n'
        for column in columns:
            content += (f"\t{column['key']} = Column({self.__get_column_type(_type=column['type'])}, "
                        f"nullable={column['nullable']}, default='{column['default']}', "
                        f"comment='{column['comment']}')\n")
        content += '\n'
        return content

    def __option_field_for_column(self):
        # TODO: pendiente retornar la información para crear los archivos
        tables = self.__params.get('tables', {})
        response = {}
        model_content = ''
        for table in tables.keys():
            for column in tables[table]:
                model_content = self.__get_content_model(table_name=table, columns=column)
            response[table] = model_content
        return response

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
