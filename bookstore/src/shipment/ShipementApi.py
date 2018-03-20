'''
Created on Mar 30, 2016

@author: Dell
'''
from flask import request
from bookstore.src.shipment.dao.ShipmentDao import ShipmentDao
from flask_restful import Resource

dao = ShipmentDao()
class ShipementApi(Resource):
    '''
    classdocs
    '''

    def post(self):
        id = dao.add_user_addr(request.json)
        return id