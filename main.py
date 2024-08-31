import click
from colorama import init
from pyfiglet import Figlet

init(autoreset=True)

APP_NAME = 'Flask APP CLI'
APP_VERSION = '0.0.1'
APP_DEVELOPER = 'Felipe Medel'
APP_REPOSITORY = 'https://github.com/FelipeMedel/flask_app_cli'


@click.group()
@click.version_option(version=APP_VERSION, prog_name=APP_NAME)
def cli():
    pass


@cli.command('info', help='Flask App CLI Information')
def info():
    f = Figlet(font='slant', justify='center')
    print(f.renderText(APP_NAME))
    print(f'Version {APP_VERSION}\nDeveloped by {APP_DEVELOPER}')
    print(f'Repository {APP_REPOSITORY}')


# imports options
from core.options.infrastructure_option import *


if __name__ == '__main__':
    cli()
