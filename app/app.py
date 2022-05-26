"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This Python program is a small poetry.lock file parser and visualizer for depencies
used in a project. It contains a backend written in python using flask microframework
and has a basic html front using jinja2 to render the webpages.
"""
from flask import Flask
from app.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)


        