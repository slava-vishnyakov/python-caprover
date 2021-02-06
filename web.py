# encoding: utf-8

from flask import Flask

from database import init_db

db, cache = init_db()
app = Flask(__name__, static_folder='static')


# Example:
# users = cache.remember_forever('users_addrs', lambda: db.select('select 1'))

@app.route('/ok', methods=['GET'])
def ok():
    return 'OK'
