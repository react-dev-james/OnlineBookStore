'''
Created on 20-Jul-2016

@author: Dell
'''
from flask import json, jsonify, request
from flask_restful import Resource

from bookstore.src.wishlist.dao.WishlistDao import WishlistDao


dao = WishlistDao()


class WishlistApi(Resource):

    def get(self):
        try:
            return jsonify({'status': 'success', 'data': dao.getWishlist()})
        except Exception:
            return jsonify({'status': 'failed', 'message': 'could not complete the request'})

    def post(self):
        try:
            requestData = request.json
            operationType = requestData.get('operationType')
            i = requestData.get('id')
            isbn = requestData.get('isbn')

            return jsonify({'status': 'success', 'data': dao.updateWishlist(i, isbn, operationType)})
        except Exception:
            return jsonify({'status': 'failed', 'message': 'could not complete the request'})
