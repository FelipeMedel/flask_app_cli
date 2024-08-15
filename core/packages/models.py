

class Model:

    def __init__(self, name: str, path: str = 'src/models'):
        self.name = name
        self.path = path

    def create_model(self):
        """
        Crea un modelo basado en una plantilla de formato .JSON, con el nombre y 5 campos
        """
        pass

    def load_model(self):
        """
        Carga y crea un modelo tomando como referencia un archivo JSON
        """
        pass
