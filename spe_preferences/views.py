from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader, RequestContext  # ,Context,
from .forms import FindUserForm, PrefsForm, PrefsUserSearchForm
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

# called to search for a customer in our cache table
# also trigger for if we disable the search or the additonal preferences selection
def additional_prefs_search(request):
    users_found = None
    user_id = ''
    prefs_form = PrefsForm()
    if request.method == "POST":
        search_form = PrefsUserSearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            users_found = Customer.objects.filter(id=cd.get('customer_id')).all()
            if not users_found:
                users_found = Customer.objects.filter(email=cd.get('email')).all()
                if not users_found:
                    users_found = Customer.objects.filter(first_name=cd.get('first_name'), last_name=cd.get('last_name')).all()
            if users_found and users_found.count() == 1:
                for user in users_found:
                    user_id = user.id
                # search_form.cid = user_id
                # search_form.fields["cid"].initial = user_id
                # search_form.cleaned_data['cid'] = user_id
    elif request.method == "GET":
        search_form = PrefsUserSearchForm(request.GET)
    else:
        search_form = PrefsUserSearchForm()
    context = {'search_form': search_form, 'users_found': users_found, 'prefs_form': PrefsForm(), 'cid': user_id}
    return render(request, 'spe_preferences/additional_preferences.html', context)

#called to insert the membernumber and preferences into the database and then return a blank record with an alert
def additional_prefs_insert(request):
    if request.method == "POST":
        search_form = PrefsUserSearchForm(request.POST)
        prefs_form = PrefsForm(request.POST)
        if prefs_form.is_valid():
            prefs = prefs_form.save(commit=False)
            prefs.submitted_date = timezone.now()
            prefs.save()
            # saved = True
            # prefs_form = PrefsForm()
            # search_form = FindUserForm()
            return redirect('add_prefs_search', {'saved': True})
    else:
        prefs_form = PrefsForm()
        search_form = FindUserForm()

    context = { 'prefs_form': prefs_form, 'saved' : False, 'search_form': search_form}
    return render(request, 'spe_preferences/additional_preferences.html', context)

