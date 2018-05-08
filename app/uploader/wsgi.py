"""
WSGI config for formatcom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

PROJECT_NAME = os.environ.get('PROJECT_NAME')
PROJECT_SETTINGS = '{0}.settings'.format(PROJECT_NAME)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", PROJECT_SETTINGS)

application = get_wsgi_application()
