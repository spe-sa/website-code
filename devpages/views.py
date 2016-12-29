import os
import imp
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.template import TemplateDoesNotExist
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

# This view is called from DevpagesFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.


def devpage(p_request, p_url):
    """
    I have no idea how to do this.  I am going to try to look up the template a couple of ways.  I
    will do nothing if I don't find one.  If I do I will try to load the context data and then
    render the template.  Here goes...
    """
    url = p_url
    if url.endswith('.html/'):
        url = url[0: len(url) -1]
    # all templates end in .html or else we skip
    if not url.endswith('.html'):
        raise Http404
    # all templates start with a relative path
    if url.startswith('http:'):
        raise Http404
    # strip off any language locale since that doesn't exist for templates
    if url.startswith('/en'):
        url = url[3:]
    # urls will always be in the devpages app?  what does this mean for static files vs not having it?
    if not url.startswith('/'):
        url = '/' + url
    url = 'devpages' + url
    # if we have a template here use it otherwise we bail
    template = None
    try:
        template = loader.get_template(url)
    except TemplateDoesNotExist:
        raise Http404

    if template:
        return render_devpage(p_request, template)



@csrf_protect
def render_devpage(request, template):
    """
    Internal interface to the dev page view.
    """
    context = {}
    module_name = template.origin.loadname
    datafile_name = template.origin.name
    # strip off the html and try data.py
    if datafile_name.endswith('html'):
        datafile_name = datafile_name[0:len(datafile_name) - 4]
        datafile_name += 'data.py'
    # else:
    #     datafile_name += '.data.py'
    # try to load a data file if it is there in order to get the context
    # all data files should support get_context() or a context property
    try:
        datafile = imp.load_source(module_name, datafile_name)
    except Exception:
        datafile = None
    if datafile:
        try:
            initmethod = getattr(datafile, 'get_context')
        except AttributeError:
            initmethod = None
        if initmethod:
            context = initmethod(request)
        else:
            try:
                context = getattr(datafile, 'context')
            except AttributeError:
                context = {}
    response = HttpResponse(template.render(context, request))
    return response
