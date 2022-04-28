from flask import request
from flask_restplus.resource import Resource
from flask_restplus import fields
from flask_restplus.namespace import Namespace

from models.author import AuthorModel
from schemas.author import AuthorSchema

AUTHOR_NOT_FOUND = "Author not found."
AUTHOR_ALREADY_EXISTS = "Authorwith given id: '{}' Already exists."

author_ns = Namespace('author', description='author related operations')
authors_ns = Namespace('authors', description='Authors related operations')

author_schema = AuthorSchema()
author_list_schema = AuthorSchema(many=True)

# Model required by flask_restplus for expect
author = authors_ns.model('Author', {
    'name': fields.String('Name of the Author')
})


class Author(Resource):
    def get(self, id):
        author_data = AuthorModel.find_by_id(id)
        if author_data:
            return author_schema.dump(author_data)
        return {'message': AUTHOR_NOT_FOUND}, 404

    def delete(self, id):
        author_data = AuthorModel.find_by_id(id)
        if author_data:
            author_data.delete_from_db()
            return {'message': "Author with given id Deleted successfully"}, 200
        return {'message': AUTHOR_NOT_FOUND}, 404


class AuthorList(Resource):
    @authors_ns.doc('Get all the Authors list')
    def get(self):
        return author_list_schema.dump(AuthorModel.find_all()), 200

    @authors_ns.expect(author)
    @authors_ns.doc('Create a new Author')
    def post(self):
        author_json = request.get_json()
        name = author_json['name']
        if AuthorModel.find_by_name(name):
            return {'message': AUTHOR_ALREADY_EXISTS.format(name)}, 400

        author_data = author_schema.load(author_json)
        author_data.save_to_db()

        return author_schema.dump(author_data), 201