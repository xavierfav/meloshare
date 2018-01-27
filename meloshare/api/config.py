class Config(object):
    SECRET_KEY = 'verysecretapistuff'
    DEBUG = True
    CACHE_CONFIG = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': 'redis://localhost'
    }

class DevelopmentConfig(Config):
    pass

config = {
    'development': DevelopmentConfig
}
