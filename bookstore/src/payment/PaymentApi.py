'''
Created on Mar 30, 2016

@author: Dell
'''
from flask_restful import Resource
from flask import request, jsonify
from bookstore.src.payment.dao.PaymentDao import PaymentDao

dao = PaymentDao()
class PaymentApi(Resource):
    '''
    classdocs
    '''

        
       
    def post(self):
        oi, pd = dao.process_payment(request.json)
        return jsonify({"pd":pd, "order_id":oi})