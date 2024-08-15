import click
from colorama import init

init(autoreset=True)


@click.group()
def cli():
    pass


# imports options
from options.model_option import *
from options.infrastructure_option import *

if __name__ == '__main__':
    cli()
