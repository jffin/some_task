import click
from flask.cli import FlaskGroup

from text_api.app import create_app


def create_text_api(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_text_api)
def cli():
    """Main entry point"""


@cli.command('init')
def init():
    """Initial values"""
    pass


if __name__ == '__main__':
    cli()
