import click
from main import cli
from core.packages import Model
from core.utilities import Credits, CommandMessage

command_txt = CommandMessage()


@cli.command('get-models', help=command_txt.get_command_text('getModels'))
@click.option('--tablename', '-t', required=True, help=command_txt.get_command_text('tableName'))
@click.option('--all', '-a', required=True, help=command_txt.get_command_text('allModels'))
def get_models(tablename, all):
    if not tablename:
        click.Abort(command_txt.get_error_message('name'))
    Model(table_name=tablename).show_migration_models(_all=all)


@cli.command('new-model', help=command_txt.get_command_text('newModel'))
@click.option('--tablename', required=True, help=command_txt.get_command_text('tableName'))
@click.option('--key', required=True, help=command_txt.get_command_text('key'))
@click.option('--primary', required=False, type=bool, help=command_txt.get_command_text('primary'))
@click.option('--type', required=True, help=command_txt.get_command_text('type'))
@click.option('--nullable', required=True, type=bool, help=command_txt.get_command_text('nullable'))
@click.option('--default', required=False, help=command_txt.get_command_text('nullable'))
@click.option('--comment', required=False, help=command_txt.get_command_text('comment'))
def new_model(tablename, key, primary, type, nullable, default, comment):
    if not tablename or not key or not type or not nullable:
        click.Abort("Please provide all required arguments (--tablename, --key, --type, --nullable)")

    Model(table_name=tablename).create_migration_model(key=key,
                                                       primary=primary,
                                                       _type=type,
                                                       nullable=nullable,
                                                       default=default,
                                                       comment=comment)
    click.echo(f"New field added: {key} on table: {tablename}")
