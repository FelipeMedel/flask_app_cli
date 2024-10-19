class ApplicationTemplate:

    def __init__(self, with_sql: bool = False, develop: bool = True, multitenant: bool = False, root: str = 'app'):
        self.__with_sql = with_sql
        self.__develop = develop
        self.__multitenant = multitenant
        self.__root = root

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
            content += 'db = SQLAlchemy()\n\n\n'
        content += 'def create_application(config_name: str):\n'
        content += '\tfrom settings import get_environment\n'
        content += '\tapp = Flask(__name__, instance_relative_config=True)\n'
        content += "\tCORS(app, resources={r'/app/*': {'origins': '*'}}, allow_headers='authorization')\n"
        content += "\tapp.config.from_object(get_environment[config_name])\n"
        if self.__with_sql:
            content += "\tdb.init_app(app)\n"
        content += "\twith app.app_context():\n"
        content += f"\t\tfrom {self.__root}.blueprints.api_bp import api_bp\n"
        content += f"\t\turl_prefix_app = '/api/v1'\n"
        content += f"\t\tapp.register_blueprint(api_bp, url_prefix=url_prefix_app)\n"
        content += "\treturn app\n"
        content += "\n\n"
        content += "application = create_application(config_name='development')\n"
        content += '\n\n'
        content += f"from {self.__root}.middlewares import *\n"
        content += '\n\n'
        content += "@application.route('/test', methods=['GET'])\n"
        content += "def root_route():\n"
        content += "\tresponse = {'ok': True, 'message': 'Hola Mundo!'}\n"
        content += "\treturn make_response(jsonify(response), 200)\n"
        content += '\n\n'
        if self.__with_sql:
            content += '@application.teardown_request\n'
            content += 'def remove_session(param):\n'
            content += '\tdb.session.remove()\n'
        return content

    def get_content_blueprint_file(self):
        imports = ''
        if self.__with_sql and self.__multitenant:
            imports = ', jsonify, make_response, request'
        content = f'from flask import Blueprint{imports}\n'
        if self.__with_sql and self.__multitenant:
            content += f'from werkzeug.exceptions import BadRequest\n'
            content += f'from {self.__root} import application, db\n'
        content += '\n\n'
        content += "api_bp = Blueprint('api_bp', __name__)\n"
        content += '\n\n'
        content += '@api_bp.before_request\n'
        content += 'def before_request():\n'
        if self.__with_sql and self.__multitenant:
            content += '\tif request.method != "OPTIONS":\n'
            content += '\t\ttenant = request.headers.get("Database")\n'
            content += '\t\tif not tenant:\n'
            content += '\t\t\traise BadRequest("No ha enviado el parámetro tenant en los headers")\n'
            content += '\t\ttry:\n'
            content += '\t\t\tfrom database import DBTenant\n'
            content += '\t\t\tdb.session = DBTenant(app=application).get_tenant_session(tenant_name=request.headers.get("Database"))\n'
            content += '\t\texcept Exception as e:\n'
            content += "\t\t\tresponse = dict(message='Error al intentar consultar la base de datos seleccionada.')\n"
            content += "\t\t\treturn make_response(jsonify(response), 500)\n"
        else:
            content += '\tpass\n'
        content += '\n\n'
        content += '@api_bp.after_request\n'
        content += 'def after_request(response):\n'
        content += "\tresponse.headers.add('enable-underscores-in-headers', 'true')\n"
        content += "\tresponse.headers.add('Access-Control-Allow-Origin', '*')\n"
        content += "\tresponse.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')\n"
        content += "\tresponse.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')\n"
        content += "\treturn response\n"
        content += '\n\n'
        content += f'from {self.__root}.controllers.api import *\n'
        content += "\n"
        return content

    def get_content_controller_test(self):
        content = f'from flask import jsonify, make_response, request\n'
        content += f'from {self.__root}.blueprints.api_bp import api_bp\n'
        content += '\n\n'
        content += "@api_bp.route('/test', methods=['GET'])\n"
        content += "def root_route_test():\n"
        content += "\tresponse = {'ok': True, 'message': 'Testing blueprint - Flask App Cli!'}\n"
        content += "\treturn make_response(jsonify(response), 200)\n"
        content += "\n"
        return content

    def get_content_tenant(self):
        content = 'from flask import request, make_response, jsonify, g\n'
        content += f'from werkzeug.exceptions import BadRequest\n'
        content += f'from {self.__root} import application, db\n'
        content += '\n\n'
        content += '@application.before_request\n'
        content += 'def tenant_middleware():\n'
        content += '\tif request.method != "OPTIONS":\n'
        content += '\t\ttenant = request.headers.get("Database")\n'
        content += '\t\tif not tenant:\n'
        content += '\t\t\traise BadRequest("No ha enviado el parámetro tenant en los headers")\n'
        content += '\t\ttry:\n'
        content += '\t\t\tfrom database import DBTenant\n'
        content += '\t\t\tdb.session = DBTenant(app=application).get_tenant_session(tenant_name=request.headers.get("Database"))\n'
        content += '\t\texcept Exception as e:\n'
        content += "\t\t\tresponse = dict(message='Error al intentar consultar la base de datos seleccionada.')\n"
        content += "\t\t\treturn make_response(jsonify(response), 500)\n"
        return content

    def get_content_middleware_error(self):
        content = 'from flask import make_response, jsonify\n'
        content += f'from {self.__root} import application\n'
        content += '\n\n'
        content += '@application.errorhandler(400)\n'
        content += 'def request_bad_request(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'No fue posible procesar tu petición, por favor revisa que no tengas errores en la misma.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 400)\n'
        content += '\n\n'
        content += '@application.errorhandler(401)\n'
        content += 'def request_unauthorized(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'No tiene autorización para la petición.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 401)\n'
        content += '\n\n'
        content += '@application.errorhandler(403)\n'
        content += 'def request_forbidden(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'Solicitud prohibida por normas administrativas.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 403)\n'
        content += '\n\n'
        content += '@application.errorhandler(404)\n'
        content += 'def request_resource_not_found(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'No fue posible encontrar información sobre el recurso consultado.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 404)\n'
        content += '\n\n'
        content += '@application.errorhandler(405)\n'
        content += 'def request_method_not_found(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'La petición realizada tiene un método que no existe.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 405)\n'
        content += '\n\n'
        content += '@application.errorhandler(413)\n'
        content += 'def request_entity_too_large(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'La petición realizada, posee un peso superior al permitido por el servidor en cada uno de sus request.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 413)\n'
        content += '\n\n'
        content += '@application.errorhandler(500)\n'
        content += 'def request_internal_server_error(error):\n'
        content += '\tresponse = {\n'
        content += "\t\t'message': 'Se ha presentado un error en el servidor.',\n"
        content += "\t\t'error': str(error)\n"
        content += '\t}\n'
        content += '\treturn make_response(jsonify(response), 500)\n'
        content += '\n\n'
        return content

