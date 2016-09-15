# from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext  # ,Context,

from .forms import FakeLoginForm


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FakeLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # get the referrer if any
            spe_referrer = request.session['spe-referrer']
            if spe_referrer == '':
                spe_referrer = '/'
            response = HttpResponseRedirect(spe_referrer)
            response.set_cookie("ERIGHTS", form.cleaned_data['ERIGHTS'])
            response.set_cookie("sm_constitid", form.cleaned_data['sm_constitid'])
            response.set_cookie("first_name", form.cleaned_data['first_name'])
            response.set_cookie("last_name", form.cleaned_data['last_name'])
            # clear the session
            request.session['spe-referrer'] = ''
            # send the redirect response
            return response

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FakeLoginForm()
        spe_referrer = request.META['HTTP_REFERER']
        # save off the session login variable as long as it does not contain /login
        if '/login/' not in spe_referrer:
            request.session['spe-referrer'] = spe_referrer

    return render(request, 'localhost/login/login_form.html', {'form': form})


def do_login(request):
    # create or update a cookie for each value
    if request.method == 'POST':
        form = FakeLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            context = RequestContext(request)

            template = loader.get_template('localhost/login/login_show.html')
            response = HttpResponse(template.render(context, request))
            response.set_cookie("ERIGHTS", form.cleaned_data['ERIGHTS'])
            response.set_cookie("sm_constitid", form.cleaned_data['sm_constitid'])
            response.set_cookie("first_name", form.cleaned_data['first_name'])
            response.set_cookie("last_name", form.cleaned_data['last_name'])
            # render the screen
            return response
        # Obtain our Response object early so we can add cookie information.

        else:
            # context = {'test': 'test'}
            return HttpResponse("Invalid form submission")
    else:
        return HttpResponseRedirect('/localhost/login/')


def logout(request):
        spe_referrer = request.META['HTTP_REFERER']
        # save off the session login variable as long as it does not contain /login
        if '/login/' in spe_referrer:
            spe_referrer = '/'
        response = HttpResponseRedirect(spe_referrer)
        response.delete_cookie('ERIGHTS')
        response.delete_cookie('sm_constitid')
        response.delete_cookie('first_name')
        response.delete_cookie('last_name')
        return response


def login_show(request):
    return render(request, 'localhost/login/login_show.html', {'test': 'test'})


def register_ogf(request):
    return render(request, 'google_registration.html', {'site_code': 'googleaa5ff496c6812444'})


def status_code_200(request):
    return HttpResponse("<h1>200: OK</h1>", status=200)


def status_code_301(request):
    return HttpResponse('<h1>301: Permanent Redirect</h1><p>The resource has been moved to <a href="/test/sc200">here</a>.</p><p>Please update your local links and bookmarks.</p>', status=301, location="/test/sc200")


def status_code_404(request):
    return HttpResponse("<h1>404: Resource Not Found</h1><p>The requested resource could not be found. Please check your typing or start fresh from our sitemap or search.</p>", status=404)


def status_code_410(request):
    return HttpResponse("<h1>410: Resource is Gone</h1><p>The requested resource is no longer available.</p>", status=410)


def status_code_418(request):
    return HttpResponse("<h1>418: Placeholder</h1><p>The requested resource has yet to be created.</p>", status=418)


def status_code_500(request):
    return HttpResponse("<h1>500: Server Error</h1><p>The server is experiencing a temporary problem. Please try again later.</p>", status=500)


def test_gtm(request):
    return render(request, 'test.html', { })
