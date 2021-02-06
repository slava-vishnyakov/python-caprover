import os
from urllib.parse import urlparse
from orator import DatabaseManager, Model, SoftDeletes
from orator.orm import has_one, belongs_to

from orator_cache import DatabaseManager, Cache
from dotenv import load_dotenv

load_dotenv()


def init_db():
    result = urlparse(os.environ['DATABASE_URL'])
    config = {
        'pgsql': {
            'driver': 'pgsql',
            'host': result.hostname,
            'database': result.path[1:],
            'user': result.username,
            'port': result.port,
            'password': result.password,
            'prefix': ''
        }
    }

    cache = None
    if 'REDIS_URL' in os.environ:
        result = urlparse(os.environ['REDIS_URL'])
        stores = {
            'stores': {
                'redis': {
                    'driver': 'redis',
                    'host': result.hostname or 'localhost',
                    'port': result.port or 6379,
                    'db': int(result.path[1:]) or 0
                }
            }
        }

        cache = Cache(stores)

    db = DatabaseManager(config, cache=cache)
    Model.set_connection_resolver(db)
    return db, cache


class User(SoftDeletes, Model):
    __guarded__ = []
    __dates__ = ['deleted_at']

# class Example(Model):
#     __guarded__ = []
#
#     @belongs_to('to_user_id')
#     def to_user(self):
#         return User
