from flask.blueprints import Blueprint
from flask_restful import Api
from .ShipementApi import ShipementApi

shipment= Blueprint("shipment_mgr",__name__)
api= Api(shipment)

api.add_resource(ShipementApi,"/api/v1.0/shipment/addAddress")