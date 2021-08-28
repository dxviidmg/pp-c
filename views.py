from app import app
from apps.store.utils import load_example_data

@app.route('/load_data')
def load_data():
    load_example_data()
    
    return 'Data cargada'