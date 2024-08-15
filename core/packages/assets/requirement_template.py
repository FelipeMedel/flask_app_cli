
class RequirementTemplate:

    def __init__(self):
        self.__DEPENDENCIES = [
            'Flask',
            'Flask-Cors',
            'python-dotenv'
        ]

    def load_dependencies(self):
        response = ''
        for dependency in self.__DEPENDENCIES:
            response += f'{dependency}\n'
        return response
