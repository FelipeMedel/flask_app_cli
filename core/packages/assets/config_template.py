class ConfigTemplate:

    def __init__(self, with_db: bool = False, multitenant: bool = False):
        self.__content_init = 'from .config import get_environment\n'
        self.content = 'import os\n'
        self.multitenant = multitenant
        self.with_db = with_db

    def get_content_import_file(self):
        if self.with_db and self.multitenant:
            self.__content_init += 'from .db_tenants import DBTenant\n'
        return self.__content_init

    def get_content_file(self):
        self.content += 'from dotenv import load_dotenv\n'
        self.content += '\n\n'
        self.content += 'load_dotenv()\n'
        if self.with_db:
            self.content += '\n\n'
            self.content += 'class DBConfig:\n'
            self.content += '\tDB_NAME = os.getenv("DB_NAME")\n'
            self.content += '\tDB_USER = os.getenv("DB_USER")\n'
            self.content += '\tDB_PASS = os.getenv("DB_PASS")\n'
            self.content += '\tDB_HOST = os.getenv("DB_HOST")\n'
            self.content += '\tDB_PORT = os.getenv("DB_PORT")\n'
        if self.with_db and not self.multitenant:
            self.content += '\tmysql_uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(\n'
            self.content += '\t\tuser=DB_USER,\n'
            self.content += '\t\tpassword=DB_PASS,\n'
            self.content += '\t\thost=DB_HOST,\n'
            self.content += '\t\tport=DB_PORT,\n'
            self.content += '\t\tdb=DB_NAME)\n'
            self.content += '\tSQLALCHEMY_DATABASE_URI = mysql_uri\n'
        elif self.with_db and self.multitenant:
            self.content += '\tSQLALCHEMY_TRACK_MODIFICATIONS = False\n'
            self.content += '\tSQLALCHEMY_BINDS = dict()\n'
            self.content += '\tSQLALCHEMY_COMMIT_ON_TEARDOWN = True\n'
            self.content += "\tSQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'\n"
        self.content += '\n\n'
        if self.with_db:
            self.content += 'class DevelopConfig(DBConfig):\n'
        else:
            self.content += 'class DevelopConfig:\n'
        self.content += '\tAPP_NAME = os.getenv("APP_NAME")\n'
        self.content += '\tHOST = os.getenv("HOST")\n'
        self.content += '\tPORT = os.getenv("PORT")\n'
        self.content += '\tDEBUG = os.getenv("DEBUG")\n'
        self.content += '\tENVIRONMENT = "development"\n'
        self.content += '\tSECRET_KEY = os.getenv("SECRET_KEY")\n'
        self.content += '\n\n'
        if self.with_db:
            self.content += 'class ProductionConfig(DBConfig):\n'
        else:
            self.content += 'class ProductionConfig:\n'
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

