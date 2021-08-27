import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/pp-c'