#!/usr/bin/env python
from app import app
from flup.server.fcgi import WSGIServer
from config import LOG_FILE, WSGI_SCRIPT


if __name__ == '__main__':
    app.debug = False
    import logging
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    WSGIServer(app, bindAddress=WSGI_SCRIPT).run()
