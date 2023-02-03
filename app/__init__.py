# myapp/app/__init__.py
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

from . import routes