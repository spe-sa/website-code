from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext  # ,Context,
from .forms import PrefsForm
from django.utils import timezone


def hello_world(request):
    return HttpResponse("Bonjour")


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
