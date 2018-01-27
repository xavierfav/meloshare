from flask import Flask
from config import config
from blueprints import BLUEPRINTS
from extensions import EXTENSIONS
from ..utils import register_blueprints, register_extensions
import os, logging

def create_app(profile=None):
    logging.basicConfig(filename='meloshare.log', level='INFO')
    if profile is None:
        profile = os.environ.get('PROFILE', 'development')
    app = Flask(__name__, template_folder='templates', static_folder='static')
    cfg = config[profile]
    app.config.from_object(cfg)

    from blueprints import BLUEPRINTS
    register_blueprints(app, BLUEPRINTS)

    from extensions import EXTENSIONS
    register_extensions(app, EXTENSIONS)

    return app
