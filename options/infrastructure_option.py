import click
from main import cli
from packages import Infrastructure
from utilities.credits import Credits


@cli.command('new-project')
@click.option('--name', required=True, help='Project name')
@click.option('--root', required=False, default='app', help='root dir (Default app)')
@click.option('--template', required=False, type=bool, default=True, help='use a functional template (Default True)')
def new_project(name, root, template):
    if not name:
        click.Abort("Please provide all required arguments: Project name (--name)")

    project = Infrastructure(project_name=name, root=root)
    project.create_project_dir()
    project.create_all_dir()
    Credits(title=name).get_finish_project()


@cli.command('add-config')
def config_app():
    pass


