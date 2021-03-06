from app import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Store(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Product(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class StoreProduct(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __init__(self, store_id, product_id, stock=0):
        self.store_id = store_id
        self.product_id = product_id
        self.stock = stock

    def __repr__(self):
        return '<id {}>'.format(self.id)