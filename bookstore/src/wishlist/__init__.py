from flask.blueprints import Blueprint
from flask_restful import Api
from .WishlistApi import WishlistApi

wishlist_mgr = Blueprint('wishlist_mgr', __name__)
api = Api(wishlist_mgr)

api.add_resource(WishlistApi, '/api/v1.0/user/wishlist')
