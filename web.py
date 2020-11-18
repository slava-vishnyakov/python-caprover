# encoding: utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/ok', methods=['GET'])
def ok():
    return 'OK'
