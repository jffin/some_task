import nltk

from flask import request
from sqlalchemy import exc
from flask_restful import Resource

from text_api.models import Text
from text_api.extensions import db
from text_api.api.schemas import TextSchema
from text_api.commons.pagination import paginate
from text_api.tasks.sentences import find_sentences_task


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
        # try to find text in database or throw 404
        # then divide text into sentences
        text = Text.get_by_slug_or_404(text_slug)
        sentences = nltk.tokenize.sent_tokenize(text.content)
        return {'text': sentences}

    @staticmethod
    def post(text_slug):
        # we receive sentence and slug to eliminate current text from search
        # then call celery task to find similar sentences
        # TODO create websocket to communicate with browser with updates
        data = request.json
        result = find_sentences_task.delay(data['sentence'], text_slug)
        return result.wait(timeout=None, interval=0.5)


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
        """get all texts"""
        schema = TextSchema(many=True)
        query = Text.query

        return paginate(query, schema)

    def post(self):
        """add new text to database"""
        schema = TextSchema()
        text = schema.load(request.json)

        if not self.is_english(text.content):
            return {'msg', 'Please provide text in english language'}, 403

        db.session.add(text)

        try:
            db.session.commit()
        except exc.IntegrityError:
            return {'msg': 'duplicate entries'}, 403

        return {'msg': 'text created', 'text': schema.dump(text)}, 201

    @staticmethod
    def is_english(s):
        """checks if text is english"""
        return s.isascii()


class TaskResult(Resource):
    """
    Creation and get_all

    ---
    post:
      tags:
        - api
      requestBody:
        content:
          application/json
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: Array
        """

    @staticmethod
    def post():
        """for communication results with frontend"""
        pass
