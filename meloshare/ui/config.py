class Config(object):
    SECRET_KEY = 'verysecretstuff'
    DEBUG = True
    
class DevelopmentConfig(Config):
    pass

config = {
    'development': DevelopmentConfig
}
