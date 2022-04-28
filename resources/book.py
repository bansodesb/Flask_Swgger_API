from flask import request
from flask_restplus import Resource, fields, Namespace

from models.book import BookModel
from schemas.author import BookSchema

BOOK_NOT_FOUND = "Book not found."

book_ns = Namespace('book', description='Book related operations')
books_ns = Namespace('books', description='Books related operations')

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

# Model required by flask_restplus for expect
book = books_ns.model('book', {
    'title': fields.String('Name of the Book')
})


class Book(Resource):

    def get(self, id):
        book_data = BookModelModel.find_by_id(id)
        if book_data:
            return book_schema.dump(book_data)
        return {'message': Book_NOT_FOUND}, 404

    def delete(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            book_data.delete_from_db()
            return {'message': "Book Deleted successfully"}, 200
        return {'message': BOOK_NOT_FOUND}, 404

    @book_ns.expect(book)
    def put(self, id):
        book_data = BookModel.find_by_id(id)
        book_json = request.get_json();

        if book_data:
            book_data.name = book_json['title']
        else:
            book_data = book_schema.load(book_json)

        book_data.save_to_db()
        return book_schema.dump(book_data), 200


class BookList(Resource):
    @books_ns.doc('Get all the Books')
    def get(self):
        return book_list_schema.dump(BookModel.find_all()), 200

    @books_ns.expect(book)
    @books_ns.doc('Create an Book')
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)
        book_data.save_to_db()

        return book_schema.dump(book_data), 201
