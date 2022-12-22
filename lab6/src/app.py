#!/usr/bin/env python3
from flask import Flask, request, jsonify
import xml.etree.ElementTree as et

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    result = {}
    xml_data = request.data
    params = et.fromstring(xml_data)
    string =  params.find("str")
    if string != None:
        result['lowercase'] = sum(map(str.islower, string))
        result['digits']    = sum(map(str.isdigit, string))
        result['uppercase'] = sum(map(str.isupper, string))
        result['special']   = sum(not char.isalpha() and not char.isdigit() for char in string)

    num1 = params.find('num1')
    num2 = params.find('num2')
    print(num1, num2)
    if num1 != None and num2 != None:
        a, b = int(num1.text), int(num2.text)
        result['sum'] = a + b
        result['sub'] = a - b
        result['mul'] = a * b
        result['div'] = a // b
        result['mod'] = a % b
    return jsonify(result)