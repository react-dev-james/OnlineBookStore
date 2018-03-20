'''
Created on Mar 30, 2016

@author: Dell
'''
from bookstore.src.shipment.dao.ShipmentDao import ShipmentDao
from bookstore.src.order.OrderDao import OrderDao
from bookstore.src.cart.dao.CartDao import CartDao

ship_dao = ShipmentDao()
order_dao= OrderDao()
cart_dao = CartDao()
class PaymentDao(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(PaymentDao,self).__init__()
       
    def process_payment(self, data):
        
        cart_items = data['cart']['items']
        shipment_id, promised_date= ship_dao.add_user_shipment()
        order_id = order_dao.insert_into_order()
        order_dao.insert_order_book(cart_items)
        order_dao.insert_into_details(book_items=cart_items ,shipment_id=shipment_id)
       
        cart_dao.delete_items_from_cart(items= cart_items, delete_all= True,cart_id=data['cart']['cart_id'])
        return [order_id, promised_date]
        
        
        