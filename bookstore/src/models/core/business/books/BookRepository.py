'''
Created on 15-Mar-2016

@author: parkar_s
'''
from bookstore.src.Trie.TRIE import TRIE

trie = TRIE()


class BookRepository(object):
    '''
    classdocs
    '''

    def __init__(self, book_list, category=None, repository_name="general"):
        '''
        Constructor
        '''
        self.books = book_list
        self.book_category = category
        self.repository_name = repository_name
        for book in book_list:
            trie.rawInsert(book.get('title'), end=book.get('isbn'))
        self.searchRepo = trie
