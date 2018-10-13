import os

class Config(object):
    """Base configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """ Development configurations."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configurations."""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}