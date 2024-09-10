import os


class PathFiles:

    def __init__(self, dir_name: str = ''):
        self.__dir_name = dir_name

    def get_root_dir(self):
        source_dir = 'src'
        end_route = source_dir
        exclude_dir = ('database', 'documentation', 'settings')
        with (os.scandir(source_dir) as ficheros):
            first_record = False
            for fichero in ficheros:
                if (not first_record and '.' not in fichero.name and fichero.is_dir()
                        and fichero.name not in exclude_dir):
                    end_route += f'/{fichero.name}'
                    first_record = True
                if fichero.is_dir():
                    print(fichero.name)
        return f'{end_route}/{self.__dir_name}'
