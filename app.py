from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/pp-c'
app.config.from_object(Config)
#db = SQLAlchemy(app)