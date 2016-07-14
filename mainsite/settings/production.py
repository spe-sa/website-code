#from __future__ import absolute_import # optional, but I like it
from .common import *

# Development overrides
DEBUG = False
ENVIRONMENT = "PROD"
WS_EVENTS_URL = 'http://iisprod1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3'
WS_EVENTS_GENERIC_URL = 'http://iisprod1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList4'

# make all loggers use the file & make sure debugging is turned to warning.
for logger in LOGGING['loggers']:
    # LOGGING['loggers'][logger]['handlers'] = ['file']
    if LOGGING['loggers'][logger]['level'] == 'DEBUG':
        LOGGING['loggers'][logger]['level'] = 'ERROR'

