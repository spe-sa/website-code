from django.shortcuts import get_object_or_404, render
from django.utils import timezone
# import sys

from .models import Article, Issue, Publication

def index(request):
    articles = Article.objects.order_by('-date')
    context = {'articles': articles}
    return render(request, 'spe_blog/index.html', context)


def detail(request, article_id):
    q = get_object_or_404(Article, pk=article_id)
    q.article_hits += 1
    q.article_last_viewed = timezone.now()
    q.save()
    i = Issue.objects.filter(publication=q.publication).order_by('-date')[:1]
    t = q.publication.code + "_base.html"
    t = t.lower()
    ur = q.publication.subscription_url
    return render(request, 'spe_blog/detail.html',
                  {
                      'article': q,
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
