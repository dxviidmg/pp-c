from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/pp-c'
app.config.from_object(Config)
#db = SQLAlchemy(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from apps.store.models import *