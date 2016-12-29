# Based off of flat pages but no database needed for dev pages.  Concept is that we have dynamic
# urls based off of a docroot that extend from a template.  Each developer page is a template
# relative to DEVPAGES_URL.  The purpose is to bypass having to enter urls for each page we build
# which would get out of hand quickly.  Furthermore, we would like to dynamically inject the
# data context for the page template to avoid having thousands of view functions that the url calls
# based on a naming convention (<dev_page_name>.data.py)
from django.conf import settings

from .. import views
from django.http import Http404


class DevpagesFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response  # No need to check for a flatpage for non-404 responses.
        try:
            return views.devpage(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except Exception:
            if settings.DEBUG:
                raise
            return response
