import os

class Config(object):
    SECRET_KEY = 'verysecretapistuff'
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://')
    CACHE_CONFIG = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://localhost'
    }

class DevelopmentConfig(Config):
    pass

config = {
    'development': DevelopmentConfig
}
