#!/usr/bin/env python3
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def hello():
    params = request.args.to_dict()
    if params["cmd"] == "time":
        return str(time.strftime("%H:%M:%S"))
    if params["cmd"] == "rev":
        return reversed(params["rev"])
    return "Hello world!"
