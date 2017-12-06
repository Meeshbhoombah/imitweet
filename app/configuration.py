# -*- encoding: utf-8 -*-
"""
config.py

configuration for imitweet
"""

class Config:
    """ BASE """
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """ PROD """
    DEBUG = True

class TestingConfig(Config):
    """ TEST """
    TESTING = True

class DevelopmentConfig(Config):
    """ DEV """
    DEBUG = True

