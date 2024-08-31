

class DatabaseTemplate:

    def __init__(self):
        self.write = ''
        self.imports = ''

    def get_import_init(self):
        self.imports += 'from .db_tenants import DBTenant\n'
        return self.imports

    def get_database_config(self):
        self.write += '#!/usr/bin/env python\n'
        self.write += '# -*- coding: utf-8 -*-\n'
        self.write += '\n'
        self.write += 'from sqlalchemy import create_engine\n'
        self.write += 'from sqlalchemy.orm import sessionmaker, scoped_session\n'
        self.write += 'from sqlalchemy.pool import NullPool\n'
        self.write += 'from settings.config import DBConfig\n'
        self.write += '\n\n'
        self.write += 'class DBTenant:\n'
        self.write += '\n'
        self.write += '\tdef __init__(self, app):\n'
        self.write += '\t\tself.application = app\n'
        self.write += '\n'
        self.write += '\tdef __prepare_bind(self, tenant_name: str):\n'
        self.write += '\t\tif tenant_name not in self.application.config["SQLALCHEMY_BINDS"]:\n'
        self.write += '\t\t\tmysql_uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{tenant}?charset=utf8".format(\n'
        self.write += '\t\t\t\tuser=DBConfig.DB_USER,\n'
        self.write += '\t\t\t\tpassword=DBConfig.DB_PASS,\n'
        self.write += '\t\t\t\thost=DBConfig.DB_HOST,\n'
        self.write += '\t\t\t\tport=DBConfig.DB_PORT,\n'
        self.write += '\t\t\t\ttenant=tenant_name)\n'
        self.write += '\t\t\tself.application.config["SQLALCHEMY_BINDS"][tenant_name] = mysql_uri\n'
        self.write += '\t\treturn self.application.config["SQLALCHEMY_BINDS"][tenant_name]\n'
        self.write += '\n'
        self.write += '\tdef get_tenant_session(self, tenant_name: str):\n'
        self.write += '\t\turl = self.__prepare_bind(tenant_name=tenant_name)\n'
        self.write += '\t\tengine = create_engine(url=url, poolclass=NullPool)\n'
        self.write += '\t\tsession = scoped_session(sessionmaker(autocommit=False, bind=engine))\n'
        self.write += '\t\treturn session\n'
        return self.write
