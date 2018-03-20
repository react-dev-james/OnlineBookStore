'''
Created on 16-Mar-2016

@author: parkar_s
'''

from abc import ABCMeta, abstractmethod
from bookstore.src.dao.DataAccessor import DataAccessor
from ..CategoryService import CategoryService


class CategoryDao(DataAccessor):
    '''
    classdocs
    '''

    def __init__(self):
        super(CategoryDao, self).__init__()
        self.cat = CategoryService()

    def get_books_by_id(self, category_id=None):
        try:
            query = (
                " select * from books where category_id= {};").format(category_id)
            book_list = super(CategoryDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_books_by_id", "SubCat")

    def get_all_categories(self, cat_id=None):
        self.cat = CategoryService()
        try:
            query = ("select parent.name as main_category,"
                     "parent.cat_id as cat_id, child.name as subcategory,"
                     "child.cat_id as subcategory_id "
                     "from category as parent "
                     "left join category as child "
                     "on parent.cat_id = child.parent where child.name is not NULL;")
            raw_categories = super(CategoryDao, self).read(query=query)
            categorie_list = self.cat.prepare_categories(
                raw_categories)

            return categorie_list
        except Exception as e:
            print(e, "get_books_by_id", "SubCat")
