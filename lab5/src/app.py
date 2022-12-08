#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    result = {}
    params = request.get_json()
    if 'str' in params:
        string = params['str']
        result['lowercase'] = sum(map(str.islower, string))
        result['digits'] = sum(map(str.isdigit, string))
        result['uppercase'] = sum(map(str.isupper, string))
        result['special'] = sum(not char.isalpha() and not char.isdigit() for char in string)
    return jsonify(params)