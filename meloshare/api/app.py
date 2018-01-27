from . import create_app
import os

app = create_app(os.environ.get('PROFILE', 'development'))
