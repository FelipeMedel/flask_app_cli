class CommandMessage:

    def __init__(self):
        self.__COMMANDS = {
            'new': 'Generate a new project of Python with Flask',
            'name': 'Project name',
            'root': 'Root dir (Default app)',
            'database': 'Database Management with SQLAlchemy (Default False)',
            'multitenant': 'Connection to multiple databases (Default False)',
            'getModels': 'Show all models',
            'tableName': 'Table or model name',
            'allModels': 'Show all models (Default True)',
            'newModel': 'Add new model',
            'key': 'Column name',
            'primary': 'If the field is a primary key (Default False)',
            'type': 'Column type, varchar(20) or int...',
            'nullable': 'Indicates if the column allows null values. (True or False)',
            'default': 'indicates the default value of the field',
            'comment': 'Allows you to add a comment to the field',
            'loadModel': 'Generate in code the models created in the json file as well as the migration files',
            'generate': 'Generate the models created in the migration files (Default False)',
        }
        self.__ERRORS = {
            'name': 'Please provide all required arguments: Project name (--name)',
            'tableName': 'Please provide all required arguments: Table name (--tablename)',
            'required': 'Please provide all required arguments',
        }
        self.__SUCCESS = {
            'migration': 'The migration files have been created and all models have been generated.'
        }
        self.__MODELS = {
            'addField': "New field added: {field} on table: {table}"
        }

    def get_command_text(self, command: str):
        return self.__COMMANDS.get(command, 'Command not found')

    def get_error_message(self, command: str):
        return self.__ERRORS.get(command, 'Command not found')

    def get_success_message(self, command: str):
        return self.__SUCCESS.get(command, 'Command not found')

    def get_model_message(self, command: str, **params):
        field = params.get('field')
        table = params.get('table')
        response = self.__SUCCESS.get(command, 'Command not found')
        if field and table:
            response = response.replace('{field}', field)
            response = response.replace('{table}', table)
        return response
