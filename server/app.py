#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_client():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def test_print(parameter):
    print(parameter)
    return parameter

@app.route('/math/<int:num1>/<op>/<int:num2>')
def test_math(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':  
        result = num1 / num2
    elif op == '%':    
        result = num1 % num2
    else:
        return 'Invalid operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
