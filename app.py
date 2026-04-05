"""
This app shows how to use paths in Flask web application
"""

import os
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()
username = os.environ.get("DEFAULT_NAME", "&lt;Name not set&gt;")
app = Flask(__name__)

# http://localhost:8080/ displays "Welcome!"
@app.route('/')
def index():
    """Displays welcome message"""
    return f'<H1>Welcome {username}!</H1>'

@app.route('/healthz')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

# http://localhost:8080/person/Jane displays "Welcome Jane!". Try to use different names.
@app.route('/person/<fname>')
def greeting1(fname):
    """Displays the name provided as argument"""
    return '<H1>Welcome ' + fname + '!</H1>'


# http://localhost:8080/person/Jane/Doe displays first and last name provided
@app.route('/person/<fname>/<lname>')
def greeting2(fname, lname):
    """Displays first and last name"""
    output = '<H1>Welcome ' + fname + ' ' + lname + '!</H1>'
    return output


# http://localhost:8080/square/4 - you have to use a number to get a result
@app.route('/square/<int:anumber>')
def square(anumber):
    """Returns sqare of provided integer number"""
    result = calculate_square(anumber)
    output = f'<H1>{anumber} * {anumber} = {result} </H1>'
    return output


def calculate_square(x):
    """Calculates square root of the number"""
    return x * x
# http://localhost:8080/multiply/5/5 displays "5 * 5 = 25"
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return f'<H1>{a} * {b} = {result}</H1>'

if __name__ == "__main__":
    app.run()
