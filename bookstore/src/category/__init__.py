from flask.blueprints import Blueprint
from flask_restful import Api
from .CategoryApi import CategoryApi,AllCategoryApi
category= Blueprint("category",__name__)
api= Api(category)

api.add_resource(CategoryApi,"/api/v1.0/getBookByCategory")
api.add_resource(AllCategoryApi,"/api/v1.0/categories/getallCategories")