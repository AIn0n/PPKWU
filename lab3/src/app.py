#!/usr/bin/env python3
from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/")
def hello():
    params = request.args.to_dict()
    if "str" in params:
        string = params["str"]
        return json.dumps({"lowercase": sum(1 for char in string if char.islower())})
    return "no str parameter found"
