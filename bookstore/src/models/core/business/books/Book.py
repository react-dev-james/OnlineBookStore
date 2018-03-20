'''
Created on 14-Mar-2016

@author: parkar_s
'''
from bookstore.src.models.core.business.category.ParentCategory import Category

class Book(object):
    '''
    classdocs
    '''
    

    def __init__(self,isbn= None, title= None, authors =[],publisher=None, yop= None,available= 0,price =0.00, format=None, keywords= None, subject = None, image_loc= None ):
        '''
        Constructor
        '''
        self.isbn = isbn
        self.title = title
        self.authors = authors 
        self.publisher =publisher
        self.yop = yop
        self.available = available
        self.authors = authors 
        self.price =price
        self.format = price
        self.keywords = price
        self.subject = subject 
        self.image_loc =image_loc
    
