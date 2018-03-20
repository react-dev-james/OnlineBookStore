'''
Created on Mar 24, 2016

@author: siddhi parkar
'''
from flask_restful import Resource
from flask import jsonify, request
from bookstore.src.cart.dao.CartDetailsDao import CartDetailsDao
import jsonpickle, json

cart_dao= CartDetailsDao()

class CartDetailsApi(Resource):
    '''
    classdocs
    '''
    '''def __init__(self):
        self.connection = DBConnect().get_connection()
        self.connection.autocommit(True)'''
    def post(self):
        try:
            frozen = jsonpickle.encode(cart_dao.get_cart_with_details())
            
            return jsonify({"cart":json.loads(frozen)})
        except Exception as e:
            print("post CartDetailsApi",e )   