
import os
from . import create_app

app = create_app(os.environ.get('PROFILE', 'development'))
