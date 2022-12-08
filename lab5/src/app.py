#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    params = request.get_json()
    print(params)
    return jsonify(params)