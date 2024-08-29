import click
from main import cli
from core.packages import Infrastructure
from core.utilities.credits import Credits


@cli.command('new-project', help='Generate a new project of Python with Flask')
@click.option('--name', '-n', required=True, help='Project name')
@click.option('--root', '-r', required=False, default='app', help='root dir (Default app)')
def new_project(name, root):
    if not name:
        click.Abort("Please provide all required arguments: Project name (--name)")

    project = Infrastructure(project_name=name, root=root)
    project.create_project_dir()
    project.create_all_dir()
    Credits(title=name).get_finish_project()

