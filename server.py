from flask import Flask

app = Flask(__name__)

@app.route('/sum/<string:a>/<string:b>/')
def sum(a, b):
    return str(int(a) + int(b))

@app.route('/mul/<string:a>/<string:b>/')
def mul(a, b):
    return str(int(a) * int(b))

@app.route('/dev/<string:a>/<string:b>/')
def dev(a, b):
    return str(int(a) / int(b))

@app.route('/sub/<string:a>/<string:b>/')
def min(a, b):
    return str(int(a) - int(b))

@app.route('/pow/<string:a>/<string:b>/')
def pow(a, b):
    return str(int(a) ** int(b))

app.run(port=8080, debug=True)