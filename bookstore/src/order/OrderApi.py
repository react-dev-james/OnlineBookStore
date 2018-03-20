'''
Created on Mar 30, 2016

@author: Dell
'''
from flask import request, jsonify
from flask_restful import Resource

from bookstore.src.order.OrderDao import OrderDao


dao = OrderDao()


class OrderApi(Resource):
    '''
    classdocs
    '''

    def post(self):
        order_data = dao.get_order_details()
        return jsonify({'orderData': order_data})
