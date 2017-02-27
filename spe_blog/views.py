from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse

from django.contrib.gis.geoip import GeoIP

import csv
import string
import socket

# import datetime
# import sys

from .models import Article, Brief, Issue, Publication, ArticleViews, BriefViews
from mainsite.models import Customer, Web_Region, Web_Region_Country, Tier1Discipline

from mainsite.context_processors.spe_context import (
    get_context_variable,
    get_visitor, )

from netaddr import IPAddress

exclude_agents = ['bot', 'spider', 'crawl', 'search', 'python', 'miketest', '8legs', 'ltx71', 'icevikatam', 'goldfire', 'fetch', 'archive', 'metauri', 'go-http-client', 'jetty', 'java', 'php', 'drupal', 'coldfusion', 'idg/uk', 'default', 'downnotifier', 'jakarta', 'grammarly', 'check', 'scoutjet' ]


def article_links(request):
    # get all the articles we want to provide links to
    articles = Article.objects.filter(published=True)
    briefs = Brief.objects.filter(published=True)
    # todo: decide if we want to do any additional filtering
    context = {'articles': articles,
               'briefs': briefs
               }
    return render(request, 'spe_blog/crawler_index.html', context)


def article_index(request):
    # get parameters if we posted/ if not get them from GET in case we refresh the page
    pub = request.POST.get("pub", None)
    if (pub == None):
        pub = request.GET.get("pub", None)
    vol = request.POST.get("vol", None)
    if (vol == None):
        vol = request.GET.get("vol", None)
    issue = request.POST.get("issue", None)
    if (issue == None):
        issue = request.GET.get("issue", None)
    search_term = request.POST.get('search', None)
    if (search_term == None):
        search_term = request.GET.get("search", None)
    try:
        search_id = int(search_term)
    except Exception:
        search_id = 0

    published = request.POST.get("published", None)
    if (published == None):
        published = request.GET.get("published", None)
    # convert the string to boolean for compares
    if (published == 'True'):
        published = 1
    elif (published == 'False'):
        published = 0
    else:
        published = None
    show_details = request.POST.get("show_details", None)
    if (show_details == None):
        show_details = request.GET.get("show_details", False)
    render_type = request.POST.get("render", None)
    if (render_type == None):
        render_type = request.GET.get("render", 'admin')
    limit_selected = request.POST.get("limit_results", None)
    if (limit_selected == None):
        limit_selected = request.GET.get("limit_results", 200)
    form_url = request.path

    filter = ''
    if not form_url:
        form_url = request.META.get("HTTP_REFERER", "localhost")

    articles = Article.objects.order_by('-date')
    if (pub):
        articles = articles.filter(publication__code__exact=pub)
        filter = build_filter(filter, " publicaton=" + pub)
    if (vol):
        articles = articles.filter(print_volume__exact=vol)
        filter = build_filter(filter, " volume=" + vol)
    if (issue):
        articles = articles.filter(print_issue__exact=issue)
        filter = build_filter(filter, " issue=" + issue)
    if (published != None):
        articles = articles.filter(published__exact=published)
        filter = build_filter(filter, " only published")
    if (search_term):
        if (search_id != 0):
            articles = articles.filter(Q(id=search_id) | Q(title__icontains=search_term))
        else:
            articles = articles.filter(title__icontains=search_term)
        filter = build_filter(filter, " title or id contains '" + search_term + "'")
    articles = articles[:limit_selected]
    if (search_term == None):
        search_term = ''

    # get a list of publication codes to send to build the drop down from
    pub_list = Publication.objects.values_list('code', flat=True)

    context = {'articles': articles,
               'pub_list': pub_list,
               'pub_selected': pub,
               'vol_selected': vol,
               'issue_selected': issue,
               'search_selected': search_term,
               'published_selected': published,
               'form_url': form_url,
               'render_type': render_type,
               'filter': filter,
               'show_details': show_details,
               'type': 'article'
               }
    return render(request, 'spe_blog/article_index.html', context)


def build_filter(current_filter, append_string):
    if (len(current_filter) > 0):
        current_filter += " and"
    current_filter += append_string
    return current_filter


def brief_index(request):
    # get parameters if we posted/ if not get them from GET in case we refresh the page
    pub = request.POST.get("pub", None)
    if (pub == None):
        pub = request.GET.get("pub", None)
    vol = request.POST.get("vol", None)
    if (vol == None):
        vol = request.GET.get("vol", None)
    issue = request.POST.get("issue", None)
    if (issue == None):
        issue = request.GET.get("issue", None)
    search_term = request.POST.get('search', None)
    if (search_term == None):
        search_term = request.GET.get("search", None)
    try:
        search_id = int(search_term)
    except Exception:
        search_id = 0

    search_region = request.POST.get('region', None)
    if (search_region == None):
        search_region = request.GET.get("region", None)
    published = request.POST.get("published", None)
    if (published == None):
        published = request.GET.get("published", None)
    # convert the string to boolean for compares
    if (published == 'True'):
        published = 1
    elif (published == 'False'):
        published = 0
    else:
        published = None
    show_details = request.POST.get("show_details", None)
    if (show_details == None):
        show_details = request.GET.get("show_details", False)
    render_type = request.POST.get("render", None)
    if (render_type == None):
        render_type = request.GET.get("render", 'admin')
    limit_selected = request.POST.get("limit_results", None)
    if (limit_selected == None):
        limit_selected = request.GET.get("limit_results", 200)
    form_url = request.path

    filter = ''
    if not form_url:
        form_url = request.META.get("HTTP_REFERER", "localhost")

    articles = Brief.objects.order_by('-date')
    if (pub):
        articles = articles.filter(publication__code__exact=pub)
        filter = build_filter(filter, " publicaton=" + pub)
    if (vol):
        articles = articles.filter(print_volume__exact=vol)
        filter = build_filter(filter, " volume=" + vol)
    if (issue):
        articles = articles.filter(print_issue__exact=issue)
        filter = build_filter(filter, " issue=" + issue)
    if (search_region):
        articles = articles.filter(region__region_name__iexact=search_region)
    if (published != None):
        articles = articles.filter(published__exact=published)
        filter = build_filter(filter, " only published")
    if (search_term):
        if (search_id != 0):
            articles = articles.filter(Q(id=search_id) | Q(title__icontains=search_term))
        else:
            articles = articles.filter(title__icontains=search_term)
        filter = build_filter(filter, " title or id contains '" + search_term + "'")
    articles = articles[:limit_selected]
    if (search_term == None):
        search_term = ''

    # get a list of publication codes to send to build the drop down from
    pub_list = Publication.objects.values_list('code', flat=True)
    # get a list of regions to send to build the drop down from
    region_list = Web_Region.objects.values_list('region_name', flat=True)

    context = {'articles': articles,
               'pub_list': pub_list,
               'pub_selected': pub,
               'vol_selected': vol,
               'issue_selected': issue,
               'search_selected': search_term,
               'published_selected': published,
               'form_url': form_url,
               'render_type': render_type,
               'filter': filter,
               'show_details': show_details,
               'type': 'brief',
               'region_list': region_list,
               'region_selected': search_region
               }
    return render(request, 'spe_blog/brief_index.html', context)


def article_detail(request, article_id):
    q = get_object_or_404(Article, pk=article_id)
    ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        q.article_hits += 1
        q.article_last_viewed = timezone.now()
        q.save()
        record = ArticleViews()
        record.article = q.id
        record.time = timezone.now()
        record.ip = ip
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    i = Issue.objects.filter(publication=q.publication).order_by('-date')[:1]
    t = q.publication.code + "_base.html"
    t = t.lower()
    ur = q.publication.subscription_url
    return render(request, 'spe_blog/article_detail.html',
                  {
                      'article': q,
                      'issues': i,
                      'base_template': t,
                      'show_subscribe_url': ur,
                  })


def brief_detail(request, brief_id):
    q = get_object_or_404(Brief, pk=brief_id)
    ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            [y in user_agent.lower() for y in exclude_agents]):
        q.article_hits += 1
        q.article_last_viewed = timezone.now()
        q.save()
        record = BriefViews()
        record.article = q.id
        record.time = timezone.now()
        record.ip = ip
        if 'vid' in request.COOKIES:
            vid = request.COOKIES['vid']
        record.vid = vid
        visitor = get_visitor(request)
        if visitor:
            record.customer_id = visitor.id
        record.save()
    i = Issue.objects.filter(publication=q.publication).order_by('-date')[:1]
    t = q.publication.code + "_base.html"
    t = t.lower()
    ur = q.publication.subscription_url
    return render(request, 'spe_blog/brief_detail.html',
                  {
                      'brief': q,
                      'issues': i,
                      'base_template': t,
                      'show_subscribe_url': ur,
                  })


def issue(request, publication_code):
    issues = Issue.objects.filter(publication__code=publication_code.upper()).order_by('-date')
    pub = get_object_or_404(Publication, code=publication_code.upper())
    if publication_code.upper() in ['WWW', 'JPT', 'TWA', 'HSE']:
        t = "www_base.html"
    else:
        t = pub.code + "_base.html"
    t = t.lower()
    context = {
        'issues': issues,
        'publication_code': publication_code,
        'show_subscribe_url': pub.subscription_url,
        'base_template': t,
    }

    return render(request, 'spe_blog/issues.html', context)


def brief_regional(request):
    # today = datetime.datetime.now()
    # we have worked it out where we will be passing the vol and issue to further filter from in the link
    vol = request.POST.get("vol", None)
    if (vol == None):
        vol = request.GET.get("vol", None)
    issue = request.POST.get("issue", None)
    if (issue == None):
        issue = request.GET.get("issue", None)

    articles = Brief.objects.filter(region__isnull=False)
    # articles = articles.filter(date__year=today.year, date__month=today.month)
    # for filtering to last month
    # last_month = today.month - 1 if today.month > 1 else 12
    # last_month_year = today.year if today.month > last_month else today.year - 1
    # articles = articles.filter(date__year=last_month_year, date__month=last_month)
    articles = articles.filter(publication__code='JPT')
    if vol:
        articles = articles.filter(print_volume=vol)
    if issue:
        articles = articles.filter(print_issue=issue)
    articles = articles.order_by('region', '-date')[:25]
    context = {'articles': articles, }
    return render(request, 'spe_blog/regional_briefs.html', context)


def export_article_detail_excel(request):
    clicks = ArticleViews.objects.all()
    g = GeoIP()
    printable = set(string.printable)
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="articles_tracking.csv"'

    writer = csv.writer(response)
    writer.writerow(['Count', 'Publication', 'Title', 'id', 'Time', 'IP', 'Host', 'Country', 'Region Shown', 'vid',
                     'Customer Number', 'Discipline', 'Country'])
    for click in clicks:
        if click.ip == 'internal':
            click.ip = '192.168.1.1'
        if not IPAddress(click.ip).is_private():
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
            cust_discipline = 'unknown'
            cust_country = 'unknown'
            if click.customer_id:
                try:
                    cust = Customer.objects.get(pk=click.customer_id)
                    cust_discipline = cust.primary_discipline
                    cust_country = cust.country
                except:
                    cust_discipline = 'unknown'
                    cust_country = 'unknown'
            try:
                art = Article.objects.get(pk=click.article)
                title = filter(lambda x: x in printable, art.title)
            except:
                title = 'article deleted'
            try:
                writer.writerow(
                    [click.pk, art.publication.name, title, click.article, click.time, click.ip, host, ip_country,
                     ip_region, click.vid, click.customer_id, cust_discipline, cust_country])
            except:
                writer.writerow(
                    [click.pk, art.publication.name, "Bad Title", click.article, click.time, click.ip, host, ip_country,
                     ip_region, click.vid, click.customer_id, cust_discipline, cust_country])
    return response


def export_brief_detail_excel(request):
    clicks = BriefViews.objects.all()
    g = GeoIP()
    printable = set(string.printable)
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="briefs_tracking.csv"'

    writer = csv.writer(response)
    writer.writerow(['Count', 'Publication', 'Title', 'id', 'Time', 'IP', 'Host', 'Country', 'Region Shown', 'vid',
                     'Customer Number', 'Discipline', 'Country'])
    for click in clicks:
        # If IP is not internal use same logic as plugins to find regions shown
        if click.ip == 'internal':
            click.ip = '192.168.1.1'
        if not IPAddress(click.ip).is_private():
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
            cust_discipline = 'unknown'
            cust_country = 'unknown'
            if click.customer_id:
                try:
                    cust = Customer.objects.get(pk=click.customer_id)
                    cust_discipline = cust.primary_discipline
                    cust_country = cust.country
                except:
                    cust_discipline = 'unknown'
                    cust_country = 'unknown'
            try:
                art = Brief.objects.get(pk=click.article)
                title = filter(lambda x: x in printable, art.title)
            except:
                title = 'article deleted'
            try:
                writer.writerow(
                    [click.pk, art.publication.name, title, click.article, click.time, click.ip, host, ip_country,
                     ip_region, click.vid, click.customer_id, cust_discipline, cust_country])
            except:
                writer.writerow(
                    [click.pk, art.publication.name, "Bad Title", click.article, click.time, click.ip, host, ip_country,
                     ip_region, click.vid, click.customer_id, cust_discipline, cust_country])
    return response


def export_article_disciplines_excel(request):
    articles = Article.objects.all().order_by('id')
    printable = set(string.printable)
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="article_disciplines.csv"'
    writer = csv.writer(response)
    disciplines = Tier1Discipline.objects.all()
    writer.writerow(['id', 'Publication', 'Title'] + map(lambda x: x.name, disciplines.all()))
    for article in articles:
        title = filter(lambda x: x in printable, article.title)
        writer.writerow([article.id, article.publication.name, title] + map(lambda x: x in article.disciplines.all(),
                                                                            disciplines.all()))
    return response
