
class ConfigTemplate:

    def __init__(self):
        self.__content_init = 'from .config import get_environment\n'
        self.content = 'import os\n'

    def get_content_import_file(self):
        return self.__content_init
    
    def get_content_file(self):
        self.content += 'from dotenv import load_dotenv\n'
        self.content += '\n\n'
        self.content += 'load_dotenv()\n'
        self.content += '\n\n'
        self.content += 'class DBConfig:\n'
        self.content += '\tDB_NAME = os.getenv("DB_NAME")\n'
        self.content += '\tDB_USER = os.getenv("DB_USER")\n'
        self.content += '\tDB_PASS = os.getenv("DB_PASS")\n'
        self.content += '\tDB_HOST = os.getenv("DB_HOST")\n'
        self.content += '\tDB_PORT = os.getenv("DB_PORT")\n'
        self.content += '\n\n'
        self.content += 'class DevelopConfig(DBConfig):\n'
        self.content += '\tAPP_NAME = os.getenv("APP_NAME")\n'
        self.content += '\tHOST = os.getenv("HOST")\n'
        self.content += '\tPORT = os.getenv("PORT")\n'
        self.content += '\tDEBUG = os.getenv("DEBUG")\n'
        self.content += '\tENVIRONMENT = "development"\n'
        self.content += '\tSECRET_KEY = os.getenv("SECRET_KEY")\n'
        self.content += '\n\n'
        self.content += 'class ProductionConfig(DBConfig):\n'
        self.content += '\tAPP_NAME = os.getenv("APP_NAME")\n'
        self.content += '\tHOST = os.getenv("HOST")\n'
        self.content += '\tPORT = os.getenv("PORT")\n'
        self.content += '\tDEBUG = False\n'
        self.content += '\tENVIRONMENT = "production"\n'
        self.content += '\tSECRET_KEY = os.getenv("SECRET_KEY")\n'
        self.content += '\n\n'
        self.content += 'get_environment = {\n'
        self.content += '\t"development": DevelopConfig,\n'
        self.content += '\t"production": ProductionConfig\n'
        self.content += '}\n'
        return self.content

