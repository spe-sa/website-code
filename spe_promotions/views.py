from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone

from mainsite.context_processors.spe_context import (
    get_visitor,
)

from .models import (
    SimpleEventPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    SimpleEventNonMemberPromotion,
    PromotionsEventClicks,
)


def event_select(request, index):
    try:
        object = SimpleEventPromotion.objects.get(pk=index)
    except SimpleEventPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    record = PromotionsEventClicks()
    record.promotion_title = object.event
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
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
    record = PromotionsEventClicks()
    record.promotion_title = object.event
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
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
    record = PromotionsEventClicks()
    record.promotion_title = object.event
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
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
    record = PromotionsEventClicks()
    record.promotion_title = object.event
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)