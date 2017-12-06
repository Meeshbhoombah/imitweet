# -*- encoding: utf-8 -*-
"""
__init__.py

initalizes the imitweet server
"""
from flask import Flask

""" SERVER """
app = Flask(__name__)

""" CONFIG """
# app.config.from_object("app.configuration.ProductionConfig") # PROD
app.config.from_object("app.configuration.DevelopmentConfig") # DEV
# app.config.from_object("app.configuration.TestingConfig") # TESTING

from app.src import dumper

