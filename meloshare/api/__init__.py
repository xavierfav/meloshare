from flask_flash import Flash
from config import config
from extensions import EXTENSIONS
from resources import RESOURCES
import os
import logging

def create_app(profile=None):
    logging.basicConfig(filename='meloshare.log', level='INFO')
    if profile is None:
        profile = os.environ.get('PROFILE', 'development')
    flash = Flash(
        resources=RESOURCES,
        config=config,
        profile=profile,
        extensions=EXTENSIONS)
    return flash.app
