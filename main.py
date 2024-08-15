import click
from colorama import init

init(autoreset=True)


@click.group()
def cli():
    pass


# imports options
# TODO: Pendiente por agregar la creación de modelos
# from core.options.model_option import *
from core.options.infrastructure_option import *

if __name__ == '__main__':
    cli()
