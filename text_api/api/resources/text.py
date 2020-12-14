from flask import request
from sqlalchemy import exc
from flask_restful import Resource

from text_api.models import Text
from text_api.extensions import db
from text_api.api.schemas import TextSchema
from text_api.commons.pagination import paginate


class TextResource(Resource):
    """Single object resource

        ---
        get:
          tags:
            - api
          parameters:
            - in: path
              name: text_id
              schema:
                type: integer
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      text: TextSchema
            404:
              description: text does not exists
        put:
          tags:
            - api
          parameters:
            - in: path
              name: text_id
              schema:
                type: integer
          requestBody:
            content:
              application/json:
                schema:
                  TextSchema
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      msg:
                        type: string
                        example: text updated
                      text: TextSchema
            404:
              description: text does not exists
        delete:
          tags:
            - api
          parameters:
            - in: path
              name: text_id
              schema:
                type: integer
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      msg:
                        type: string
                        example: text deleted
            404:
              description: text does not exists
        """

    @staticmethod
    def get(text_slug):
        schema = TextSchema()
        text = Text.get_by_slug_or_404(text_slug)
        return {"text": schema.dump(text)}


class TextList(Resource):
    """
    Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/TextSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              TextSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: text created
                  text: TextSchema
    """

    @staticmethod
    def get():
        schema = TextSchema(many=True)
        query = Text.query

        return paginate(query, schema)

    @staticmethod
    def post():
        schema = TextSchema()
        text = schema.load(request.json)

        db.session.add(text)

        try:
            db.session.commit()
        except exc.IntegrityError:
            return {'msg': 'duplicate entries'}, 403

        return {'msg': 'text created', 'text': schema.dump(text)}, 201

