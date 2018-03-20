from flask.blueprints import Blueprint
from flask_restful  import Api
from .OrderApi import OrderApi
order_manager = Blueprint("order_manager",__name__)
api = Api(order_manager)

api.add_resource(OrderApi,"/api/v1.0/order/getOrders")