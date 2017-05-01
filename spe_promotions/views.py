from django.http import Http404
from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.gis.geoip import GeoIP

import csv
import string
import socket
# from netaddr import IPAddress

from mainsite.common import (
    get_visitor, get_ip, is_local_ip
)

from mainsite.models import Customer, Web_Region, Web_Region_Country, Tier1Discipline
from spe_events.models import EventType

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
from .filters import SimplePromotionFilter

exclude_agents = ['bot', 'spider', 'crawl', 'search']


def event_select(request, index):
    try:
        object = SimpleEventPromotion.objects.get(pk=index)
    except SimpleEventPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = PromotionsEventClicks()
        record.promotion_title = object.event
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def no_discipline(request, index):
    try:
        object = SimpleEventNoDisciplinePromotion.objects.get(pk=index)
    except SimpleEventNoDisciplinePromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    #   ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = PromotionsEventClicks()
        record.promotion_title = object.event
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def no_region(request, index):
    try:
        object = SimpleEventNoAddressPromotion.objects.get(pk=index)
    except SimpleEventNoAddressPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = PromotionsEventClicks()
        record.promotion_title = object.event
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def non_member(request, index):
    try:
        object = SimpleEventNonMemberPromotion.objects.get(pk=index)
    except SimpleEventNonMemberPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = PromotionsEventClicks()
        record.promotion_title = object.event
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def not_logged_in(request, index):
    try:
        object = SimpleEventNotLoggedInPromotion.objects.get(pk=index)
    except SimpleEventNotLoggedInPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = PromotionsEventClicks()
        record.promotion_title = object.event
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def membership_select(request, index):
    try:
        object = SimpleMembershipPromotion.objects.get(pk=index)
    except SimpleMembershipPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = MembershipPromotionsClicks()
        record.promotion_title = object.title
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def membership_no_discipline(request, index):
    try:
        object = SimpleEventNoDisciplinePromotion.objects.get(pk=index)
    except SimpleEventNoDisciplinePromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = MembershipPromotionsClicks()
        record.promotion_title = object.title
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
    return redirect(url)


def membership_no_region(request, index):
    try:
        object = SimpleEventNoAddressPromotion.objects.get(pk=index)
    except SimpleEventNoAddressPromotion.DoesNotExist:
        raise Http404("Promotion does not exist")
    # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    ip = get_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
    if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        object.hits += 1
        object.save()
        record = MembershipPromotionsClicks()
        record.promotion_title = object.title
        record.promotion_type = object.promotion_type
        record.promotion_id = index
        record.time = timezone.now()
        record.ip = ip
        vid = 'no vid'
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    if object.click_url:
        url = object.click_url
    else:
        url = request.build_absolute_uri("/")
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
        ['Count', 'Time', 'Title', 'Type', 'id', 'Sub Type', 'Event Location', 'Time', 'IP', 'Host', 'Country',
         'Region Shown', 'vid',
         'Customer Number', 'Discipline', 'Country'])
    for click in clicks:
        if click.ip == 'internal':
            click.ip = '192.168.1.1'
        # if not IPAddress(click.ip).is_private():
        if not is_local_ip(click.ip):
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
            if click.ip != '192.168.1.1':
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
            writer.writerow(
                [click.pk, click.time, click.promotion_title, click.promotion_type, click.promotion_id,
                 promotion_sub_type,
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


def promotion_timeline(request):
    promotions = SimpleEventPromotion.objects.all().order_by('start')
    context = {'promos': promotions, }
    return render(request, 'spe_promotions/promotion_timeline.html', context)


def promotion_by_discipline(request):
    disciplines = Tier1Discipline.objects.filter(active=True).order_by('name')
    context = {}
    for discipline in disciplines:
        promotions = SimpleEventPromotion.objects.filter(disciplines=discipline).order_by('start')
        context.update({discipline: {'promos': promotions}, }, )
    context = {'disciplines': context}
    return render(request, 'spe_promotions/discipline_view.html', context)


def promotion_by_region(request):
    regions = Web_Region.objects.order_by('region_name').all()
    context = {}
    for region in regions:
        promotions = SimpleEventPromotion.objects.filter(regions=region).order_by('start')
        context.update({region: {'promos': promotions}, }, )
    context = {'regions': context}
    return render(request, 'spe_promotions/region_view.html', context)


def promotion_by_event_type(request):
    types = EventType.objects.filter(active=True).order_by('name').all()
    context = {}
    for type in types:
        promotions = SimpleEventPromotion.objects.filter(event_type=type).order_by('start')
        context.update({type: {'promos': promotions}, }, )
    context = {'event_types': context}
    return render(request, 'spe_promotions/event_type_view.html', context)


def filter_simple_promotions(request):
    promotion_list = SimpleEventPromotion.objects.all()
    promotion_filter = SimplePromotionFilter(request.GET, queryset=promotion_list)
    return render(request, 'spe_promotions/promotion_list.html', {'filter': promotion_filter})
