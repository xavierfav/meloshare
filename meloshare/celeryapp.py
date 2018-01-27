from celery import Celery
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

broker_url = os.environ['BROKER_URL']
result_backend = os.environ.get('RESULT_BACKEND')

app = Celery(__name__)
app.config_from_object(__name__)
task_track_started = True
print app.conf
