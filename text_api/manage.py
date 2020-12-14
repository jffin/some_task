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
    """Create a new admin user"""
    from text_api.extensions import db
    from text_api.models import User

    click.echo('create user')
    user = User(username='zxzzoaydnnzs', email='admin@mail.com', password='ed315517-bd1e-4b55-bc4a-0e1d7e72c558', active=True)
    db.session.add(user)
    db.session.commit()
    click.echo('created user admin')


if __name__ == '__main__':
    cli()
