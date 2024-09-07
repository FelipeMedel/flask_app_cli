
class DocumentationTemplate:

    def __init__(self, project_name: str, root: str) -> None:
        self.__project_name = project_name
        self.__root = root

    def get_content_apidoc_json(self):
        content = '{\n'
        content += '\t"name": "",\n'
        content += '\t"version": "1.0.0",\n'
        content += '\t"description": "",\n'
        content += f'\t"title": "{self.__project_name}",\n'
        content += '\t"url": "http://127.0.0.1/",\n'
        content += '\t"header": {\n'
        content += '\t\t"title": "Inicio",\n'
        content += '\t\t"filename": "header.md"\n'
        content += '\t},\n'
        content += '\t"template": {\n'
        content += '\t\t"showRequiredLabels": true,\n'
        content += '\t\t"withCompare": false,\n'
        content += '\t\t"withGenerator": false,\n'
        content += '\t\t"aloneDisplay": false\n'
        content += '\t}\n'
        content += '}\n'
        return content

    def get_content_header_md(self):
        content = f'# Documentación API {self.__project_name}\n'
        content += '\n'
        content += f'Esta es la descripción de la documentación del API {self.__project_name}\n'
        return content

    def get_content_endpoint_test(self):
        content = f'# Documentación API {self.__project_name}\n'
        content += '\n\n'
        content += 'def root_route_test():\n'
        content += '\t"""\n'
        content += '\t@api {get}' + f'/{self.__root}/api/v1/test Correr ruta controlador test\n'
        content += '\t@apiName GetTesting\n'
        content += '\t@apiGroup Testing\n'
        content += '\t@apiDescription Esta es una descipción de prueba para el servicio testing.\n'
        content += '\t@apiSampleRequest off\n'
        content += '\t@apiSuccessExample {json} Success-Response:\n'
        content += '\t\tHTTP/1.1 200 OK\n'
        content += '\t\t{\n'
        content += '\t\t"ok": true,\n'
        content += '\t\t"message": "Testing blueprint - Flask App Cli!"\n'
        content += '\t\t}\n'
        content += '\t"""\n'
        content += '\tpass\n'
        return content


