'''
Created on Mar 24, 2016

@author: Dell
'''
from bookstore.src.dao.DataAccessor import DataAccessor
from bookstore.config import userid
from bookstore.src.models.core.business.cart import Cart
from bookstore.src.models.core.business.cart.CartItem import CartItem
from bookstore.src.models.core.business.books.Book import Book

class CartDetailsDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(CartDetailsDao,self).__init__()
    
    def get_cart_with_details(self):
        query = ("select *"
                 " from cart "
                 "join book_item "
                 "on cart.item_id = book_item.item_id "
                 "join books "
                 "on books.isbn = book_item.isbn "
                 "where user_id= '{}'").format(userid)
        result = super(CartDetailsDao,self).read(query= query)
        count = 0
        cart_items = []
        total= 0.0
        book = None
        for value in result :
            count+= value['quantity']
            total = total + value['book_item.total']
            book = Book(isbn= value['ISBN'], title= value['ISBN'], authors= value['Authors'], publisher= value['Publisher'], yop= value['YOP'], available= value['Available_copies'], price= value['Price'], format= value['Format'], keywords= value['Keywords'], subject= value['Subject'], image_loc= value['image_loc'])
            cart_items.append(CartItem(book= book,isbn=value['ISBN'], quantity= value['quantity'], item_id= value['item_id'], price= value['price'], total= value['book_item.total']))
        return Cart(cart_id= result[0]['cart_id'], user_id= userid, items=cart_items,total=total, count=count)