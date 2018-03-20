'''
Created on 14-Mar-2016

@author: parkar_s
'''

from bookstore.src.config import BookConfig
from flask import jsonify
from ..models.core.business.books.BookRepository import BookRepository
from bookstore.src.dao.DataAccessor import DataAccessor

class BookDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(BookDao,self).__init__()
       
        
    def get_popular_books(self):
        try:
            query =("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,sub_cat_id ,category_id,sub_category.name as sub_name,category.name as name "
                    "from books "
                    "left join ("
                    "Sub_category left join Category "
                    "on Sub_Category.sub_cat_id=Category.cat_id) "
                    "on books.category_id=sub_category.sub_cat_id "
                    "where books.ratings<={} and books.ratings>{};").format(BookConfig.popular_max_rt, BookConfig.popular_min_rt)
            book_list = super(BookDao,self).read(query= query)
            return book_list
        except Exception as e:
            print(e,"get_popular_books")
        