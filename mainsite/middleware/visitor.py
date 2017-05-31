from django.conf import settings
import uuid
import urlparse, os
from mainsite.common import get_context_variables, get_visitor

FOREVER = 365 * 24 * 60 * 60 * 60 # 60 years
TRACKING_COOKIE = "vid"

# ensure everyone has a visitor identification cookie or create one:  at some point this should be replaced when they
#   authenticate to get all devices the same for a person
class VisitorMiddleware(object):
    def process_response(self, request, response):
        # determine if we have a vid cookie
        vid = request.COOKIES.get(TRACKING_COOKIE, None)
        if not vid:
            # attempt to set one forever
            response.set_cookie(TRACKING_COOKIE, value=make_uuid(), max_age=FOREVER)
        return response

def make_uuid():
    return str(uuid.uuid4())

# try loading the visitor and variables to the request object instead of context for plugins to be able to use
# NOTE: we believe this will reduce the number of database hits for many plugins on a page
class CustomerMiddleware(object):
    def process_request(self, request):

        url = request.get_full_path()
        path = urlparse.urlparse(url).path
        ext = os.path.splitext(path)[1]
        request.ext = ext

        # we have a few exceptions we need to have our variables set for (see the urls.py)
        if path == '/en/staff/articlesandbriefs/sitemap.xml' or path == '/staff/articlesandbriefs/sitemap.xml':
            ext = ""

        if not ext:
            request.variables = get_context_variables(request)
            request.visitor = get_visitor(request)
        return