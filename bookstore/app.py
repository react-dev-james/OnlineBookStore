'''
Created on 11-Mar-2016

@author: parkar_s
'''
from flask import Flask, redirect, render_template
from flask.blueprints import Blueprint

from bookstore.src.cart import cart_manager
from bookstore.src.order import order_manager
from bookstore.src.payment import payment
from bookstore.src.shipment import shipment
from bookstore.src.wishlist import wishlist_mgr
from .src.book import book_manager
from .src.category import category


app = Flask(__name__, static_url_path='/static')
bookstore = Blueprint("bookstore", __name__)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(bookstore)
app.register_blueprint(book_manager)
app.register_blueprint(category)
app.register_blueprint(cart_manager)
app.register_blueprint(payment)
app.register_blueprint(shipment)
app.register_blueprint(order_manager)
app.register_blueprint(wishlist_mgr)