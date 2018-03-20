'''
Created on Mar 24, 2016

@author: Dell
'''
from ..books.Book import Book
class CartItem(object):
    '''
    classdocs
    '''


    def __init__(self,isbn=None,quantity= 0,item_id = None,price= 0.00, total =0.00, book= Book()):
        '''
        Constructor
        '''
        self.isbn = isbn,
        self.quantity = quantity
        self.item_id = item_id 
        self.price = price 
        self.total = total
        self.book = book