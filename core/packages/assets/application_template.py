

class ApplicationTemplate:

    def __init__(self, with_sql: bool = False, develop: bool = True):
        self.__with_sql = with_sql
        self.__develop = develop

    def get_content_run(self):
        content = 'import os\n'
        content += 'from dotenv import load_dotenv\n'
        content += 'from app import application\n'
        content += '\n\n'
        content += 'load_dotenv()\n'
        content += '\n\n'
        content += "if __name__ == '__main__':\n"
        if self.__develop:
            debug = 'bool(os.getenv("APP_DEBUG", 1))'
        else:
            debug = 'False'
        content += ('\tapplication.run(host=os.getenv("APP_HOST"), '
                    'port=os.getenv("APP_PORT"), '
                    f'debug={debug})\n')
        return content

    def get_content_application(self):
        content = 'from flask import Flask, make_response, jsonify\n'
        content += 'from flask_cors import CORS\n'
        if self.__with_sql:
            content += 'from flask_sqlalchemy import SQLAlchemy\n'
        content += '\n\n'
        if self.__with_sql:
            content += 'db = SQLAlchemy()\n'
        content += 'def create_application(config_name: str):\n'
        content += '\tfrom settings import get_environment\n'
        content += '\tapp = Flask(__name__, instance_relative_config=True)\n'
        content += "\tCORS(app, resources={r'/app/*': {'origins': '*'}}, allow_headers='authorization')\n"
        content += "\tapp.config.from_object(get_environment[config_name])\n"
        if self.__with_sql:
            content += "\tdb.init_app()\n"
        content += "\treturn app\n"
        content += "\n\n"
        content += "application = create_application(config_name='development')\n"
        content += "\n\n"
        content += "@application.route('/', methods=['GET'])\n"
        content += "def root_route():\n"
        content += "\tresponse = {'ok': True, 'message': 'Hola Mundo!'}\n"
        content += "\treturn make_response(jsonify(response), 200)\n"
        content += "\n"
        return content
