#from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides

DEBUG = True
ENVIRONMENT = "DEV"
WS_EVENTS_URL = 'http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3'
WS_EVENTS_GENERIC_URL = 'http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList4'

# Overriding the templates in development to include a test page
CMS_TEMPLATES += (
    ('test.html', 'Test Page'),
)

# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '/tmp/redis.sock',
    },
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'