"""
WSGI config for mainsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

# add the project path into the sys.path
sys.path.append('/Users/sstacha/dev/projects/djangocms/website/')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/Users/sstacha/dev/projects/djangocms/env/lib/python2.7/site-packages')

# pointing to project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainsite.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
