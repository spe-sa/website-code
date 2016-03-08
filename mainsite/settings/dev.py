#from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides

DEBUG = True
ENVIRONMENT = "DEV"

# Overriding the templates in development to include a test page
CMS_TEMPLATES += (
    ('test.html', 'Test Page'),
    ('html5.html', 'JDs html5 tempate'),
    ('html5_bootstrap.html', 'JDs html5 bootstrap tempate'),
    ('spe_base.html', 'SPE Base Header & Footer with blank content area'),
    ('spe_3col.html', 'SPE 3 Column page. Homepage'),
)

# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': os.path.join(PROJECT_DIR, 'project.db'),
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

