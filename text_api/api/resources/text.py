import nltk

from flask import request
from sqlalchemy import exc
from flask_restful import Resource

from text_api.commons.sentences_finder import SentenceEmbedding
from text_api.models import Text
from text_api.extensions import db
from text_api.api.schemas import TextSchema
from text_api.commons.pagination import paginate


RESULT = [
    {
        "sentence": "new test",
        "distance": 0.16993166870256526,
        "slug": "new-test"
    },
    {
        "sentence": "Continue your learning with related content selected by the Team or move between pages by using the navigation links below.",
        "distance": 0.16205188943416116,
        "slug": "continue-your-learni"
    },
    {
        "sentence": "sdfndsjfndsjfsd",
        "distance": 0.15816308106857968,
        "slug": "sdfndsjfndsjfsd"
    },
    {
        "sentence": "gsdfsdgsdgsd",
        "distance": 0.10788399986970942,
        "slug": "gsdfsdgsdgsd"
    },
    {
        "sentence": "testtexttesttexttesttexttesttexttesttexttesttexttesttexttesttexttesttexttesttexttesttext",
        "distance": 0.1063344959452629,
        "slug": "testtexttesttexttest"
    },
    {
        "sentence": "jyujtyfhdgdrgdfgdf",
        "distance": 0.09909857467801386,
        "slug": "jyujtyfhdgdrgdfgdf"
    },
    {
        "sentence": "gsfsfsdfsdfsdgsdfsd",
        "distance": 0.09721390134673458,
        "slug": "gsfsfsdfsdfsdgsdfsd"
    },
    {
        "sentence": "gsdfdsfnsfnsd",
        "distance": 0.09447300785168167,
        "slug": "gsdfdsfnsfnsd"
    },
    {
        "sentence": "gsfsfsdfsdfsdgsdfsdf",
        "distance": 0.09055933770398161,
        "slug": "gsfsfsdfsdfsdgsdfsdf"
    },
    {
        "sentence": "gsfsdgsdfdsfsdf",
        "distance": 0.09052721991185886,
        "slug": "gsfsdgsdfdsfsdf"
    },
    {
        "sentence": "gsdfsdfdsgdsfsdf",
        "distance": 0.08231491021381165,
        "slug": "gsdfsdfdsgdsfsdf"
    },
    {
        "sentence": "test",
        "distance": 0.07399995248936064,
        "slug": "test"
    },
    {
        "sentence": "gddsfdsgf",
        "distance": 0.06966567491036335,
        "slug": "gddsfdsgf"
    }
]


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
        text = Text.get_by_slug_or_404(text_slug)
        sentences = nltk.tokenize.sent_tokenize(text.content)
        return {"text": sentences}

    @staticmethod
    def post(text_slug):
        data = request.json
        # results = SentenceEmbedding.run(data['sentence'], text_slug)
        return RESULT


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

