from django.http import Http404
from django.shortcuts import redirect

from .models import (
    SimpleEventPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    SimpleEventNonMemberPromotion,
)


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


def no_discipline(request, index):
    try:
        object = SimpleEventNoDisciplinePromotion.objects.get(pk=index)
    except SimpleEventNoDisciplinePromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def no_region(request, index):
    try:
        object = SimpleEventNoAddressPromotion.objects.get(pk=index)
    except SimpleEventNoAddressPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def non_member(request, index):
    try:
        object = SimpleEventNonMemberPromotion.objects.get(pk=index)
    except SimpleEventNonMemberPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)