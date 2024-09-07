
class RequirementTemplate:

    def __init__(self, with_db: bool = False):
        self.__DEPENDENCIES = [
            'Flask',
            'Flask-Cors',
            'python-dotenv'
        ]
        if with_db:
            self.__DEPENDENCIES.append('sqlalchemy')
            self.__DEPENDENCIES.append('PyMySQL')
            self.__DEPENDENCIES.append('Flask-SQLAlchemy')

    def load_dependencies(self):
        response = ''
        for dependency in self.__DEPENDENCIES:
            response += f'{dependency}\n'
        return response
