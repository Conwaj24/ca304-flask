#!/usr/bin/env pipenv run python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/formtest')
def form():
    return render_template('form.html')

@app.route('/formsubmit', methods=['POST'])
def result():
    return request.form['name']

@app.route('/allegiances')
def json():
    return "allegiances"

@app.route('/allegiancedashboard')
def dash():
    return "allegiancedashboard"

if __name__ == "__main__":
    app.run(port=8000)

