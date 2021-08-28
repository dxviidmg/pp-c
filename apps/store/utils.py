from .models import Store, Product, StoreProduct
from app import db

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        kwargs |= defaults or {}
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except Exception:  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True



def load_example_data():
    data_stores = [{'name': 'Tienda1'}, {'name': 'Tienda2'}]
    data_products = [{'sku': '1', 'name': 'Galletas'}, {'sku': '2', 'name': 'Paleta'}, {'sku': '3', 'name': 'Refresco'}]

    for data_store in data_stores:
        get_or_create(db.session, Store, defaults=None, **data_store)

    for data_product in data_products:
        product = get_or_create(db.session, Product, defaults=None, **data_product)
        stores = Store.query.all()

        for store in stores:
            data_sp = {'product_id': product.id, 'store_id': store.id}
            get_or_create(db.session, StoreProduct, defaults=None, **data_sp)

#    products = Product.query.all()

    