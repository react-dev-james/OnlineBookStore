'''
Created on Apr 1, 2016

@author: Dell
'''
import datetime
import random

import pymysql

from bookstore.config import userid
from bookstore.src.dao.DataAccessor import DataAccessor


class OrderDao(DataAccessor):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OrderDao, self).__init__()
        self.order_id = None

    def get_order_details(self):
        query = ("select o.Order_id,ob.ISBN,DATE_FORMAT(timestamp,'%Y-%m-%d') as orderDate,status,total,copies_ordered,discount,item_id,Title as title,"
                 "image_loc as imageLocation from orders as o join order_detail as od on od.Order_id=o.Or"
                 "der_id join order_book as ob on ob.Order_id=od.Order_id and ob.ISBN=od.ISBN "
                 "join books as b on b.ISBN= od.ISBN where login_id='{}'").format(userid)
        result = super(OrderDao, self).read(query=query)
        return result

    def insert_order_book(self, book_items=[]):

        for item in book_items:
            isbn, available = item['book']['isbn'], item['book']['available']
            query = ("insert into order_book"
                     " (order_id , isbn, copies_ordered)"
                     " values({}, '{}',{})").format(self.order_id, item['book']['isbn'], available)
            try:
                super(OrderDao, self).read(query=query)
            except pymysql.err.IntegrityError as e:
                print("duplicate book", isbn)
                pass

    def insert_into_details(self, book_items=[], shipment_id=0):

        for item in book_items:
            isbn, available = item['book']['isbn'], item['book']['available']
            query = ("insert into order_detail"
                     " (isbn,order_id, item_id, total, discount, shipment_id )"
                     " values('{}',{},'{}',{},{},{})").format(isbn, self.order_id, item['item_id'],  item['total'], 0, shipment_id)
            super(OrderDao, self).read(query=query)

    def insert_into_order(self, timestamp=None):
        self.order_id = random.randint(0, 9999999)
        current_dt = datetime.datetime.utcnow()
        query = ("insert into orders"
                 " (timestamp, login_id, status)"
                 " values ('{}','{}', '{}')").format(current_dt, userid, "Processing payment")
        super(OrderDao, self).read(query=query)
        query = ("select LAST_INSERT_ID() as id from orders")
        result = super(OrderDao, self).read(query=query)
        self.order_id = result[0]['id']
        return self.order_id
