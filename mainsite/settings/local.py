#from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides

DEBUG = True
ENVIRONMENT = "DEV"
WS_EVENTS_URL = 'http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3'
WS_EVENTS_GENERIC_URL = 'http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList4'

# tuple for old host to new host for this environment
HOST_REPLACEMENTS = (
    ('www.spe.org', 'dev.spe.org'),
)

# Overriding the templates in development to include a test page
CMS_TEMPLATES += (
    ('test.html', 'Test Page'),
)

# Add Profiling for Local Instances
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)


# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'NAME': 'django',
            'USER': 'root',
            'PASSWORD': 'root',
            'PORT': 3306
        }
}

# DATABASES = {
#     'default': {
#         'CONN_MAX_AGE': 0,
#         'ENGINE': 'django.db.backends.sqlite3',
#         'HOST': 'localhost',
#         'NAME': os.path.join(DATA_DIR, 'project.db'),
#         'PASSWORD': '',
#         'PORT': '',
#         'USER': ''
#     }
# }

