import os

from flask import Flask

from application.web.url_helper import DAY_SAMPLE_URL
from application.web.handlers.day_sample_handler import day_sample_handlers
from application.dal.db_config import DB_SERVER, DB_NAME

app = Flask(__name__)
app.register_blueprint(day_sample_handlers, url_prefix=DAY_SAMPLE_URL)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(DB_SERVER, DB_NAME),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
