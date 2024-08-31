
class CommandMessage:

    def __init__(self):
        self.__COMMANDS = {
            'new': 'Generate a new project of Python with Flask',
            'name': 'Project name',
            'root': 'root dir (Default app)',
            'database': 'Database Management with SQLAlchemy (Default False)',
            'multitenant': 'Connection to multiple databases (Default False)'
        }
        self.__ERRORS = {
            'name': 'Please provide all required arguments: Project name (--name)'
        }

    def get_command_text(self, command: str):
        return self.__COMMANDS.get(command, 'Command not found')

    def get_error_message(self, command: str):
        return self.__ERRORS.get(command, 'Command not found')