from ma import ma
from marshmallow import Schema, fields
from models.author import AuthorModel
from models.book import BookModel


'''
class AuthorSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(BookSchema, many=True)

    class Meta:
        model = AuthorModel
        load_instance = True
        include_fk = True
'''


class AuthorSchema(Schema):
    class Meta:
        fields = ('id', 'name')
        ordered = True


class Book_AuthorSchema(Schema):
    author = fields.Nested(AuthorSchema)

    class Meta:
        fields = ('id', 'author', 'active')
        ordered = True


class BookSchema(Schema):
    author = fields.Nested(Book_AuthorSchema, many=True)

    class Meta:
        fields = ('id', 'name', 'author')
        ordered = True
