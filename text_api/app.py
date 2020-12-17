from flask import Flask

from text_api import api
from text_api.extensions import db, jwt, migrate, apispec, celery


def create_app(testing=False, cli=False):
    """Application factory, used to create application"""
    app = Flask('text_api')
    app.config.from_object('text_api.config')

    if testing is True:
        app.config['TESTING'] = True

    configure_extensions(app, cli)
    configure_apispec(app)
    register_blueprints(app)
    init_celery(app)

    return app


def configure_extensions(app, cli):
    """configure flask extensions"""
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{'jwt': []}])
    apispec.spec.components.security_scheme(
        'jwt', {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}
    )
    apispec.spec.components.schema(
        'PaginatedResult',
        {
            'properties': {
                'total': {'type': 'integer'},
                'pages': {'type': 'integer'},
                'next': {'type': 'string'},
                'prev': {'type': 'string'},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(api.views.blueprint)


def init_celery(app=None):
    app = app or create_app()
    celery.conf.update(app.config.get('CELERY', {}))
    app.config['SQLALCHEMY_URL'] = app.config.get('CELERY_DATABASE_URI', '')

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
