from datetime import datetime

from flask_restful import abort
from inflection import parameterize

from text_api.extensions import db


class Text(db.Model):

    model = 'texts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, unique=True)

    slug = db.Column(db.String(20), unique=True, nullable=False)

    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = self.create_slug_from_text(kwargs.get('content', '')[:20])
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Text {self.content[:20]}>'

    @staticmethod
    def create_slug_from_text(text):
        # TODO insure slug is unique
        new_slug = parameterize(text)
        return new_slug

    @staticmethod
    def get_by_slug_or_404(text_slug):
        # finds text by slug or throw 404
        text = Text.query.filter_by(slug=text_slug).first()
        if text is None:
            abort(404, description='text not found')
        return text
