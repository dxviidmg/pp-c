from app import app, api
from .models import Store, Product, StoreProduct
from flask import jsonify
import json

@app.route('/stores')
def getStores():
    stores = Store.query.all()
    return json.dumps(Store.serialize_list(stores))

@app.route('/products')
def getProducts():
    products = Product.query.all()
    return json.dumps(Product.serialize_list(products))