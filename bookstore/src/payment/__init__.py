from flask.blueprints import Blueprint
from flask_restful import Api
from .PaymentApi import PaymentApi

payment= Blueprint("payment_manager",__name__)
api= Api(payment)

api.add_resource(PaymentApi,"/api/v1.0/payment/processPayment")