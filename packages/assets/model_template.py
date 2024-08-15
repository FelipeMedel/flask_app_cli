

class ModelTemplate:

    def __init__(self, table_name: str = 'TableName', **params):
        self.__table_name = table_name
        self.__params: dict = params

    def __create_table(self):
        script = f"""create table if not exist {self.__table_name}"""
        script += '(\n'
        for column in self.__params:
            if column['primary']:
                script += f"{column['key']} INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',\n"
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
                script += f'{column["key"]} {column["type"]} {nullable} {default} {comment},\n'
        script += ');\n'
        return script

    def create_table_for_script(self):
        return self.__create_table()
