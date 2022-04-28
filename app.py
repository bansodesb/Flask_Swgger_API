import flask_restful
import flask_restplus
from flask import Flask, Blueprint, jsonify
from flask_restful import reqparse, Api, Resource

from ma import ma
from db import db

from resources.author import Author, AuthorList, author_ns, authors_ns
from resources.book import Book, BookList, book_ns, books_ns
from marshmallow import ValidationError

app = Flask(__name__)
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = flask_restplus.Api(bluePrint, doc='/doc', title='Books and Authors API')
app.register_blueprint(bluePrint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

api.add_namespace(book_ns)
api.add_namespace(books_ns)
api.add_namespace(author_ns)
api.add_namespace(authors_ns)



@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


book_ns.add_resource(Book, '/<int:id>')
books_ns.add_resource(BookList, "")
author_ns.add_resource(Author, '/<int:id>')
authors_ns.add_resource(AuthorList, "")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)