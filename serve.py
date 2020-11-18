import os
import waitress
import web

waitress.serve(web.app, port=int(os.environ.get('PORT', 80)), url_scheme='http', threads=25)