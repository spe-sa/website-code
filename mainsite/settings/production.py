from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides
DEBUG = False
ENVIRONMENT = "PROD"

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}
