class EnvTemplate:

    def __init__(self):
        self.__APP_NAME = 'APPLICATION NAME'
        self.__HOST = '127.0.0.1'
        self.__PORT = 5000
        self.__DEBUG = True
        self.__SECRET_KEY = 'SECRET KEY'
        self.__DB_NAME = 'DATABASE NAME'
        self.__DB_USER = 'USERNAME'
        self.__DB_PASS = 'PASSWORD'
        self.__DB_HOST = 'localhost'
        self.__DB_PORT = 3306

    def get_data(self):
        text = '# ========================\n'
        text += '# application variables\n'
        text += '# ========================\n'
        text += f'APP_NAME="{self.__APP_NAME}"\n'
        text += f'APP_HOST={self.__HOST}\n'
        text += f'APP_PORT={self.__PORT}\n'
        text += f'APP_DEBUG={int(self.__DEBUG)}\n'
        text += f'APP_SECRET_KEY="{self.__SECRET_KEY}"\n'
        text += '\n'
        text += '# ========================\n'
        text += '# database variables\n'
        text += '# ========================\n'
        text += f'DB_NAME="{self.__DB_NAME}"\n'
        text += f'DB_USER="{self.__DB_USER}"\n'
        text += f'DB_PASS="{self.__DB_PASS}"\n'
        text += f'DB_HOST={self.__DB_HOST}\n'
        text += f'DB_PORT={self.__DB_PORT}\n'
        return text

    def get_values(self):
        return dict(
            appName=self.__APP_NAME,
            host=self.__HOST,
            port=self.__PORT,
            debug=self.__DEBUG,
            secretKey=self.__SECRET_KEY,
            dbName=self.__DB_NAME,
            dbUser=self.__DB_USER,
            dbPass=self.__DB_PASS,
            dbHost=self.__DB_HOST,
            dbPort=self.__DB_PORT
        )
