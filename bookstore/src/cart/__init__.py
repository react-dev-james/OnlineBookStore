from flask.blueprints import Blueprint
from flask_restful import Api
from .CartApi import CartApi
from .CartDetailsApi import CartDetailsApi
from .CartApi import cartUpdateApi

cart_manager = Blueprint("cart", __name__)
api = Api(cart_manager)

api.add_resource(CartApi,"/api/v1.0/cart/getCartByUser")
api.add_resource(cartUpdateApi,"/api/v1.0/cart/addItem")
api.add_resource(CartDetailsApi, "/api/v1.0/cart/getCartDetails")