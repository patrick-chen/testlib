# -*- coding: utf-8 -*-

from threading import Thread, Lock
import logging
import qt
from time import sleep
from server import run_server

server_lock = Lock()

logger = logging.getLogger(__name__)


def url_ok(url, port):
    # Use httplib on Python 2
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception("Server not started")
        return False

def init():
    logger.debug("Starting server")
    t = Thread(target=run_server)
    t.daemon = True
    t.start()

    #t1 = Thread(target=start_loading)
    #t1.start()

    logger.debug("Checking server")

    while not url_ok("127.0.0.1", 23946):
        sleep(0.1)

    logger.debug("Server started")
    qt.create_window("学习系统", "http://127.0.0.1:23946", width=1150, height=650,
                     icon='./static/img/logo_32.png', min_size=(800, 600))

init()

