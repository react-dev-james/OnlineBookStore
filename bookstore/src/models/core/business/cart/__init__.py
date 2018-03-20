'''
Created on 14-Mar-2016

@author: parkar_s
'''
from functools import total_ordering


class Cart:
    '''
    classdocs
    '''
    _instance = None
    cart_id = None
    user_id = None
    items = []
    total = 0.00
    count = 0 
    _instance = None
    
    

    def __init__(self, cart_id= None, user_id= None, items=[],total=0.00, count=0 ):
        '''
        Constructor
        '''
        self.cart_id = cart_id
        self.user_id = user_id
        self.items = items
        self.total = total
        self.count = count
        
    def add_item_to_cart(self,cart_item ):  
        self.items.append(cart_item)
        
        
        
    
