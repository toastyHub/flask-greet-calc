from flask import Flask, request
from operations import *

app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operator>')
def calculate(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    res = operations[operator](a,b)

    return str(res)
