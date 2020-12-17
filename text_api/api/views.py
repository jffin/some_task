from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from text_api.api.resources.text import TextList
from text_api.extensions import apispec
from text_api.api.resources import TextResource
from text_api.api.schemas import TextSchema

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(TextResource, '/text/<string:text_slug>/', endpoint='text_by_slug')
api.add_resource(TextList, '/texts/', endpoint='texts')


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema('TextSchema', schema=TextSchema)
    apispec.spec.path(view=TextResource, app=current_app)
    apispec.spec.path(view=TextList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
