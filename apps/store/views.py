from app import app, api
from .models import Store, Product, StoreProduct
from flask import jsonify
import json

@app.route('/stores/')
def getStores():
    stores = Store.query.all()
    return json.dumps(Store.serialize_list(stores))

@app.route('/products/')
def getProducts():
    products = Product.query.all()
    return json.dumps(Product.serialize_list(products))

@app.route('/stores/<id>', methods=['GET'])
def get_store(id):
   store = Store.query.get(id)
   return json.dumps(Store.serialize(store))

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
   product = Product.query.get(id)
   return json.dumps(Product.serialize(product))

@app.route('/check-stock-by-store-and-product/<store_id>/<product_id>', methods=['GET'])
def check_stock_of_product_in_store(store_id, product_id):
    store = Store.query.get(store_id)
    stock = StoreProduct.query.filter_by(store_id=store_id, product_id=product_id).all()

    if len(stock) == 0:
        message = 'Stock no encontrado'

    elif stock[0].stock < 5:
        message = 'Stock Insuficiente'
    else:
        message = 'Stock Suficiente'

    return json.dumps({'Message': message})

@app.route('/stock-by-store/<store_id>/', methods=['GET'])
def stock_by_store(store_id):
    stock = StoreProduct.query.filter_by(store_id=store_id).all()
    return json.dumps(StoreProduct.serialize_list(stock))
