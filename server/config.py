import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_URL = "postgresql://postgres:docker@localhost:5432/backtester"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
