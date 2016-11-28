from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.utils import timezone
# import time
from .models import CarouselComponentModel

def clicked(request, component_id):
    referrer = request.META.get('HTTP_REFERER', '')
    # vid = request.COOKIES.get('vid', '')
    # ip = request.META.get('REMOTE_ADDR', '')

    component = CarouselComponentModel.objects.get(pk=component_id)
    component.clicks = component.clicks + 1
    component.save()
    href = component.link_to
    if href:
        return redirect(href)
    return redirect(referrer)


def viewed(request, component_id):
    # we only need to return something since we just need a view url request in the apache log that we can parse by component_id
    # changing to count impressions when we send instead of ajax; see view
    return HttpResponse("success")
