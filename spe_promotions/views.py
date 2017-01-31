from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.gis.geoip import GeoIP

import csv
import string
import socket

from mainsite.context_processors.spe_context import (
    get_visitor,
)

from mainsite.models import Customer, Web_Region_Country

from .models import (
    SimpleEventPromotion,
    SimpleEventNotLoggedInPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    SimpleEventNonMemberPromotion,
    PromotionsEventClicks,
    SimpleMembershipPromotion,
    MembershipPromotionsClicks,
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
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
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
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
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
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
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
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
    visitor = get_visitor(request)
    if 'cookie_name' in request.COOKIES:
        value = request.COOKIES['cookie_name']
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def not_logged_in(request, index):
    try:
        object = SimpleEventNotLoggedInPromotion.objects.get(pk=index)
    except SimpleEventNotLoggedInPromotion.DoesNotExist:
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
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def membership_select(request, index):
    try:
        object = SimpleMembershipPromotion.objects.get(pk=index)
    except SimpleMembershipPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    record = MembershipPromotionsClicks()
    record.promotion_title = object.title
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def membership_no_discipline(request, index):
    try:
        object = SimpleEventNoDisciplinePromotion.objects.get(pk=index)
    except SimpleEventNoDisciplinePromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    record = MembershipPromotionsClicks()
    record.promotion_title = object.title
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)


def membership_no_region(request, index):
    try:
        object = SimpleEventNoAddressPromotion.objects.get(pk=index)
    except SimpleEventNoAddressPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    object.hits += 1
    object.save()
    record = MembershipPromotionsClicks()
    record.promotion_title = object.title
    record.promotion_type = object.promotion_type
    record.promotion_id = index
    record.time = timezone.now()
    ip = request.META.get('HTTP_X_REAL_IP', 'internal')
    record.ip = ip
    if 'vid' in request.COOKIES:
        vid = request.COOKIES['vid']
    record.vid = vid
    visitor = get_visitor(request)
    if visitor:
        record.customer_id = visitor.id
    record.save()
    if object.click_url:
        url = object.click_url
    return redirect(url)



# Data Exports

def export_excel(request):
    clicks = PromotionsEventClicks.objects.all()
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="promotion_tracking.csv"'

    writer = csv.writer(response)
    writer.writerow(['Count', 'Title', 'Type', 'id', 'Time', 'IP', 'Customer Number'])
    for click in clicks:
        writer.writerow(
            [click.pk, click.promotion_title, click.promotion_type, click.promotion_id, click.time, click.ip,
             click.customer_id])
    return response


def export_detail_excel(request):
    clicks = PromotionsEventClicks.objects.all()
    g = GeoIP()
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="promotion_tracking.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Count', 'Time', 'Title', 'Type', 'id', 'Sub Type', 'Event Location', 'Time', 'IP', 'Host', 'Country', 'Region Shown', 'vid',
         'Customer Number', 'Discipline', 'Country'])
    for click in clicks:
        if click.promotion_type == "Event":
            try:
                object = SimpleEventPromotion.objects.get(pk=click.promotion_id)
                promotion_sub_type = object.event_type
                event_location = map(lambda x: x.region_name, object.regions.all())
            except:
                promotion_sub_type = 'unknown'
                event_location = 'unknown'
        else:
            promotion_sub_type = 'no subtype'
            event_location = 'web'
        # If IP is not internal use same logic as plugins to find regions shown
        ip_country = "unknown"
        ip_region = "USA"
        try:
            host = socket.gethostbyaddr(click.ip)[0]
        except:
            host = "unknown"
        if click.ip != 'internal':
            loc = g.city(click.ip)
            if loc:
                ip_country = loc['country_code3']
                try:
                    ip_region = Web_Region_Country.objects.get(country_UN=ip_country).region
                except Web_Region_Country.DoesNotExist:
                    ip_region = Web_Region_Country.objects.get(country_UN='USA').region
        cust_discipline = "unknown"
        cust_country = "unknown"
        if click.customer_id:
            try:
                cust = Customer.objects.get(pk=click.customer_id)
                cust_discipline = cust.primary_discipline
                cust_country = cust.country
            except:
                cust_discipline = "unknown"
                cust_country = "unknown"
        writer.writerow([click.pk, click.time, click.promotion_title, click.promotion_type, click.promotion_id, promotion_sub_type,
                         event_location, click.time, click.ip, host, ip_country, ip_region, click.vid, click.customer_id,
                         cust_discipline, cust_country])
    return response


def export_summary_excel(request):
    printable = set(string.printable)

    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="promotion_summary.csv"'
    writer = csv.writer(response)

    promotions = SimpleEventPromotion.objects.all().order_by('event')
    writer.writerow(
        ['id', 'Title', 'Type', 'Regions Shown', 'Disciplines Shown', 'Campaign Start', 'Campaign End', 'Impressions',
         'Last Impression', 'Click Thrus'])
    for promotion in promotions:
        title = filter(lambda x: x in printable, promotion.event)
        event_regions = map(lambda x: x.region_name, promotion.regions.all())
        event_disciplines = map(lambda x: x.name, promotion.disciplines.all())
        writer.writerow([promotion.pk, title, promotion.event_type, event_regions, event_disciplines, promotion.start,
                         promotion.end, promotion.impressions, promotion.last_impression, promotion.hits])
    return response
