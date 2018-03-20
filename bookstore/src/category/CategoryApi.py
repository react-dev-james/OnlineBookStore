'''
Created on 17-Mar-2016

@author: parkar_s
'''
import json

from flask import jsonify, request
from flask_restful import Resource
import jsonpickle

from bookstore.src.Database.DBConnection import DBConnect
from bookstore.src.category.dao.CategoryDao import CategoryDao


dao = CategoryDao()


class CategoryApi(Resource):
    '''
    classdocs
    '''

    def get(self):

        try:
            return jsonify({"books": dao.get_books_by_id(request.get_json()['cat_id'])})
        except Exception as e:
            print("CategoryApi", e)


class AllCategoryApi(Resource):

    def get(self):

        try:
            data = dao.get_all_categories()
            if data is not None:
                return jsonify({"categoryList": json.loads(jsonpickle.dumps(data, unpicklable=False))})
            else:
                raise
        except Exception as e:
            print("AllCategoryApi", e)
