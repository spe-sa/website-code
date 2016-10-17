from django.http import HttpResponsePermanentRedirect

def url_redirect(request):
    return HttpResponsePermanentRedirect("/en/dashboard/#/main/?roll=60000")
