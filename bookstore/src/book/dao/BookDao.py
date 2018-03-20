'''
Created on 14-Mar-2016

@author: parkar_s
'''

from flask import jsonify

from bookstore.src.config import BookConfig
from bookstore.src.dao.DataAccessor import DataAccessor

from ...category.CategoryService import CategoryService
from ...models.core.business.books.BookRepository import BookRepository
from ...searchengine import SearchEngine

searchEngine = SearchEngine()


class BookDao(DataAccessor):
    '''
    classdocs
    '''
    __collection__ = "books"

    def __init__(self):
        '''
        Constructor
        '''
        super(BookDao, self).__init__()
        #self.collection = self.database[self.__collection__]
        self.categoryService = CategoryService()
        self.bookRepo = None
        self.sortMapper = {
            0: {'reverse': False, 'key': 'isbn'},
            1: {'reverse': False, 'key': 'price'},
            2: {'reverse': True, 'key': 'yop'}
        }

    def get_popular_books(self):
        book_list = list()
        try:
            query = ("select books.isbn as isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc, category_id "
                     "from books"
                     " left join rating"
                     " on rating.isbn = books.isbn"
                     " where rating.score <={} and rating.score> {};").format(BookConfig.popular_max_rt, BookConfig.popular_min_rt)

            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_popular_books")

    def get_all_books(self):
        try:
            query = (
                "select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                "available_copies, price, format, keywords, subject,image_loc "
                "from books")
            book_list = super(BookDao, self).read(query=query)
            self.bookRepo = BookRepository(book_list)
        except Exception as e:
            print(e, "get_all_books")

    def get_all_books_by_cat(self):
        try:
            query = (
                "select books.title ,books.category_id, category.name from books left join category on books.category_id = category.cat_id;")
            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_all_books")

    def get_books_by_category(self, catData):
        categories = self.categoryService.getCategoriesById(
            catData[1], catData[0])

        print(categories)
        try:
            if len(categories) == 0:
                return []
            categoryList = str(tuple(categories))
            if len(categories) == 1:
                categoryList = '(' + str(categories[0]) + ')'
            query = ("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,cc.name as childcategory "
                     "from books"
                     " inner join category cc "
                     "on cc.cat_id = books.category_id "
                     "where cc.cat_id in " + categoryList)
            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_all_books")

    def searchBooks(self, query, filterList=[]):
        return searchEngine.searchBooks(query, filterList=filterList)

    def getBookInfo(self, isbn):
        query = ("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                 "available_copies, price, format, keywords, subject,image_loc,description from books as b"
                 " left join category as c on b.Category_id = c.cat_id where b.ISBN='{}'").format(isbn)
        queryR = ("select * from rating where ISBN='{}'").format(isbn)
        result = super(BookDao, self).read(query=query)
        ratingResult = super(BookDao, self).read(query=queryR)
        return {'book': result[0], 'ratings': ratingResult}

    def filterBooks(self, sortParam=0, filterParam=None, searchText=None):
        bookList = []

        if filterParam is not None:
            bookList = self.get_books_by_category(
                filterParam)

        if searchText is not None and searchText is not '':
            bookList = self.searchBooks(
                searchText, [book.get('isbn') for book in bookList])

        if sortParam is not None:
            bookList.sort(key=lambda x: x.get(
                'price'), reverse=self.sortMapper.get(sortParam)['reverse'])
        return bookList

    def sortList(self, booklist=[], key='isbn'):
        booklist.sort(key='isbn')
