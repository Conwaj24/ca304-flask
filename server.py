#!/usr/bin/env pipenv run python
from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import os
import json
import csv

def csv_to_dicts(csv):
    fields = csv.readline().strip().split(',')
    out = []
    for line in csv:
        d = {}
        vals = line.strip().split(',')
        for i in range(min(len(fields), len(vals))):
            d[fields[i]] = vals[i]
        out.append(d)
    return out

def csv_to_json(csv_filename):
    with open("allegiance.csv", "r") as f:
        return( json.dumps( csv_to_dicts(f)))

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
def rest():
    return Response("allegiances", mimetype="application/json")

@app.route('/allegiancedashboard')
def dash():
    return "allegiancedashboard"

if __name__ == "__main__":
    app.run(port=8000)

