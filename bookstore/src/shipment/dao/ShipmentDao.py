'''
Created on Mar 30, 2016

@author: Dell
'''
from bookstore.src.dao.DataAccessor import DataAccessor
import datetime
from datetime import timedelta
from bookstore.config import userid
class ShipmentDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(ShipmentDao,self).__init__()
        self.address_id = 0
        
    def add_user_addr(self, address):
        try:
            qry = ("insert into address(country, state, city, zipcode, street, building, room_no) "
            "values('{}', '{}', '{}', {}, '{}', '{}', {})").format(address['country'], address['state'], address['city'], int(address['zipcode']), address['street'], address['building'], int(address['room_no']))
            qry_c = """select LAST_INSERT_ID() as id from address"""
            super(ShipmentDao,self).read(query= qry)
            result= super(ShipmentDao,self).read(query= qry_c)
            self.address_id = result[0]['id']
            qry_update = ("""update customer set address = {}""").format(self.address_id)
            super(ShipmentDao,self).read(query=qry_update)
            return self.address_id
        except Exception as e:
            print("exception in address",e)    
            
            
    def add_user_shipment(self, type="Home delivery", promised_date=None, delivery_date = None):        
        dt=(datetime.datetime.utcnow() + timedelta(hours = 24))
        delivery_date = promised_date = dt.strftime("%y-%m-%d %H:%M:%S")
        query=("insert into shipment"
               " (address_id, type, promised_date, delivery_date, user_id)"
               " values({}, '{}', '{}', '{}', '{}')").format(self.address_id, type, delivery_date,promised_date, userid)
        super(ShipmentDao,self).read(query=query)
        query =("select LAST_INSERT_ID() as id from shipment where user_id = '{}'").format(userid)
        result= super(ShipmentDao,self).read(query=query)
        return [result[0]['id'], delivery_date]
            