import os


class PathFiles:

    def __init__(self, dir_name: str = '', root_path: str = 'app'):
        self.__dir_name = dir_name
        self.__root_path = root_path

    def get_root_path(self):
        source_dir = 'src'
        root_path = self.__root_path
        exclude_dir = ('database', 'documentation', 'settings')
        with (os.scandir(source_dir) as ficheros):
            for fichero in ficheros:
                if ('.' not in fichero.name and fichero.is_dir()
                        and fichero.name not in exclude_dir):
                    root_path = f'{fichero.name}'
                    break
        return root_path

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
        return f'{end_route}/{self.__dir_name}'

    def get_file_for_path(self, file_name: str):
        path = self.get_root_dir()
        exist = False
        path_result = ''
        for dir_path, dirname, filename in os.walk(path):
            if file_name in filename:
                path_result = os.path.join(dir_path, file_name)
                exist = True
                break
        return exist, path_result
