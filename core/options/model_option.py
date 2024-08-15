import click
from main import cli
from core.utilities.manage_json import read_json, write_json


@cli.command('get-models')
def get_models():
    data = read_json()
    for model in data:
        text = f"""============================\nTable: {model}\n============================"""
        print(text)
        for field in data[model]:
            print(field)


@cli.command('get-model')
@click.option('--tablename', required=True, help='table name')
def get_model_by_name(tablename):
    data = read_json()
    if tablename in data:
        text = f"""============================\nTable: {tablename}\n============================"""
        print(text)
        for field in data[tablename]:
            print(field)
    else:
        print(f'Table {tablename} not found')


@cli.command('new-model')
@click.option('--tablename', required=True, help='table name')
@click.option('--key', required=True, help='Column name')
@click.option('--primary', required=False, help='optional, if the field is a primary key')
@click.option('--type', required=True, help='column type, varchar(20) or int...')
@click.option('--nullable', required=True, help='indicates if the column allows null values. (True or False)')
@click.option('--default', required=False, help='indicates the default value of the field')
@click.option('--comment', required=False, help='Allows you to add a comment to the field')
def new_model(tablename, key, primary, type, nullable, default, comment):
    if not tablename or not key or not type or not nullable:
        click.Abort("Please provide all required arguments (table_name, key, type, nullable)")
    else:
        data = read_json()

        new_table = {
            "key": key,
            "primary": primary,
            "type": type,
            "nullable": nullable,
            "default": default,
            "comment": comment
        }
        is_exist = False
        for model in data:
            if tablename in model:
                is_exist = True
                break
        if is_exist:
            data[tablename].append(new_table)
        else:
            result = {
                tablename: [new_table]
            }
            data.update(result)
        write_json(data)
        click.echo(f"New field added: {key} on table: {tablename}")
