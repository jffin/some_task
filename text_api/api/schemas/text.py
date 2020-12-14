from text_api.models import Text
from text_api.extensions import ma, db


class TextSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Text
        sqla_session = db.session
        load_instance = True
        fields = (
            'id',
            'text',
            'slug',
            'created',
            'updated',
        )
