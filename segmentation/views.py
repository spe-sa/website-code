# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from django.utils.encoding import force_text

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from .forms import DisciplineForm

from .segment_pool import segment_pool


@require_POST
def set_segment_override(request):
    '''
    This view (re)sets an override on a specific segment.
    '''

    segment_class = request.POST.get('segment_class', None)
    segment_config = request.POST.get('segment_config', None)
    override = request.POST.get('override', None)

    segment_pool.set_override(request.user, segment_class, segment_config, override)
    return HttpResponse(force_text(_('The segment override was successfully changed.')))


def reset_all_segment_overrides(request):
    '''
    This view resets all segment overrides in one go.
    '''

    segment_pool.reset_all_segment_overrides(request.user)
    return HttpResponse(force_text(_('The all segment override were successfully reset.')))

def set_discipline(request):
    if request.method == "POST":
        form = DisciplineForm(request.POST)
        if form.is_valid():
            response = render_to_response("cookie_set.html")
            response.set_cookie("discipline", form.cleaned_data['discipline'])
            return response
    else:
        form = DisciplineForm()
    return render(request, 'set_cookie.html', {'form': form})
