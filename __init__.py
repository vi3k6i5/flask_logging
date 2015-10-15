# file app/__init__.py
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from logging import Formatter

application = Flask(__name__)

handler = RotatingFileHandler('file.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

application.logger.addHandler(handler)
