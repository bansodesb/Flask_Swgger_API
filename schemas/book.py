from ma import ma
from marshmallow import Schema, fields
from models.book import BookModel
from models.author import AuthorModel
from schemas.author import Book_AuthorSchema

'''
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True
        load_only = ("author",)
        include_fk = True
'''


