from db import db
from typing import List


class Book_Author(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)
    active = db.Column(db.Boolean)
    author = db.relationship('Author', back_populates='book')
    book = db.relationship('Book', back_populates='author')


'''class BookModel(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)

    author_id = db.Column(db.Integer,db.ForeignKey('author.id'),nullable=False)
    author = db.relationship("AuthorModel",)

    def __init__(self, title,author_id):
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return 'BookModel(title=%s)' % (self.title)

    def json(self):
        return {'title': self.title}'''


class BookModel(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.relationship('Book_Author', back_populates='book')

    @classmethod
    def find_by_name(cls, name) -> "BookModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "BookModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
