import click
from main import cli
from core.packages import Model
from core.utilities import (Credits,
                            CommandMessage)

command_txt = CommandMessage()


@cli.command('get-models', help=command_txt.get_command_text('getModels'))
@click.option('--tablename', '-t', required=True, help=command_txt.get_command_text('tableName'))
@click.option('--all', '-a', required=False, default=True, help=command_txt.get_command_text('allModels'))
def get_models(tablename, all):
    if not tablename:
        click.Abort(command_txt.get_error_message('tableName'))
    Model(table_name=tablename).show_migration_models(_all=all)


@cli.command('base-model', help=command_txt.get_command_text('baseModel'))
@click.option('--id', '-p', required=False, type=bool, default=True, help=command_txt.get_command_text('id'))
def generate_base_model(id):
    Model(**{'id': id}).generate_base_model()


@cli.command('new-model', help=command_txt.get_command_text('newModel'))
@click.option('--tablename', '-tb', required=True, help=command_txt.get_command_text('tableName'))
@click.option('--key', '-k', required=True, help=command_txt.get_command_text('key'))
@click.option('--primary', '-p', required=False, type=bool, help=command_txt.get_command_text('primary'))
@click.option('--type', '-t', required=True, help=command_txt.get_command_text('type'))
@click.option('--nullable', '-n', required=True, type=bool, help=command_txt.get_command_text('nullable'))
@click.option('--default', '-d', required=False, help=command_txt.get_command_text('nullable'))
@click.option('--comment', '-c', required=False, help=command_txt.get_command_text('comment'))
@click.option('--update', '-u', required=False, type=bool, default=False, help=command_txt.get_command_text('update'))
def new_model(tablename, key, primary, type, nullable, default, comment, update):
    if not tablename or not key or not type or not nullable:
        click.Abort(command_txt.get_error_message('required') + " (--tablename, --key, --type, --nullable)")

    is_new = Model(table_name=tablename, **{'update': update}).create_migration_model(key=key,
                                                                                      primary=primary,
                                                                                      _type=type,
                                                                                      nullable=nullable,
                                                                                      default=default,
                                                                                      comment=comment)
    command_response = 'addField' if is_new else 'existField'
    if update:
        command_response = 'updateField'
    click.echo(command_txt.get_model_message(command=command_response, **{'field': key, 'table': tablename}))


@cli.command('load-model', help=command_txt.get_command_text('loadModel'))
@click.option('--generate', '-g', required=False, type=bool, default=False,
              help=command_txt.get_command_text('generate'))
def load_models():
    Model().load_model()
    click.echo(command_txt.get_success_message('migration'))
