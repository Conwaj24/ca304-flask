#!/usr/bin/env pipenv run python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    with open('./index.html', 'r') as f:
        return f.read()

if __name__ == "__main__":
    app.run()

