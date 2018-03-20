'''
Created on 23-Mar-2016

@author: parkar_s
'''
import json

from flask import jsonify, request
from flask_restful import Resource
import jsonpickle

from bookstore.src.cart.dao.CartDao import CartDao

from ..Database.DBConnection import DBConnect


dao = CartDao()


class CartApi(Resource):
    '''
    classdocs
    '''

    def get(self):
        '''
        Constructor
        '''
        pass

    def post(self):
        try:
            frozen = jsonpickle.encode(
                dao.get_cart_by_user(request.get_json()['userId']))

            return jsonify({"cart": json.loads(frozen)})
        except Exception as e:
            print("post cart", e)


class cartUpdateApi(Resource):
    '''
    classdocs
    '''

    def __init__(self):
        self.connection = DBConnect().get_connection()
        self.connection.autocommit(True)

    def get(self):
        '''
        Constructor
        '''
        pass

    def post(self):

        try:

            return jsonify(dao.updatecart(request.get_json()))
        except Exception as e:
            print("post cart", e)
