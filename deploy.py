from jikanpy import Jikan
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Yes</h1>'