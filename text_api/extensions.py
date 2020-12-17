"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from celery import Celery

from text_api.commons.apispec import APISpecExt


db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
apispec = APISpecExt()
celery = Celery()
