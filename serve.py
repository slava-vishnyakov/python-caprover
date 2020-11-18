import os
import waitress
import web

waitress.serve(web.app, port=int(os.environ.get('PORT', 5000)), url_scheme='http', threads=25, asyncore_use_poll=True)
