from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

PROJECT_NAME = os.environ.get('PROJECT_NAME')
PROJECT_SETTINGS = '{0}.settings'.format(PROJECT_NAME)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_SETTINGS)

app = Celery(PROJECT_NAME)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
