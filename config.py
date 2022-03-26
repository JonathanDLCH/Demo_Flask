from distutils.debug import DEBUG

class Config:
    SECRET_KEY = 'llavesecretaparalaapp'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}