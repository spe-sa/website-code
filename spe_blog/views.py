from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Q
# import sys

from .models import Article, Brief, Issue, Publication


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
               'type': 'brief'
               }
    return render(request, 'spe_blog/article_index.html', context)


def article_detail(request, article_id):
    q = get_object_or_404(Article, pk=article_id)
    q.article_hits += 1
    q.article_last_viewed = timezone.now()
    q.save()
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
    q.article_hits += 1
    q.article_last_viewed = timezone.now()
    q.save()
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

# def issue(request, publication_code):
#     issues = Issue.objects.filter(publication__code=publication_code.upper()).order_by('-date')
#     pub = get_object_or_404(Publication, code=publication_code.upper())
#     years = Issue.objects.filter(publication__code=publication_code.upper()).distinct('date.year').order_by('-date')
#     context = {'issues': issues, 'publication_code': publication_code, 'show_subscribe_url': pub.subscription_url,
#                'years': years}
#
#     return render(request, 'spe_blog/issues.html', context)
