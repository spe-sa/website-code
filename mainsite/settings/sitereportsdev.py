#from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides

DEBUG = True
ENVIRONMENT = "sitereportsdev"
WS_EVENTS_URL = 'http://iisdev.spe.org/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3'
WS_EVENTS_GENERIC_URL = 'http://iisdev.spe.org/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList4'

# tuple for old host to new host for this environment
HOST_REPLACEMENTS = (
    ('www.spe.org', 'sitereportsdev'),
)

# Overriding the templates in development to include a test page
CMS_TEMPLATES += (
    ('test.html', 'Test Page'),
)

# make all loggers use the console.
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']
