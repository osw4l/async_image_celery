from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda self: True
}

INSTALLED_APPS = [
                     'django_extensions',
                    
                 ] + INSTALLED_APPS

MIDDLEWARE = [
                 
             ] + MIDDLEWARE

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'uploader': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'OSW4L': {
            'level': 'WARNING',
            'handlers': ['console']
        }
    },
}

AUTH_PASSWORD_VALIDATORS = []
