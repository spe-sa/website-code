from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext  # ,Context,
from .forms import FindUserForm, PrefsForm
from mainsite.models import Customer
from django.utils import timezone


def hello_world(request):
    return HttpResponse("Bonjour")


def find_user(request):
    users_found = None
    if request.method == "POST":
        form = FindUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users_found = Customer.objects.filter(id=cd.get('constituent_id')).all()
            if not users_found:
                users_found = Customer.objects.filter(email=cd.get('email')).all()
                if not users_found:
                    users_found = Customer.objects.filter(first_name=cd.get('first_name'), last_name=cd.get('last_name')).all()

#            form = FindUserForm()
    else:
        form = FindUserForm()
    context = {'form': form, 'users_found': users_found}
    return render(request, 'spe_preferences/search.html', context)


def prefs_new(request):
    saved = None
    if request.method == "POST":
        form = PrefsForm(request.POST)
        if form.is_valid():
            prefs = form.save(commit=False)
            prefs.submitted_date = timezone.now()
            prefs.save()
            saved = True
            form = PrefsForm()
    else:
        form = PrefsForm()
    context = { 'form': form, 'saved' : saved }
    return render(request, 'spe_preferences/base.html', context)
