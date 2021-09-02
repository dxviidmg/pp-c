from app import app, api
from .models import Store, Product, StoreProduct
from flask import jsonify
import json
from app import db

@app.route('/stores/')
def getStores():
    """lista de tiendas"""
    stores = Store.query.all()
    return json.dumps(Store.serialize_list(stores))

@app.route('/products/')
def getProducts():
    """lista de productos"""
    products = Product.query.all()
    return json.dumps(Product.serialize_list(products))

@app.route('/stores/<id>', methods=['GET'])
def get_store(id):
    """detalle tienda"""
    store = Store.query.get(id)
    return json.dumps(Store.serialize(store))

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    """detalle producto"""
    product = Product.query.get(id)
    return json.dumps(Product.serialize(product))

@app.route('/check-stock-by-store-and-product/<store_id>/<product_id>', methods=['GET'])
def check_stock_of_product_in_store(store_id, product_id):
    """Checa si hay suficiente stock de un producto en una tienda"""
    stock = StoreProduct.query.filter_by(store_id=store_id, product_id=product_id).first()

    if stock == None:
        message = 'Stock no encontrado'

    elif stock.stock < 5:
        message = 'Stock Insuficiente'
    else:
        message = 'Stock Suficiente'

    return json.dumps({'Message': message})

@app.route('/stock-by-store/<store_id>/', methods=['GET'])
def stock_by_store(store_id):
    """Stock por tienda"""
    stock = StoreProduct.query.filter_by(store_id=store_id).all()
    return json.dumps(StoreProduct.serialize_list(stock))

@app.route('/update-stock-by-store-and-product/<store_id>/<product_id>/<cuantity>/', methods=['PATCH'])
def update_stock_of_product_in_store(store_id, product_id, cuantity):
    """Actualiza stock en tienda"""
    stock = StoreProduct.query.filter_by(store_id=store_id, product_id=product_id).first()

    if stock == None:
        message = 'Stock no encontrado'
        return json.dumps({'Message': message})
    else:
        stock.stock = stock.stock + int(cuantity)
        db.session.commit()

    return json.dumps(StoreProduct.serialize(stock))
    