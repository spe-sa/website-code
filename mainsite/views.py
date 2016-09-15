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

def test_gtm(request):
    return render(request, 'test.html', { })