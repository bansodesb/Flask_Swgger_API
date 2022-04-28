from db import db
from typing import List

'''
class AuthorModel(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    books = db.relationship("BookModel", lazy="dynamic", primary join="AuthorModel.id == BookModel.author_id")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'AuthorModel(name=%s)' % self.name'''


class AuthorModel(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book = db.relationship('Book_Author', back_populates='author')

    @classmethod
    def find_by_name(cls, name) -> "AuthorModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "AuthorModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["AuthorModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
