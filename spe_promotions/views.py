from django.http import Http404
from django.shortcuts import redirect
# from .models import Promotion, SimpleEventPromotion
from .models import SimpleEventPromotion


def promo_select(request, index):
    try:
        object = Promotion.objects.get(pk=index)
    except Promotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    if object.article:
        print "needs handling"
    if object.click_url:
        url = object.click_url
    if object.click_page:
        url = object.click_page
    return redirect(url)

def event_select(request, index):
    try:
        object = SimpleEventPromotion.objects.get(pk=index)
    except SimpleEventPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)

