from text_api.models import Text
from text_api.extensions import ma, db


class TextSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    slug = ma.Str(dump_only=True)
    created = ma.DateTime(dump_only=True)
    updated = ma.DateTime(dump_only=True)

    class Meta:
        model = Text
        sqla_session = db.session
        load_instance = True
        datetimeformat = '%Y-%m-%d %H:%m:%S'
        fields = (
            'text',
            'slug',
            'created',
            'updated',
        )
