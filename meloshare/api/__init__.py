from flask_flash import Flash
from config import config
from extensions import EXTENSIONS
from resources import RESOURCES

def create_app(profile='development'):
    app = Flash(resources=RESOURCES, config=config, profile=profile)
    return app
