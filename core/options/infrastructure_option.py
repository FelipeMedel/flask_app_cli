import click
from main import cli
from core.packages import Infrastructure
from core.utilities import Credits, CommandMessage


command_txt = CommandMessage()


@cli.command('new', help=command_txt.get_command_text('new'))
@click.option('--name', '-n', required=True, help=command_txt.get_command_text('name'))
@click.option('--root', '-r', required=False, default='app', help=command_txt.get_command_text('root'))
@click.option('--database', '-d', required=False, default=False, help=command_txt.get_command_text('database'))
@click.option('--multitenant', '-t', required=False, default=False, help=command_txt.get_command_text('multitenant'))
def new_project(name, root, database, multitenant):
    if not name:
        click.Abort(command_txt.get_error_message('name'))

    project = Infrastructure(project_name=name, root=root, with_db=database, multitenant=multitenant)
    project.create_project_dir()
    project.create_all_dir()
    Credits(title=name).get_finish_project()

