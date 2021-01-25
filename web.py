# encoding: utf-8

from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)

@app.route('/ok', methods=['GET'])
def ok():
    return 'OK'
