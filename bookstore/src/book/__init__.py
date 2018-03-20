from flask.blueprints import Blueprint
from flask_restful import Api

from bookstore.src.book.BookApi import BookByCategoryApi, SearchBookApi, FilterBookApi

from .BookApi import BookApi, PopularBookApi, BookDescriptionApi


book_manager = Blueprint("books", __name__)
api = Api(book_manager)

api.add_resource(BookApi, "/api/v1.0/books/getAllBooks")
api.add_resource(PopularBookApi, "/api/v1.0/books/getPopularBooks")
api.add_resource(BookByCategoryApi, "/api/v1.0/books/getBooksByCategory")
api.add_resource(SearchBookApi, '/api/v1.0/books/search')
api.add_resource(BookDescriptionApi, '/api/v1.0/books/getBookInfo')
api.add_resource(FilterBookApi, '/api/v1.0/books/filter')
