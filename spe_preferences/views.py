from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FindUserForm, PrefsForm, PrefsUserSearchForm, PrefsListForm, PrefsSubmissionForm
from .models import Preference, CustomerPreference
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
                    users_found = Customer.objects.filter(first_name=cd.get('first_name'),
                                                          last_name=cd.get('last_name')).all()

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
    context = {'form': form, 'saved': saved}
    return render(request, 'spe_preferences/base.html', context)


# called to search for a customer in our cache table
# also trigger for if we disable the search or the additonal preferences selection
def additional_prefs_search(request):
    users_found = None
    user_id = ''
    saved = request.session.get('prefs_inserted', False)
    emsg = request.session.get('emsg', '')
    request.session['prefs_inserted'] = False
    request.session['emsg'] = ''

    if request.method == "POST":
        search_form = PrefsUserSearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            users_found = Customer.objects.filter(id=cd.get('customer_id'))[:50].all()
            if not users_found:
                users_found = Customer.objects.filter(email=cd.get('email'))[:50].all()
                if not users_found:
                    users_found = Customer.objects.filter(first_name=cd.get('first_name'),
                                                          last_name=cd.get('last_name'))[:50].all()
                if not users_found:
                    users_found = Customer.objects.filter(last_name=cd.get('last_name'))[:50].all()
            if users_found and users_found.count() == 1:
                for user in users_found:
                    user_id = user.id
            if not users_found:
                request.session['emsg'] = "No Matches Found."
                    # search_form.cid = user_id
                    # search_form.fields["cid"].initial = user_id
                    # search_form.cleaned_data['cid'] = user_id
    elif request.method == "GET":
        search_form = PrefsUserSearchForm(request.GET)
        user_id = request.GET.get('user_id', '')
    else:
        search_form = PrefsUserSearchForm()
    prefs_form = PrefsListForm()
    # set the choices
    prefs_form.fields['prefs'].choices = [(x.id, x) for x in Preference.objects.filter(status__in=['ACTIVE'])]
    context = {'search_form': search_form, 'users_found': users_found, 'prefs_form': prefs_form, 'cid': user_id,
               'saved': saved, 'emsg': emsg}
    return render(request, 'spe_preferences/additional_preferences.html', context)

# called to insert the membernumber and preferences into the database and then return a blank record with an alert
def additional_prefs_insert(request):
    if request.method == "POST":
        meeting_id = "16ATCE"
        selection_list = request.POST.getlist('prefs')
        customer_id = request.POST.get('customer_id', None)
        if customer_id:
            try:
                # remove all records for this guy for this meeting
                CustomerPreference.objects.filter(customer_id=customer_id, meeting_id=meeting_id).delete()
                for selection in selection_list:
                    try:
                        id = int(selection)
                        p = Preference.objects.get(pk=id)
                        result = CustomerPreference()
                        result.meeting_id = meeting_id
                        result.customer_id = customer_id
                        result.preference = p
                        result.save()
                    except Exception as save_e:
                        request.session['emsg'] = save_e
                if not request.session['emsg']:
                    request.session['prefs_inserted'] = True
            except Exception as insert_e:
                request.session['emsg'] = insert_e
        else:
            request.session['emsg'] = "Customer id was not found with submission.  Unable to save."
    else:
        request.session['emsg'] = "Invalid save method.  Preferences were not saved."
    return redirect('add_prefs_search')

def submit_prefs(request):
    if request.method == "POST":
        search_form = PrefsUserSearchForm(request.POST)
        prefs_form = PrefsSubmissionForm(request.POST)
        if prefs_form.is_valid():
            prefs = prefs_form.save(commit=False)
            prefs.when_submitted = timezone.now()
            prefs.save()
            return redirect('add_prefs_search', {'saved': True})
    else:
        prefs_form = PrefsForm()
        search_form = FindUserForm()
    context = { 'prefs_form': prefs_form, 'saved' : False, 'search_form': search_form}
    return render(request, 'spe_preferences/submit_prefs.html', context)

